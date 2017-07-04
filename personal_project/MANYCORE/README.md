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

문제가 있다.

1. 만약 로컬 lock contention 자체가 길어질 경우에 server core 가 starving
2. 만약 로컬 lock contention 이 지나치게 짧을 경우에 스위칭이 너무 자주 일어나서 이것도 좋지 않음

결론적으로 threshold 를 적절하게 잘 찾는게 중요함 -> 기계학습을 이용해보면 어떨까?

각 노드마다 node-cas-lock 이라는걸 쓰고있음

[PAPI](http://icl.utk.edu/papi/) 라는 라이브러리를 써서 구현했음 (리얼 타임 하드웨어 데이터를 좀 더 쉽게 볼 수 있는 라이브러리, 비교적 최신에 구현된 거라 좋을듯?)

POSIX 사용


~~~


~~~
# 04.07.2017

SANL 소스 구해서 빌드시켜봄

PAPI 랑 mpich 먼저 설치해야함

~~~

~~~
# 05.07.2017

PAPI 랑 MPICH 설치완료

권한때매 애좀먹었당.

benchmark set 빌드

1. liblock ( 완료 )

2. microbenchmark ( 완료 )

3. Phoenix 2 ( 코어 에러 )

4. memcached ( libmemcached-1.0.2/clients/memslap.cc 내컴에 맞게 )

5. Berkeley DB ( 에러뜸 )

일단 microbenchmark 만으로 실제 성능측정 확인해봐야할듯

성능 향상이 눈으로 확인되면 커널에 포팅작업 고고
			   
~~~
### 해야 할일

* KNL NUMA 구조고민


