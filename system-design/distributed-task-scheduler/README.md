# System Design: Distributed Task Scheduler

## What is a task scheduler?

Task란 특정 시간대에 특정 자원(CPU time, mememory, storage, network bandwidth, and so on)을 요구하는 계산작업의 한 단위다.
예를 들어, Facebook이나 Instagram에서 이미지 또는 비디오를 업로드할때 다음과 같은 background task가 수행된다.

1. 이미지 또는 비디오를 여러 해상도로 인코딩
2. 이미지 또는 비디오의 컨텐츠 수익화(content monetization)를 점검하기 위한 저작권 등의 검사

이미지나 비디오를 업로드하는 사람은 굳이 위 동작이 완료될 때까지 대기할 필요가 없으므로 위 작업은 task scheduler에 의해 비동기로 수행된다.
Task scheduler는 시스템 상의 제한된 계산 자원 위에서 다수의 task가 task level / system level의 목표를 만족할 수 있도록 똑똑하게 자원을 할당하는 역할을 한다.

## Distributed task scheduling

OS-level task scheduler와 Data center-level task scheduler는 다음과 같은 차이가 있다.

<img width="939" src="https://user-images.githubusercontent.com/14961526/215316523-3d9f6948-a0e0-42a5-88ec-346d5ab02b63.png">

OS task scheduler는 특정 노드의 계산 자원 위에서 local task 또는 process를 스케쥴하는 반면,
Datacenter task scheduler는 다수의 사용자로부터 요청받은 수많은 task를 데이터센터의 자원에 할당한다.

이번 system design의 목표는 다음 항목을 만족하는 datacenter level task scheduler를 설계하는 것이다.

- 다양한 경로로부터 task가 요청된다.
- Datacenter에 흩어져있는 여러 계산 자원을 활용한다.

동시에 시스템은 확장가능해야 하며(scalable), 신뢰성이 있고(reliable), 장애애 강인해야(fault-tolerant) 한다.

## Requirements

Task scheduler의 설계에 앞서 시스템의 functional / non-functional requirements를 정리해본다.

### Functional Requirements

<img width="579" src="https://user-images.githubusercontent.com/14961526/215316990-61aae8a8-4bf5-4b71-a9d7-12c28eff114b.png">

- Submit Tasks
- Allocate Resources
- Remove Tasks
- Monitor Task Execution
- Efficient Resource Utilization
- Release Resources
- Show Task Status

### Non-Functional Requiremetns

<img width="381" src="https://user-images.githubusercontent.com/14961526/215317012-77d8c936-d9f7-4765-b56d-801e0009fca2.png">

- Availability: Task를 스케쥴하고 실행하는데 있어 높은 가용성을 가져야 한다.
- Durability: 시스템이 요청받은 task는 유실되어서는 안된다.
- Scalability: 증가하는 task에 대한 대응이 가능해야 한다.
- Fault-tolerance: 시스템의 컴포넌트에 발생하는 장애에 의해 서비스가 중단되어서는 안된다.
- Bounded Waiting Time: Task가 실행되기까지 최대로 기다리는 시간에 대한 상한이 있어야 한다.

## Building blocks we will use

<img width="533" src="https://user-images.githubusercontent.com/14961526/215317229-a2901f6a-73a8-4790-8d25-e1dfda4f92b7.png">

- Rate limiter: System을 안정적으로 유지하기 위해서는 task의 수에 대한 제한이 필요하다.
- A sequencer: Task를 식별할 수 있어야 한다.
- Database: Task에 대한 정보를 저장한다.
- A distributed queue: Task의 순서를 적절하게 배열하는데 필요하다.
- Monitoring: 서비스를 안정적으로 제공하기 위해 자원의 상태나 task의 실패여부를 확인할 수 있어야 한다.

## Components

Task scheduler는 여러가지 형태가 될 수 있다.

- 특정 조직 내부에서 그들이 구축한 자원 클러스터를 이용하는 형태
- 클라우드 제공사가 다수의 클라이언트로부터 들어오는 task를 처리하는 형태

