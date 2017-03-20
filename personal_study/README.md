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


