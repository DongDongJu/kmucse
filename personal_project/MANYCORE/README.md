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

~~~
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
			   

benchmark set run

microbenchmark
1. posix ( O )
2. spinlock ( O )
4. mcsm ( 에러 )
5. mcs ( O )
6. flat combining ( O )
7. rclb ( O )
8. rcl ( O )
9. mwait ( 에러 )
~~~

~~~
# 06.07.2017

딴일을 좀 했당.
~~~

~~~
# 07.07.2017

성능확인차 벤치마크 돌리는중

~~~

## 10.07.2017 , 12.07.2018

# 오늘부터 memory 커널 소스 확인해볼려고함

~~~
mm/memory.c

line 95 ~ 101 : 모든 x86 시스템은 direct map memory 위쪽에 high memory 가 존재한다고 가정하는 ioremap 을 가지고있다.
max low pfn 이랑 highstart pfn 이 같을 수 밖에 없다. normal 이랑 highmem 의 차이는 없다.
ioremap , iounmap -> 물리 메모리 주소를 가상 메모리 주소로 바꿔주는것 , 그반대

line 105 ~ 110 : 랜덤한 주소 ( 스택, mmap , brk , 등등 )

line 130 ~ 132 : CONFIG_MMU architecure 가 ZERO_PAGE 를 자기 paging_init() 에 셋팅한다.


init/main.c

set_task_stack_end_magic() -> .data 랑 .init_task 섹션으로 결정되는 init_task 를 가지고 overflow detection 을 위해서 메모리의 끝을 정해놈( STACK_END_MAGIC )
smp_setup_processor_id() -> smp 를 위한 processor id 셋팅
debug_objects_early_init() -> initial 에 필요한 object 들을 부팅 전에 셋팅해주는것 이 작업 이후에는 오브젝트 tracker 가 정상작동함

boot_init_stack_canary() -> 스택 overflow 를 막기위한 방어책 정도로 생각하면 될듯
cgroup_init_early() -> cgroup 을 초기화하고 subsystem ( early_init ) 도 초기화하고

local_irq_disable() -> 현재 cpu irq 를 disable
early_boot_irqs_disabled -> early_boot 의 irq 도 disable

주석 : 인터럽트가 지금은 꺼져있지만 부팅시에 필요하다면 켜도됨

boot_cpu_init() -> cpu 의 현재 상태 설정 ( online , active , present , possible ) 
page_address_init() -> 메모리 변환을 위한 hash table 초기화 ( lock 도 같이 )
setup_arch(&command_line) -> 너무 길어서 나눠서 가겠음 x86_64 기준

memblock_reserve() , early_reserve_initrd() -> ramdisk 데이터를 읽어와서 init 함

trap_init() , cpu_init() , ioremap_init() -> trap,cpu,ioremap 을 init

olpc 관련된 코드가 이쪽에 있음

root_dev, screen , edid(확장 디스플레이), video 모드 , bootloader 타입 ,version, 등을 여기서 결정해줌

arch_setup -> platform 별 셋업이 이 함수 포인터로 이루어짐

e820 셋팅이 여기서 이루어짐

e820 이란 arm 이나 특정 하드웨어들은 각각 specified 된 설정을 사용하지만 pc(x86) 에서는 AX 에 e820 이라는 값을 확인하므로써 메모리 맵을 설정함.

parse_setup_data -> data_type ( EFI,DTB,E820 ) 에 따른 셋팅을 해줌

edd -> for old bios

주석 : parse_early_param 전에 하드웨어가 NX 를 서포트 하는지 안하는지 검사함

parse_early_param -> boot param 읽어옴

hotplug 관련 셋팅도 이루어짐

apic (advenced programmable interupt controller ) 셋팅도 여기

pci 설정

dmi 관련 설정 ( bus 인터페이스 )
--

mm_init_cpumask() -> 씨퓨 클리어

setup_command_line -> 나중을 위해서 만들어놈

setup_per_cpu_areas() -> cpu별 공간 allocate numa 관련 설정도 여기있음

64 비트는 atom_size 로 PMD_SIZE 를 32는 PAGE_SIZE 를 씀

smp_prepare_boot_cpu -> cpu 상태를 online 으로 만들어줌

build_all_zonelists -> system booting 상태에서만 부를수있고, 노드별로 메모리 셋팅 ( 그래서 바이오스에서 밖에 접근이 안되는 거였음 )

page_alloc_init -> cpu 상태 확인해서 init 함

parse_early_param -> early param들을 파싱해서 처리해줌

parse_args -> ~~~

jump_label_init -> jump_label 을 소팅해서 설정해줌

setup_log_buf -> 로그를 사용하기 위해서 buf 를 0 으로 셋팅해줌

pidhash_init -> pid 를 사용하기위한 hash 셋팅

vfs_caches_init_early -> vfs , dcache , inode 초기화하고

sort_main_extable -> 커널에 빌트인 된 exception 테이블을 소팅 

trap_init -> 일일히 exception 셋팅 해주고 , idt 테이블도 셋팅


# EISA -> 버스의 일종


mm_init -> page_ext_init_flatmem : 노드별로 버디 알고리즘을 이용 페이지의 range 가 넘치지 않는지 확인해줌 -> mem_init : pci를 위한 io mmu alloc , NUMA 상태일경우 상태를 가져옴


# ASLR (Address Space Layour Randomization) -> 힙이랑 스택의 영역을 계속 바꿔주는 메모리 보호기법
# DEP (Data Excution prventation) -> 데이터 영역에서 코드가 실행되는 걸 막는 기법
# ASCII-armor -> 공유라이브러리 상위주소에 00을 포함시키는 기법 
# canary -> 프로그램 내에 작은 값을 삽입시켜서 원본과 계속해서 비교 이상이 있을시에 변조당했다고 생각하기 위한 기법


~~~


### 해야 할일

* 코어별, 캐시별 피닝