일반적으로 System Component는 다음과 같이 4가지로 나눈다.

- Clients: Task의 실행을 요청한다.
- Resources: 이 Component 상에서 Task가 실행된다.
- Scheduler: 어떤 task를 어떤 Resource에 배치할지 결정한다.

<img width="537" src="https://user-images.githubusercontent.com/14961526/215318304-8771af02-e65d-48e9-ac0c-602010df5e86.png">

또한 위 그림에 보이는 것처럼 일련의 task 요청들을 담아둘 수 있는 queue가 필요하다.

- 당장 task를 수행하기에 충분한 resource가 없을 수도 있음
- Task간의 의존성이 있는 경우 다른 Task가 끝날 때까지 대기해야 함
- Client를 Task execution으로부터 분리할 필요가 있음.

## Design

Task scheduling을 위해서는 다음과 같은 정보들이 필요하다.

- Resource Requirements: CPU cores / RAM / Disk Space / Disk Access Rate / TCP Ports 등. 하지만 Clients가 이 요구사항을 정확히 기술하는 것은 어렵다. 이 문제를 개선하기 위해 basic / regular / premium으로 resource의 등급을 나누도록 한다. Client는 설정을 통해 이 등급의 세부사항을 변경할 수 있다.
- Dependency: Task 간 의존성이 있는 경우 task의 실행순서가 보장되어야 한다. 반면 의존성이 없는 task들의 경우 동시에 실행되어 자원을 좀 더 효율적으로 사용할 수 있다.

Task schduler의 설계를 그려보면 다음과 같다.

<img width="943" src="https://user-images.githubusercontent.com/14961526/215319151-60289b9b-a3e4-4a36-b014-0f77cd6b3abd.png">

- Clients: Task를 실행하는 주체로써, 어떤 조직이거나 또는 Cloud provider의 개개인 이용자일  수 있다.
- Rate limiter: 서비스의 안정성(reliability)을 위해서는 task의 실행규모를 제약할 수 있어야 한다. (예를 들어, 시간당 X개의 task 수행만 허용.) Rate limiter는 Clients의 요금제에 따라 실행할 수 있는 task 규모를 제한한다. 만약 제한을 초과하면 `Limit Exceeded` 메시지를 반환한다.
- Task submitter: Rate limiter를 통과한 task들을 처리한다. Task submitter는 task의 요청이 급등하는 것을 대비해 single node가 아닌 클러스터로 구성한다.
- Unique ID generator: task에 식별자를 부여한다.
- Database: Task submitter는 distributed database에 task를 저장한다.
  - Relational Database (RDB): RDB는 task ID, user ID, required resources, execution caps, total number of attempts made by the client, delay tolerance 등의 정보를 저장한다.
  - Graph Database (GDB): Task 간의 의존성 정보를 다루기 위해 Directed Acyclic Graph (DAG) 형태로 task의 정보를 저장한다. 이 DAG 정보를 바탕으로 Task Scheduling을 수행한다.

### Database Schema

| Column Name          | Datatype | Description                                                                                                                                                                                                                                                          |
| -------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TaskID               | Integer  | Uniquely identifies each task.                                                                                                                                                                                                                                       |
| UserID               | Integer  | This is the ID of the task owner.                                                                                                                                                                                                                                    |
| SchedulingType       | VarChar  | This can be either once, daily, weekly, monthly, or annually.                                                                                                                                                                                                        |
| TotalAttempts        | Integer  | This is the maximum number of retries in case a task execution fails.                                                                                                                                                                                                |
| ResourceRequirements | VarChar  | Clients have to specify the type of the offered resource categories, such as Basic, Regular, or Premium. The specified resource category is saved in the form of a string in the RDB.                                                                                |
| ExecutionCap         | Time     | This is the maximum time allowed for the task execution. (This time starts when a resource is allocated to the task.)                                                                                                                                                |
| Status               | VarChar  | This can be waiting, in progress, done, or failed.                                                                                                                                                                                                                   |
| DelayTolerance       | Time     | This indicates how much delay we can sustain before starting a task.                                                                                                                                                                                                 |
| ScriptPath           | VarChar  | The path of the script that needs to be executed. The script is a file placed in a file system. The file should be made accessible so that it can be executed, just like how we mount Google Drive in the Google Colaboratory and then execute our code files there. |

