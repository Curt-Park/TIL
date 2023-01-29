# System Design: Distributed Task Scheduler

## What is a task scheduler?
Task란 특정 시간대에 특정 자원(CPU time, mememory, storage, network bandwidth, and so on)을 요구하는 계산작업의 한 단위다.
예를 들어, Facebook이나 Instagram에서 이미지 또는 비디오를 업로드할때 다음과 같은 background task가 수행된다.

1. 이미지 또는 비디오를 여러 해상도로 인코딩
2. 이미지 또는 비디오의 컨텐츠 수익화(content monetization)를 점검하기 위한 저작권 등의 검사

이미지나 비디오를 업로드하는 사람은 굳이 위 동작이 완료될 때까지 대기할 필요가 없으므로 위 작업은 task scheduler에 의해 비동기로 수행된다.
Task scheduler는 시스템 상의 제한된 계산 자원 위에서 다수의 task가 task level / system level의 목표를 만족할 수 있도록 똑똑하게 자원을 할당하는 역할을 한다.

## Distributed task scheduling

