> 03.18.2017

###init/main.c 

main.c -> start_kernel -> linux/kernel/params.c : parse_args

line: 272

dts/~~ 에 chosen 노드를 파싱해서 args 로 사용함  

parse_args 에서 사용   

early_param 을 사용하면 struct 를 차례대로 돌면서 init 된 디바이스를 볼 수 있음  

early_mem ->  사용자가 mem 인잇해주면 그걸로 사용하고 원래 했던거 리셋함  
* 리눅스 소스에서 (at) 이  무슨뜻인지 확인해보기

http://jake.dothome.co.kr/ 공부하기
ARMv7-A의 페이징은 크게 Short-descriptor translation과 Long-descriptor translation 두 종류로 나뉩니다. Long-descriptor translation은 큰 물리 메모리를 지원하는 LPAE(Large Physical Address Extension) 기능

efi_init()

> 03.24.2017

* arm_memblock_init(mdesc) -> kernel text 랑 kernel data 랑 initrd 를 메모리에 init 하는 함수

* memblock_is_region_memory -> 메모리 블록에 arg로 들어오는 base + size 가 mem block 안에 존재하는지 확인하는 함수

* memblock_is_region_reserved -> base+size 가 예약된 영역에 침범하는지 확인하는 함수

* memblock_add_range -> 새로운 memblock region 을 예약하는 함수

> 03.25.2017

* sanity 체크는 결국 high memory 초기화 current limit 초기화

* 메모리 어떻게 움직이는지 확인 

* arm 메모리 시스템에 대한 것들을 쫌 확인해봐야할 듯 

* phys memory 랑 virtual memory arm 에서 어떻게 되는지 확인해봐야함

* memblock struct 확인해보면 current_limit 이 phys address 임 확인해보자

* CONFIG_BLK_DEV_INITRD initial ram filesystem and ram disk ( initramfs , initrd ) support

* xip 일때는 text 영역이 필요가 없으니까 제외 "arch/arm/mm/init.c" 790L, 19661C

* fdt -> flattened device tree -> device tree 중에 하나이다.

* arch/arm/mm/init.c -> 맨처음에 declare 부분 보면 __init 이란게 있다. __init 에 들어가는 것은 booting 이후에 지우고 싶은 데이터들을 집어넣는 과정을 define 해논 것

* initrd , initramfs 의 차이점 -> initramfs : cpio로 만들어진 ramdisk , initrd 는 /dev/ram + ext2 or ext3 ohter filesystem 으로 만들어진 ramdisk 라 /dev/ram으로 접근해야함

* CONFIG_BLK_DEV_RAM -> ramdisk support

![Alt Text](./imgs/01.png)

* return 이 매우 인상적임

* swapper_pg_dir -> 커널이 쓰는 pg 테이블 을 초창기에 init 해주는 변수

* trustzone 왜 register 하고 써야함? 모든데?

* reserved-memory 의 address-cells 랑 size-cells 는 단위를 얘기하는듯?

* ENOENT -> no such file or directory

![Alt Text](./imgs/02.png)

* okay 거나 ok 이면 을 이렇게 표현함 멋있따...

* reserved memory 에 대한 것 한번 공부해와서 공유해보쟈

> 03.27.2017

* 리눅스는 virtual memory 를 4G를 사용함

* virtual memory 와 physical memory 사이의 변환 시기 및 단계에 대해서 더 잘 알아야할 듯