- Batching and prioritization: Task가 RDB에 저장되면 Task들은 Batch로 묶인다. 우선순위의 경우 delay tolerace / execution cap 등 task의 여러가지 성격에 의해 결정한다. Top K priority의 task들은 distributed queue에 넣어진다. Queue service는 비용을 소요하는 요인이므로 최대한 각 task들이 Queue를 이용하는 시간을 줄이는 것이 좋다. 또한 Scheduling Type에 긴 주기마다 실행하는 Task가 존재하므로 Task에 대한 정보를 Storage에 저장해야 한다.
- Distributed Queue: Queue와 Queue Manager로 구성된다. Queue manager는 Queue에 Task를 add / update / delete하고, task가 성공적으로 실행될 때까지 task를 queue에서 잘 유지하는 역할을 한다. 예를 들어 Task의 실행이 실패했을 경우 Queue manager는 task가 다시 queue에 들어가도록 한다. (설정한 재시도 횟수만큼 다시 시도)
- Resource Manager: 가용한 자원에 대한 정보를 가지고 있으며, task의 정상 실행 여부를 Queue Manager에 반환한다. 만약 요청받은 task를 수행할 수 있는 자원이 없을 경우 task는 종료되고 task submitter를 통해 client에게 task 수행 실패 여부를 전달한다.
- Monitoring Service: Resource에 대한 healthcheck를 수행하고, 만약 어떤 resource에 문제가 있을시에는 Administrator에게 알려서 해당 Resource를 수리하거나 교체할 수 있도록 한다. 또한 사용하지 않는 Resource가 있을 경우 Admin으로 하여금 Resource의 전원을 내리거나 제거하도록 할 수도 있다.

## Task Submitter

Task submitter가 a single point of failure가 되는 것을 방지하기 위해 Task submitter는 다수 노드의 Cluster로 구축한다. 각 node는 unique ID generator를 통해 task에 ID를 부여하고 task의 정보를 Database에 쌓는 역할을 한다. 

Cluster manager는 각 node에 heartbeat를 보내서 정상 작동여부를 확인하며, 각 node는 다루고 있는 task의 정보를 cluster manager에 업데이트한다. Cluster manager는 task와 node ID의 리스트 정보를 유지하고, 특정 task의 실행을 실패했을 경우 해당 task의 수행을 클러스터의 다른 노드로 hand-over한다. 

Cluster manager는 자기복제가 가능하다. (itself replicated)

## Queueing

Queue에서 task를 다루는 가장 간단한 방법은 First-in-first-out (FIFO)지만, 이 방법은 task의 우선순위를 고려하지 않으므로 다음과 같이 queue의 카테고리를 나눠서 운영하는 방법을 사용할 수 있다.

<img width="579" src="https://user-images.githubusercontent.com/14961526/215322926-7f314cf8-03c9-4ad2-8677-56ae30fe2bf7.png">

- Urgent Tasks: 지연되어서는 안되는 Task

- Tasks that can be delayed: 지연가능한 Task. 설정한 지연 시간에 도달한 Task는 Urgent Tasks로 옮겨야 한다.

- Periodic Tasks: 주기적으로 실행하는 Task

## Execution cap

Execution cap은 task 실행에 허용된 최대 시간을 의미한다. 의도치 않게 (e.g. 버그) 리소스를 점유하고 오랜 시간동안 실행되는 Task는 다른 Task의 실행을 막을 수 있으므로 매우 중요한 파라미터다. Task의 실행시간이 Exeution cap에 도달하면 task를 종료하고 Resource를 반환하며 다음 task를 queue에 넣는다. Execution cap에 도달해서 task가 종료되는 경우 Client가 사후처리를 할 수 있도록 이 사실을 Client에게 반드시 알려야 한다. 

