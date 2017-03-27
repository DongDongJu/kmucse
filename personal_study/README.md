> 03.20.2017

### Challenges and Opportunities in Many-Core Computing

매니 코어 시스템에서의 전통적인 문제점들을 보여주는 논문

![Alt text](./imgs/01.png)


* 클럭 디지털 디바이스의 전력은 클럭 frequency에 비례한다. 

* 클럭 속도엔 자연스런 한계가 있다.

* 클럭 자체의 속도를 높이기위해선 파이프가 얇아져야만 하고 이를 위한 cooling 시스템 없이는 불가능하다.
  더군다나 클럭속도에 비해 메모리 성능 향상또한 프로세서 성능 향상에 비해 뒤떨어져있음. ( Power Wall )

* 메모리 시스템의 진화속도가 프로세서에 따라오지 못해 고전적으로는 캐쉬 크기를 증가시키는 것으로만 해결하려고 했음. ( memory Wall )

* 하드웨어 엔지니어들은 주파수 스케일링으로 인한 성능 향상 외에도 execution을 예상하는 시스템을 만듬으로써 성능을 향상 시켰음.

* 하드웨어적 안전 장치가 존재함으로써 순서가 잘못된 실행으로 부터 오는 오류를 예방하려고 했음.

* branch를 추측해서 동시에 실행할 명령어를 결정해야함. 이것을 instruction-level parallelism (ILP) 라고함

* 데이터 종속성으로 인해 분기가 없음에도 연속 명령어가 병렬로 실행되지 않을 수 있음. ( ILP Wall )

* Berkeley 의 Patterson 이 이론적인 serial performance 문제를 제기했음

***

 The power wall + The memory wall + The ILP wall -> a brick wall for serial performance

 위의 그림처럼 아키텍쳐마다 문제가 일어나는게 달라지기 때문에 각각을 정의할 수 는 없지만, 크게 봤을때 위 세가지를 합쳐 문제점이라고 볼 수 있다.

***


![Alt text](./imgs/02.png)


* fig.2(a) 를 봤을때 왜 큰 OoC 대신에 IoC 여러개를 쓰냐면 OoC는 일반적으로 ILP 의 limit에 걸려서 바보같은 성능을 보여줌. 그렇기 때문에 IoC 여러개를 사용하는 시스템을 선호. 임베디드 칩은 C 처럼 바뀌면 좋을것이다.(확인해보장)

* 여기까지 하드웨어 얘기


***


* 소프트웨어적 관점에서 몇가지 흥미로운 approach 들을 제시함

* 재사용 가능한 components 들로 도메인별 knowledge를 캡슐화 하는것

* concurrency 와 coordination을 위해 전통적인 언어들 ( C, fortran ... ) 로 쉽게 사용할 수 있도록 포팅하는 것

* 의미적인 수준을 올리면 명시적 sequencing이 제거된다? 가 무슨소리인지 잘 모르겠음

* 아.. 함수형 프로그래밍이 매니코어에 어울린다는 얘기인가?

* OS 쪽 얘기로 넘어감

* 현재 대부분의 OS는 uniform device model 을 씀 그렇기 때문에 security problem 과 optimize 시에 어려움이 있음.

* TSOS ( Time Sharing Operating System ) 에 대한 얘기가 나옴, 이게 70년대에 VMOS ( Virtual Memory Operating System) 으로 진화했다고함.

* TSOS 의 security 는 single authority 아래에 있음, 오늘날의 컴퓨터 트랜드에 맞지않음.

 

![Alt text](./imgs/03.png)


* OS와 hypervisor 상에서도 매니코어 시스템 지원을 잘 해야지 퍼포먼스를 올릴 수 있다는 요약인듯

Programmable systems are playing an increasingly large
part in our lives and, in many ways, provide a worldwide
paradigm shift comparable in scope and benefit to the
appearance of cheap, mass market printing. Many-core
computers signal a shift in computer science, computa-
tional science, and classical commercial software that
marry the past advances of many knowledge workers as
well as provide avenues for qualitatively new advances.

* 결론 : 매니코어 짱이라 삶이 윤택해질듯 근데 이런 어려운 문제들이 존재하니까 후대에서 풀어죠

### 매니코어 시스템을 위한 리눅스 가상 메모리 관리의 락 경합 분석

* 주현이형 2015 논문

