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


