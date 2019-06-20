cmake_minimum_required(VERSION 3.2)
project(test)
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
#set(CMAKE_CXX_STANDARD 11)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
#aux_source_directory(. SOURCES)
add_library(MathFunctions MathFucntion.cpp)
# 添加头文件路径
include_directories ("${PROJECT_SOURCE_DIR}/Log")
# 添加库文件路径
link_directories ("${PROJECT_SOURCE_DIR}/Log")
add_subdirectory (Log)
add_executable(test main.cpp)
# 链接库文件
target_link_libraries(test MathFunctions)
target_link_libraries(test Log)

configure_file (
        "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
        "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)

set(CMAKE_CXX_FLAGS   "-std=c++11")             # c++11
set(CMAKE_CXX_FLAGS   "-g")                     # 调试信息
set(CMAKE_CXX_FLAGS   "-Wall")                  # 开启所有警告

#常量#################################################
#CMAKE_INSTALL_PREFIX  #make install 的安装路径 默认安装路径(/usr/local)
#CMAKE_BUILD_TYPE #生成的目标为debug或者release
#CMAKE_C_FLAGS #gcc 的编译参数指定，这个非常好用，一般通过set 修改其值
#CMAKE_CXX_FLAGS #g++ 和上面CMAKE_C_FLAGS 类似
#CMAKE_CURRENT_SOURCE_DIR # 当前CMakeLists.txt所在的目录，主要用来定位某文件
#CMAKE_CURRENT_BINARY_DIR # 当前CMakeLists.txt对应的编译时的目录

#TARGETS 指的是所有生成的文件(lib/exe)
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