* 결론 : 매니코어 시스템위에서 리눅스를 사용할 때 일어나는 메모리 관련 성능저하에 대한 벤치마킹 결과


### 매니코어 환경에서 로그 기반 동시적 업데이트 기법을 활용한 리눅스 커널 확장성 개선

* 2016 논문

* 높은 업데이트 비율로 인한 serialization 관련 문제에 대한 해결 방법은 non-blocking 알고리즘을 사용하는 방법과 로그기반을 사용하는 방법이 있다.

* 로그기반의 장점

1. 로그를 저장하는 순간에는 락이 필요없다.
2. 저장된 업데이트를 순차적으로 락과 함께 하나의 코어에서 수행해서 캐시 hit 비율이 올라간다.
3. 큰 수정 없이 기존 여러 데이터 구조에 쉽게 적용할 수 있다.
4. 저장된 로그를 실제 수행하지 않고 여러 가지 최적화 방법을 사용하여 적은 명령어로 업데이트를 수행할 수 있다.(?)

여기에 업데이트 순간 삭제 가능한 로그를 지움으로써 성능을 향상시키는 방법을 사용

* LTP ( Linux Test Project ) 통과함

* Anonymous reverse mapping , file reverse mapping 


> 03.21.2017

### Scalable Address Spaces Using RCU Balanced Trees

* working set 현재 프로세스 전용으로 할당된 물리적 메모리 페이지 그룹

* page fault -> hard fault + soft fault

* soft page fault -> working set 이 아닌 물리적 메모리상에 요청하는 페이지가 있기 때문에 메모리를 엑세스 하면 해결이 되는 fault

* hard page fault -> 요청하는 페이지가 메모리상에 없기 떄문에 디스크에 요청하는 것 

* concurrency -> 프로그램을 I/O를 수행하는 여러 개의 쓰레드로 구현하는 것을 의미함. 

* RCU (Read-Copy-Update) -> 읽기 동작에서 blocking 되지 않는 read/write 동기화 매커니즘

