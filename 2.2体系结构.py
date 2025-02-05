计算机体系结构分类

1、Flynn分类法
simple 单个 mountain 多个 

SISD:单指令流单数据流
控制部分：1
处理器：1
主存模块：1
代表：单处理系统

SIMD:单指令流多数据流
控制部分：1
处理器：多个
主存模块：多个
代表：并行处理机

MISD：多指令流单数据流
这种是不可能的，不实际
控制部分：多个
处理器：1
主存模块：多个

MIMD:多指令流多数据流
控制部分：多个
处理器：多个
主存模块：多个
代表：多处理机系统、多计算机

2、计算机指令
一条指令=操作码+操作数

指令执行过程：

3、指令寻址方式
顺序寻址方式
跳跃寻址方式：

4、指令操作数的寻址方式
立即寻址方式：
直接寻址方式
间接寻址方式：

5、指令系统
CISC:复杂指令系统，兼容性强，数量多。
指令长度不固定，寻址方式支持多种，微程序控制技术，
研制周期长

RISC:精简指令系统，数量少，使用频率接近，定长格式，大部分为单周期指令，
操作寄存器，只有load/store操作内存
支持方式少，
实现方式：大量通用寄存器，硬布线逻辑控制为主，适合采用流水线
优化编译，有效支持高级语言


6、指令流水线

取指-分析-执行

流水线周期：执行时间最长的为流水线周期
流水线执行时间:1条流水线的总执行时间+（总指令条数-1）*流水线周期
流水线吞吐率：总指令条数/流水线执行时间（单位时间内指令执行的条数）
流水线加速比：不使用流水线总执行时间/使用流水线总执行时间

超标量流水线技术：常规流水线是1度，假设度为3，相当于3条流水线并行执行
三个阶段都同时处理3条指令，所以计算的时候
指令条数=指令条数/度

真题：流水线有5段，有1段的时间为2ns，另外4段的每段时间为1ns，利用此流水线
完成100个任务的吞吐率约为（）个/s

吞吐率=总指令条数/流水线执行时间
流水线执行时间=1条流水线的总执行时间（2+4）
             +（总指令条数-1）100-1
             *流水线周期（执行时间最长的2ns）
吞吐率=100/（2+4）+（100-1）*2=100/204ns
由于题目是算s，所以204ns转成204*10^-9s
吞吐率=（100/204）*10^9=490*10^6

真题：流水线加法运算器分为5段，所需要的时间：6ns、7、8、9、6
最大加速比为多少
思路：流水线加速比：不使用流水线总执行时间/使用流水线总执行时间
6+7+8+9+6=36  执行一条指令，执行n条，36n
36+（n-1)*9=36+9n-9=9n+27
36n/9n+27   由于是最大加速比，n趋于无穷大，27忽略不计，结果是4


7、存储系统
cpu内部通用寄存器、cache、主存储器、联机磁盘存储器、脱机光盘
从左到右，内存越来越大，速度越来越慢，也越便宜

所以采用分级存储，解决成本
两级存储：cache-主存、主存-辅存(虚拟存储体系)

局部性原理：
1、时间局部性：相邻的时间里会访问同一个数据项
2、空间局部性：相邻的空间地址会被连续访问

8、高速缓存cache
  