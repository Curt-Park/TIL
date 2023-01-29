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
