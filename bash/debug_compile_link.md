## gdb 使用
https://www.cnblogs.com/secondtonone1/p/5732938.html
https://www.cnblogs.com/wuyuegb2312/archive/2013/03/29/2987025.html
1 ulimit -c unlimited
2 重新编译，增加-g选项(增加行号)
2 gdb your_exe_file
3 core-file core.file
4 bt // 查看调用链


## ar 创建修改库
nm 列出目标文件的符号清单
ldd 查看文件链接库
https://blog.csdn.net/u010977122/article/details/52993560 
```
pkg-config 是用来g++ 编译链接时的简易写法，PKG_CONFIG_PATH

#搜索动态库的先后顺序
编译目标代码时指定的动态库搜索路径
对于elf格式的可执行程序，是由ld-linux.so*来完成搜索：

LD_LIBRARY_PATH
/etc/ld.so.cache
default path /lib, and then /usr/lib.
https://blog.csdn.net/kevin_darkelf/article/details/38513781 

ldd LIBARY_PATH
方法一：在配置文件 /etc/ld.so.conf 中指定动态库搜索路径。每次编辑完该文件后，都必须运行命令 ldconfig 使修改后的配置生效 。

LIBRARY_PATH环境变量用于在程序编译期间查找动态链接库时指定查找共享库的路径，例如，指定gcc编译需要用到的动态链接库的目录。

LD_LIBRARY_PATH环境变量用于在程序加载运行期间查找动态链接库时指定除了系统默认路径之外的其他路径，注意，LD_LIBRARY_PATH中指定的路径会在系统默认路径之前进行查找。设置方法如下（其中，LIBDIR1和LIBDIR2为两个库目录）：

开发时，设置LIBRARY_PATH，以便gcc能够找到编译时需要的动态链接库。

发布时，设置LD_LIBRARY_PATH，以便程序加载运行时能够自动找到需要的动态链接库。






https://www.cnblogs.com/taskiller/archive/2012/12/14/2817650.html
ldd 查找动态库依赖关系

搜索动态库的先后顺序

http://www.cnblogs.com/kex1n/p/5993498.html 

LIBRARY_PATH环境变量用于在程序编译期间查找动态链接库时指定查找共享库的路径

LD_LIBRARY_PATH环境变量用于在程序加载运行期间查

#Makefile 选项
CFLAGS 表示用于 C 编译器的选项，

CXXFLAGS 表示用于 C++ 编译器的选项。

这两个变量实际上涵盖了编译和汇编两个步骤。

CFLAGS： 指定头文件（.h文件）的路径，如：CFLAGS=-I/usr/include -I/path/include

LDFLAGS：gcc 等编译器会用到的一些优化参数，也可以在里面指定库文件的位置。用法：LDFLAGS=-L/usr/lib -L/path/to/your/lib

LIBS：告诉链接器要链接哪些库文件，如LIBS = -lpthread -liconv

LDFLAGS是告诉链接器从哪里寻找库文件，而LIBS是告诉链接器要链接哪些库文件
```./configure --prefix=$HOME/.local CFLAGS="-I$HOME/.local/include -I$HOME/.local/include/ncurses" LDFLAGS="-L$HOME/.local/lib -L$HOME/.local/include/ncurses -L$HOME/.local/include"```
#动态链接库
1. 创建
`gcc -shared hello.c -o libhello.so`
2.链接起来 `gcc test.c -Ihello -L. -o test`
3. 运行时仍找不到，因为系统从LD_LIBRARY_PATH定义的变量中找，
`export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH`即可。

静态链接库
创建 gcc -c hello.c -o hello.o
ar -r libhello.a hello.o 创建一个新库libhello.a
使用 
`gcc test.c libhello.a -L. -o hello.static` 生成的hello.static就不再依赖libhello.a



## CMake
CMAKE_INSTALL_PREFIX  默认安装路径(/usr/local)
CMAKE找包是通过xx.make文件指定的，如果改变也是更改MAKEXX_PATH，或者指定

```cmake -DOpenCV_DIR='D:\coding\opencv3.2\opencv\build' .. 
https://blog.csdn.net/yang__jing/article/details/88118994``

cmake 编译之前可以指定CUDA版本
```CUDA_BIN_PATH=/usr/local/cuda9.0 instead of the default /usr/local/cuda```