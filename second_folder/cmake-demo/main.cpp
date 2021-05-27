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
        auto fun = [this]{ // ������ this ָ��
            this->hello(); // ���� this ���õľ��� class test �Ķ�����
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
    auto func = [](int i) { // (int i) ��ָ��������������Ĳ���
        cout << i<< endl;
    };
    func(i);
//    [=] ��������
    auto func1 = [=]{  // [=] �������ⲿ�����б�������һ�ݵ��ú����ڲ�
        cout << i<< endl;
    };
    func1();
    cout << "i:" << i << endl;
    cout << "j:" << j << endl;
    cout << "&i:" << &i << endl;
    cout << "&j:" << &j << endl;
//    [&] ���ò���
    auto fun1 = [&]{
        cout << "���ò��� &i:" << &i << endl;
    };
    fun1();
    auto fun2 = [=, &i]{ // Ĭ�Ͽ����ⲿ���б����������ñ��� i
        cout << "i:" << &i << endl;
        cout << "j:" << &j << endl;
    };
    fun2();
//    ����this
    Person t(1);
    t.lambda();
    delete &t;
    std::shared_ptr<Person> p1(new Person(1));// Person(1)�����ü���Ϊ1

    std::shared_ptr<Person> p2 = std::make_shared<Person>();

    p1.reset(new Person(3));// ���������¶���Ȼ�����ü�����1�����ü���Ϊ0��������Person(1)
    // ����¶����ָ�뽻������ָ��

    std::shared_ptr<Person> p3 = p1;//����p1��p3ͬʱָ��Person(3)��Person(3)�����ü���Ϊ2

    p1.reset();//Person(3)�����ü���Ϊ1
    p3.reset();//Person(3)�����ü���Ϊ0������Person(3)
    return 0;
}