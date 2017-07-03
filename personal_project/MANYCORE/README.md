### 실험환경
~~~

 물리 코어수 : 64
 가상 cpu수 : 256
 물리 cpu수 : 1
 NUMA 노드 수 : 2

 OS : CentOS Linux release 7.3.1611 (Core)
 Kernel : 3.10.0-327.13.1.el7.xppsl\_1.4.0.3211.x86\_64
 NUMA policy : default

~~~

* 현재 0번에 모든 cpu 가 몰아져 있음

### 진행상황

~~~
# 28.06.2017
numactl version 보여주는거 커밋, 시스템 환경 확인
~~~

~~~
# 29.06.2017
numa 구조를 가지는 시스템의 shared 메모리 관리 방법

ccNUMA( cache-coherent NUMA ) 라고 얘기한다.

[Scalable Adaptive NUMA-Aware Lock](../../personal_study/papers/SANAL.pdf)
~~~

~~
# 30.06.2017

위에 논문 보다가 QD 라는걸 봐서 일단 QD 적용했을때랑 안했을때의 성능 차이를 확인해보려함

빌드가 안되네ㅋㅋㅋ

KNL 메모리 타입이랑 뭔가 문제가있는듯.
~~~

~~~
# 03.07.2017

어쨋든 critical section 이 작으면 in place 락이 더 효율이 좋음

그렇다면 critical section이 많은 프로그램이 주인가 적은 프로그램이 주인가



~~

### 해야 할일

* KNL NUMA 구조고민

* software transactional memory 에 대해서 쫌 알아보쟝
