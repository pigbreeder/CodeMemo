# ref
# https://blog.csdn.net/u012839187/article/details/45790491
# https://blog.csdn.net/pyl88429/article/details/78203140
# https://www.kancloud.cn/itfanr/cmake-practice
# https://blog.csdn.net/ktigerhero3/article/details/70313350
cmake_minimum_required(VERSION 3.2)
project(test)
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
#set(CMAKE_CXX_STANDARD 11)
# 查找当前目录下的所有源文件并将名称保存到 DIR_SRCS 变量
#aux_source_directory(. SOURCES)  # 这个是添源文件的 aux_source_directory(./world_src DIR_WORLD_SRCS)
# 添加头文件路径
include_directories ("${PROJECT_SOURCE_DIR}/Log")
# 添加库文件路径
link_directories ("${PROJECT_SOURCE_DIR}/Log") # find_library find_package 这两个和该功能一样。如果不生成库文件 其实没用。增加lib查找路径
#find_library(TIFF_LIBRARY
#                NAMES tiff tiff2
#                PATHS /usr/local/lib /usr/lib
#                ) # 当不同的系统，相同的库文件被安装在不同路径下时，就需要使用这个命令
#find_path(TIFF_INCLUDES tiff.h
#                /usr/local/include
#                /usr/include
#                ) # 当不同的系统，相同的头文件被安装在不同路径下时，就需要使用这个命令
#find_package寻找Findxxx.cmake文件，首先到${CMAKE_MODULE_PATH}中找，然后在自己的/modules/中找。
add_subdirectory (Log) # ADD_SUBDIRECTORY(src bin)
# 用于向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置。

add_library(MathFunctions MathFucntion.cpp) # 将指定的源文件生成链接文件
# ADD_LIBRARY(unkprocess_static STATIC ${LIBUNKPROCESS_SRC})
# SET_TARGET_PROPERTIES(unkprocess_static PROPERTIES OUTPUT_NAME "unkprocess")
# 这个一般是静态库改名字用
# 
add_executable(test main.cpp)
# 链接库文件
target_link_libraries(test MathFunctions)  #指定要链接哪个lib
target_link_libraries(test Log)

configure_file (
        "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
        "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)

set(CMAKE_CXX_FLAGS   "-std=c++11")             # c++11
set(CMAKE_CXX_FLAGS   "-g")                     # 调试信息
set(CMAKE_CXX_FLAGS   "-Wall")                  # 开启所有警告

#常量#################################################
# CMAKE_BINARY_DIR <projectname>_BINARY_DIR 和PROJECT_BINARY_DIR 变量
#他们指的编译发生的当前目录，如果是内部编译，就相当于PROJECT_SOURCE_DIR 也就是工程代码所在目录，如果是外部编译，指的是外部编译所在目录，也就是例中的build
# CMAKE_SOURCE_DIR PROJECT_SOURCE_DIR <projectname>_SOURCE_DIR
#这三个变量指代的内容是一致的,不论采用何种编译方式,都是工程顶层目录。也就是在 in source 编译时,他跟 CMAKE_BINARY_DIR 等变量一致。
# CMAKE_INSTALL_PREFIX  #make install 的安装路径 默认安装路径(/usr/local)
# CMAKE_BUILD_TYPE #生成的目标为debug或者release
# CMAKE_C_FLAGS #gcc 的编译参数指定，这个非常好用，一般通过set 修改其值
# CMAKE_CXX_FLAGS #g++ 和上面CMAKE_C_FLAGS 类似
# CMAKE_CURRENT_SOURCE_DIR # 当前CMakeLists.txt所在的目录，主要用来定位某文件
# CMAKE_CURRENT_BINARY_DIR # 当前CMakeLists.txt对应的编译时的目录。in-source编译,跟CMAKE_CURRENT_SOURCE_DIR一致, out-of-source编译,他指的是 target 编译目录。
#使用 ADD_SUBDIRECTORY(src bin)可以更改这个变量的值。
#使用 SET(EXECUTABLE_OUTPUT_PATH <新路径>)并不会对这个变量造成影响,它仅仅修改了最终目标文件存放的路径。
# EXECUTABLE_OUTPUT_PATH 和LIBRARY_OUTPUT_PATH 分别用来重新定义最终结果的存放目录，
# TARGETS 指的是所有生成的文件(lib/exe)
# CMAKE_MODULE_PATH    SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake) 这时候你就可以通过INCLUDE 指令来调用自己的模块了。
#Install#################################################
install(TARGETS test Log
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
# 复制源码中的指定的头文件到 include下
install(FILES ${PROJECT_SOURCE_DIR}/Log/Log.hpp DESTINATION include)

# 复制sample代码到 sample下
#install(FILES ${PROJECT_SOURCE_DIR}/facedetect/test_detect.cpp DESTINATION sample)
#如果默认不定义权限PERMISSIONS，安装后的权限为,OWNER_WRITE,OWNER_READ, GROUP_READ,和WORLD_READ，即644权限。
#install(TARGETS myExe mySharedLib myStaticLib
#        RUNTIME DESTINATION bin
#        LIBRARY DESTINATION lib
#        ARCHIVE DESTINATION lib/static)
#install(TARGETS mySharedLib DESTINATION /some/full/path)
#将会把myExe安装到<prefix>/bin目录下，把myStaticLib安装到<prefix>/lib/static目录下。
#在非-DLL平台上，mySharedLib将会被安装到<prefix>/lib和/some/full/path下。在DLL平台上，
#mySharedLib DLL将会被安装到<prefix>/bin和/some/full/path路径下，它的导出库会被安装到<prefix>/lib/static和/some/full/path路径下。

#技巧#################################################
#cmake生成makefile之后，CMakeCache.txt可以编辑编译选项。
#CUDA指定版本 export CUDA_BIN_PATH=/usr/local/cuda-9.0