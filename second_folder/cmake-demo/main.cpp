#include <iostream>
#include "Log/Log.hpp"
#include "MathFucntion.h"
#include <thread>
#include "TutorialConfig.h"
class Person
{
public:
    int value;
    Person(){
        std::cout << "Cons" <<value<< std::endl;
    }
    Person(int x){
        value = x;
        std::cout << "Cons" <<value<< std::endl;
    }
    ~Person(){
        std::cout << "Des" <<value<< std::endl;
    }
    void hello() {
        cout << "test hello!n";
    };
    void lambda() {
        auto fun = [this]{ // 捕获了 this 指针
            this->hello(); // 这里 this 调用的就是 class test 的对象了
        };
        fun();
    }
};
int main(int argc, char *argv[]) {
    std::cout << "Hello, World!" << std::endl<<std::flush;
    fprintf(stdout,"%s Version %d.%d\n",
            argv[0],
            Tutorial_VERSION_MAJOR,
            Tutorial_VERSION_MINOR);
    ASDF::Log::Instance().SetVerbose(-1);
    ASDF::Log::Instance().Error("Beam size = " + std::to_string(232));
    double outputValue = mysqrt(16);
    fprintf(stdout,"The square root of %d is %g\n",
            16, outputValue);
//  lambda
    []{
        cout << "Hello,Worldn"<<endl;
    }();
    int i = 1024,j = 2048;
    auto func = [](int i) { // (int i) 是指传入改匿名函数的参数
        cout << i<< endl;
    };
    func(i);
//    [=] 拷贝捕获
    auto func1 = [=]{  // [=] 表明将外部的所有变量拷贝一份到该函数内部
        cout << i<< endl;
    };
    func1();
    cout << "i:" << i << endl;
    cout << "j:" << j << endl;
    cout << "&i:" << &i << endl;
    cout << "&j:" << &j << endl;
//    [&] 引用捕获
    auto fun1 = [&]{
        cout << "引用捕获 &i:" << &i << endl;
    };
    fun1();
    auto fun2 = [=, &i]{ // 默认拷贝外部所有变量，但引用变量 i
        cout << "i:" << &i << endl;
        cout << "j:" << &j << endl;
    };
    fun2();
//    捕获this
    Person t(1);
    t.lambda();
    delete &t;
    std::shared_ptr<Person> p1(new Person(1));// Person(1)的引用计数为1

    std::shared_ptr<Person> p2 = std::make_shared<Person>();

    p1.reset(new Person(3));// 首先生成新对象，然后引用计数减1，引用计数为0，故析构Person(1)
    // 最后将新对象的指针交给智能指针

    std::shared_ptr<Person> p3 = p1;//现在p1和p3同时指向Person(3)，Person(3)的引用计数为2

    p1.reset();//Person(3)的引用计数为1
    p3.reset();//Person(3)的引用计数为0，析构Person(3)
    return 0;
}