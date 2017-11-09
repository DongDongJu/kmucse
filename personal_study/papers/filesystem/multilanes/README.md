### MultiLanes: Providing Virtualized Storage for OS-level Virtualization on ManyCores


'''
Abstract :

매니코어 에서 OS 레벨의 virtualization ( 커널을 공유한다고 말하고 있으니 container 가 주가 될듯 ) 은 shared I/O stack 이 performance 에 심각한 문제를 초래할 수 있음.
이 페이퍼는 Multilanes 를 내세웠는데, virtualized storage system 이다. isolated I/O stack 을 만들어서 kernel data structures 와 locks 에  의한 contention을 줄였다. 자기들 플랫폼의 오버헤드는 리눅스에 비해서 무시할만 하다. 확장성을 떠나서 유연성과 보안까지 챙길수 있다. prototype system 은 LXC를 위해 만들어졌고 ramdisk 를 사용한다. 12배정도 퍼포먼스를 보여줬다 microbenchmark 를 통해서.

'''

* 흠 더 읽어봐야 알겠지만 ramdisk 를 사용한점이 걸린다.
* negligible : 무시할 수 있는

'''
Intoduction :

hypervisor보다 os level virtualization이 낫다 ( VServer,OpenVZ,Zap,LXC ). 이를위해서 CPU,memory,disk 등을 어떻게 하면 효과적으로 나눌까 연구가 많았다. 그런데 non-volatile memory tech가 발달하면서 문제가 생겼다. storage system 의 bottleneck 이 나타나기 시작한 것이다. 특히 I/O 스택이 퍼포먼스 하락에 심각한 영향을 주었다. 확장성에 문제를 주는 지점은 VFS에 약간과 파일시스템에 깔려있다. multiple Ves 와 I/O intensive 한 workload 들을 돌릴경우 문제가 심각해진다. hardware 의 성능과는 별개로 software 적인 한계에 부딪히고 만다.

multilane 은 shared kernel data structures 랑 locks 의 문제를 isolated 시킴으로써 완화시켰다. 또한 확장성 또한 가지게 되었다. 

multilane 은 file-based virtualized block device for each ve 를 만든다. ( docker 에 적용된 volume 개념이랑 똑같은듯) 

![Alt text](../../imgs/33.png)




'''