* write 가 10% 이상인 경우에는 다른 것을 선택하는 것이 좋음 [RCU-MC]( http://jake.dothome.co.kr/rcu/ )

* RCU 베이스의 binary-balanced tree for storing memory mappings 을 제시함

* 2.6.37 linux kernel 과 80코어 환경에서 실험해서 그 결과를 증거로 제시

* 이 논문은 x86-64 four-level page table 기준으로함, 그러나 아이디어는 x86 에 국한되지 않음


![Alt text](./imgs/04.png)


* 대부분의 시스템은 프로세스당 한개의 read/write 락을 사용하고 있음.

* 위 사진에서 하나의 프로세스에 한개의 락이 있을때 어떻게 page fault 가 진행되는지 과정을 볼 수 있음.

* bonsai tree 를 이용해서 해결했음

* RCU 를 모든 주소공간 스페이스에 적용하기에는 방법이 존재하지 않음.

* MOSBENCH, Dedup from Parsec 

* Serialization 이란 객체를 memory 에서 sequence of bits 로 바꾸는 것, serialization 된 후에 네트워크에서 이동하고, 프로그램간 정보로 교류가 되기도함. 다른 말로 marshalling 이라고 하기도 합니다.

* red-black tree -> 트리에 n 개의 원소가 있을 때 O(log n ) 으로 삽입, 삭제 , 검색이 가능 

* 윈도우 7 은 PFN lock 을 사용함

* bonsai 트리는  insert 와 delete에 대해서 read lock 을 없앤것

* single write lock 은 여전히 사용함

 
![Alt text](./imgs/05.png)


* single rotation 이 일어났을때 Z 를 못	보고 X,Y 까지 내려가는 경우가 생김, bonsai tree 는 이것을 해결함

* cache coherence -> 캐시 일관성 공유메모리를 가질때 각 프로세스별 일관성을 지켜야함

***

* A는 사기꾼 연금술사라 무슨 일이 있어도 금괴를 다른 사람이 구별할 수 없도록 만들어야 하고, B는 금괴 감정사라 가짜를 반드시 구별해야 하는 상황이다. 그런데, A와 B가 어느날 만나서 서로 금괴를 만들고 이를 구분해내는 것으로 내기를 하기로 했다. A는 최선을 다해 가짜 금괴를 만들어서 B에게 주면, B는 이걸 진짜와 구분한 뒤에 자신의 비법을 어딘가에 정리를 한다. A는 B의 비법을 어떤 방식으로든 (여기서 다양한 방법이 등장함, 이들의 지식이 연결고리를 가지기도 하고 각자 따로 경쟁하기도 하고) 반영해서 새로 금괴를 만들어서 다시 B에게 주면 B는 또 다시 열심히 연구해서 구별하는 방법을 정리한다. 이게 계속 반복되면 A는 정말 금괴를 잘 만들 수 있게 되고, B는 날이 갈수록 정교해지는 A의 금괴를 구별하기 위해 자신의 구분 실력이 더 늘어남을 알게 된다. 시간이 흘러 B가 자신의 금괴를 거의 구별하지 못하는 것을 알게 되자, A는 금괴를 만들어서 팔고 다니는데, 이것을 가짜라는 것을 알아차리는 사람들이 거의 없다. 여기서 A나 B나 같은 종류의 지식(=네트워크)를 가지고 구분을 하거나, 만들어내는데 이것이 GAN 네트워크의 특징이다.

저 비유 상황에서라면, GAN의 목적이 "최고의 연금술사 만들기"라는 점을 짚고 들어가시면 좋을 것 같습니다. 간단히 GAN의 과정을 다음과 같이 요약한다면 --- 진짜 금괴 몇개를 먼저 연금술사에게 보여주고, 비슷한거 만들어보라고 시켜놓고, 금괴감별사를 초빙해서 만들어낸것과 오리지날 금괴를 비교하게 해서 피드백을 연금술사에게 준다. 무한반복 --- 고된 훈련을 통해 연금술사는 점점 감별사가 구별하기 힘든 것을 양산하게 되겠지요. 결국 저 셋팅을 마련한 사람의 목적은, 초짜 연금술사가 마침내 처음 시작한 오리지날 금괴같은것(구별불가능한 것)을 양산하는 마스터 연금술사가 되길 기대한다는 점이라고 생각합니다

***


> 03.22.2017


### 이어서

* 만약 rock-free reader 가 업데이트 전에 tree 에 접근하려고 하면 old-tree 를 접근하게 된다.

* bounded-balance tree 에서 착안을 받아서 만들었으며 weight 를 파라미터로 사용하기 때문에, 이때문에 기존 strictly balance tree 보다 rotation 이 적어짐

![Alt text](./imgs/06.png)

* C로 함수형 프로그래밍 하듯이 짯음

* 모든 트리의 노드는 위의 4가지 필드를 가짐

* insert 가 일어나면 insert 가 끝나기 전까진 reader 는 old 값들만을 읽게됨

* tree 를 reconstruct 할 때에 mkBalanced 라는 함수를 사용함

* balancing 이 끝난 트리는 지우지만, 만약 그 동안에 lookup 중이라면 모두 끝난 후에 invaild 시킴

![Alt text](./imgs/07.png)

* 위의 (b) 를 봤을 때 mKbalanced 의 non-destructive rotate 를 볼 수 있음.

* VMA ( Virtual Memory Areas ) 란 workset 들이 존재하는 공간을 얘기하는듯? 확인필요함

* 리눅스는 process 단위로 read / write lock 을 적용함

> 03.23.2017

* mmap_sem -> read/write per process , protects address space

* Page dir. lock -> spinlock per process , protects Page dir, entries

* PTE lock -> spinlock per page table , protects Page table entries

* spinlock -> 진입이 불가능할 때 진입이 가능할 때 까지 루프를 돌면서 재시도하는 방식으로 구현된 락, 락을 획득할때까지 해당 스레드가 빙빙 돌고있다 (spinning)는 것을 의미함.

* 리눅스는 이중 잠금을 사용해서 락의 frequence 와 duration 을 줄이려고 했음.

* 그 예로 리눅스의 page fault handler 는 존재하지 않는 페이지 디렉토리 entries 를 관찰 한 후에만 페이지 디렉토리 lock 을 획득하고, 심지어 새 페이지 테이블에 대한 메모리를 많이 할당한 후에만 lock 을 획득함. 이 동시에 page fault 가 그 동안 페이지 디렉토리 entry를 채우면, 할당된 페이지 테이블을 단순히 버린다. -> double-check lock 때문

* 어떤 일이 있더라도 page fault 가 일어났을때 다른 thread 가 해당 주소에 접근이 불가능하기 때문에 매우 큰 문제임. heavy fault 일때는 더 심함.

* fault locking -> 메모리 write mode 에서 mmap sem 의 read / write lock 을 보유하는 시간을 줄여 soft page fault가 read-only part 와 동시에 실행 가능하게 하는 것

* hybrid locking/RCU -> hardware page table 구조와 각각의 VMA entries 에 RCU 를 적용해서 soft page fault 의 필요성을 없앴음.

* 이제 설명

* fault locking 을 위해서 fault lock 을 each memory space에 추가했고 page fault handler 가 read mode 에서 이 lock 을 acquire 하게 만들었음.

* write mode 일때는 똑같음 그러나 만약 write mode 일때 page fault handler 와 conflict 가 일어나게 된다면  fault lock 을 요구하게 된다.

* fault lock 은 mmap_sem 이 released 되었을 때만 released 된다.
 
* Hybrid locking/RCU 설명

* 얘네의 목적은 page fault handler 를 memory mapping operation과 다른 page fault 까지 모두 동시에 일어나도록 하는것임

* 얘네의 방법은 read lock 을 없앤것 (RCU 를 이용함)

* 제안하는 방법은 어떤 address space 에 관한 structural change를 가하지 않음.

> 03.27.2017

* VMA split race 설명

* page fault 는 segfault 일 수 있고, fault 주소를 포함하도록 확장되어야 하는 stack 영역에 있거나 VMA 분할 중간에 있을 수 있습니다.

* mmap_sem 이 저 problem 들을 control 할 수 있게 acquire 해놈

![Alt Text](./imgs/08.png)

* 위 그림에서 보는 것 처럼 분할 중에 메모리 영역이 매핑되지 않은 상태로 일시적으로 나타날 수 있기 때문에 발생함

* munmap operation은 VMA를 2개의 VMA 로 나눌때 아래의 2스탭을 실행한다.

* 그림을 보면 어떤 문제인지 이해 가능

* Page table deallocation race 설명

* page directories 와 tables 은 vma 가 fault 났을때 mapping 을 새로하는 도중에 empty page directory entry 를 만났을 때만 새로 allocate 된다.

![Alt Text](./imgs/09.png)

* 위 과정에서 2가지 문제가 있음

* 첫번쨰는 classic RCU : unmap 이 concurrent fault 때문에 사용중인 VMA, table , directories 를 비울 수 있는데, 이걸 해결하기 위해서 RCU delay 를 이용했음

* Page table fill race 

* stock linux 나 hybrid locking/RCU 에서는 fault 와 mapping free 사이의 경쟁을 해결하지 못한다.

* 만약 같은 VMA 에 대해서 page fault 와 munmap 이 같이 일어났다고 가정해보자.

* munmap 이 이미 faulting address 를 넘어갔을때 page table 은 faulting 난 address 를 free 하지 못하고 기다려야한다.

* 그리고 그 이후에 그 entry 자체를 clear 해버린다.

* 그렇게 되면 concurrent page fault 는 blank page directory 를 바라보고 있게되고 얘네는 새로운 page가 allocate 되야겠구나라고 생각한 후 완전 새로운 page를 가져오게 된다.

* 이건 간단하게 detect 할 수 있다.

* PTE lock 을 적용 하면 page table entry 가 채워지는걸 protect 하게 된다. 그러나 그걸 진짜로 채우기 전에는 page fault handler 는 doulbe-check 하게 된다 faulting 상태인지 아닌지

* Pure RCU

* 보통 OS는 virtual memory areas 를 tree에 보관함

* 그러나 일반적으로 사용하는 Red-black tree 나 AVL 은 RCU safe 하지 못하다.

* 이유는 만약 lock-less lookup 도중에 insert 와 delete가 같이 들어올경우 lookup failing 이 일어나게 된다.

* BONSAI tree는 이거를 해결함 

![Alt Text](./imgs/10.png)

* 이제 뭘 구현했는지 알려줌

* current implementation 은 regular soft page fault in anonymous memory mapping 을 handle 함

* 5가지로 증명함

1. Can application scalability be limited by boottlenecks in the implementation of address spaces? 

2. Do the techniques proposed in this paper eliminate those bottle-necks?

3. Is a simple fine-grained locking approach sufficient to remove the bottlenecks or is RCU necessary?

4. Are short-duration read-locks acceptable in the soft page fault handler, or is the complete application of RCU necessary for scalability?

5. Are application workarounds still necessary to achieve peak scalability?

* 다시 읽어보장
