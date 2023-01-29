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