Machine Learning 의 학습같이 긴 시간의 실행시간이 필요한 task의 경우 자주 Pause and Resume 해야 할 수 있다. 2초면 끝날 task들이 특정 task 때문에 이틀 이상 기다려야 하는 것은 불합리하기 때문이다. (pause 했을때 다른 short time tasks를 실행)

## Prioritization

Task에 우선순위를 부여하기 위해 task scheduler는 각 task에 대한 delay tolerance 정보를 관리한다. Delay tolerance는 task의 실행을 지연할 수 있는 최대시간을 의미한다. 만약 어떤 task가 가장 짧은 delay tolerance를 가지고 있다면 그 task는 가장 먼저 실행되어야 함을 의미한다. 

Peak time에 urgent tasks를 위한 여유를 확보하기 위해 좀 더 긴 delay tolerance를 지정하는 식으로 운영하는 것도 가능하다.

## Resource capacity optimization

Resource의 사용량이 특정 threshold를 넘어가면 (e.g. 80% utilization) 이 상황을 Peak time으로 간주할 수 있다. Peak time에서의 부하를 줄이기 위해 urgent execution이 필요하지 않은 task의 경우(e.g. 친구추천) off-peak time에만 수행하도록 별도의 queue를 만들 수 있다.

## Task idempotency

Task를 성공적으로 실행했으나, 어떤 문제로 asknowledgement를 전달하지 못했을 때 scheduler는 task를 다시 스케쥴링 하게된다. 그로인해 아래 그림에서 처럼 반복적인 task의 실행에 의해 양측이 기대한 것과 다른 결과를 갖게될 수 있다.

(A는 B에게 10달러를 송금했으나 B는 결과적으로 20달러를 송금받게 된다.)

<img width="579" alt="스크린샷 2023-01-29 오후 8 42 40" src="https://user-images.githubusercontent.com/14961526/215323741-ca695958-87c9-4742-9094-caa1ec6bf652.png">

이런류의 task는 idempotent(여러번 실행해도 결과에는 영향을 끼치지 않는)한 성격을 요구한다.

<img width="577" alt="스크린샷 2023-01-29 오후 8 47 50" src="https://user-images.githubusercontent.com/14961526/215324017-2440c974-268b-4b0b-bff0-1393f0bd5249.png">

앞선 sequence diagram에서와 달리 idempotency key의 매칭을 통해 여러번의 task 실행에도 기대했던 결과를 도출할 수 있다.

(Database에 video를 올리는 것이 idempotency의 예가 될 수 있다.)

## Schedule and execute untrusted tasks

Untrusted task란 task script가 malicious instructions를 포함할 가능성이 있는 task를 의미한다. 한 task의 수행이 다른 task의 수행에 나쁜 영향을 끼치지 않도록 해야한다. (e.g. shared environment에 대한 malicious instruction을 가지고 있는 task)

다음을 염두하자.

- 적절한 인증과 자원에 대한 인가 절차 적용

- Docker나 Virtual Machine를 사용해서 Code Sandboxing

- 각 Task의 Resource Utilization Monitoring을 통해 Task 간의 Performance Isolation

## Evaluation

### Availability

- rate limiter가 적절하게 replicated 되는지

- node가 task의 실패를 알렸을때 다른 node가 task의 수행을 대신할 수 있는지

- queue가 task를 수용가능한 상태인지

### Durability

- Task를 제출하고 수행되기까지 Database에서 유지되는지

### Scalability

- 각 component와 resource를 확장/축소할 수 있는지

### Fault Tolerance

- Task 실행에 실패했을때 재실행 할 수 있는지

- task가 infinite loop에 빠졌을때 특정 시간 이후 task를 종료하고 유저에게 알릴 수 있는지

### Bounded waiting time

- 유저의 waiting time에 상한이 있는지

- waiting time에 도달했는데도 task의 실행이 불가할때 유저에게 그 사실을 알릴 수 있는지

## Conclusion

Datacenter level의 task scheduling system에 대한 설계를 살펴봤다. 
