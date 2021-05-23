
https://zhuanlan.zhihu.com/p/55409307  
https://www.zybuluo.com/hanxiaoyang/note/534296  
https://www.voidking.com/dev-jupyter-debug/  

```

# ipy导出py
ipython nbconvert — to script abc.ipynb
# 导入ipy函数
pip install ipynb
from ipynb.fs.full.my_functions import factorial

%who      列出所有变量
%who_ls   以列表形式列出所有变量
%whos     展示所有变量更详细的信息

按住Alt拖动鼠标              多行编辑、矩形选框
按住Ctrl在多个位置点击鼠标    多处同时编辑

Shift + Tab 显示刚刚在代码单元中键入的对象的文档字符串（文档），可以继续按此快捷键以循环浏览几种文档模式。


# jupyter 每行都显示，不用print
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# jupyter 远程连接
1 生成配置文件
jupyter notebook --generate-config
2 生成一个密码
  jupyter notebook password
3 写入配置文件
c.NotebookApp.password
c.NotebookApp.ip='*'  # 允许任何ip访问
c.NotebookApp.open_browser = False  # 默认不打开浏览器



# 快捷键
## 编辑单元格
Y : 单元转入代码状态
M :单元转入markdown状态
Shift + M 合并单元格
A/B 在上(下)插入单元格
X 剪切单元格
C 复制单元格
Shift+V 粘贴在上面
V 粘贴在下面
Z 撤销删除
D,D 删除选中单元格



# 编辑模式
Ctrl + Shift + - 在光标处分割代码块






magic
设置环境变量
%env OMP_NUM_THREADS=4
%matplotlib：inline
运行ipy和py
%run ./two-histograms.ipynb
%load：从外部脚本中插入代码
%store: 在notebook文件之间传递变量
%who: 列出所有的全局变量
%reset：清除变量
%%time 会告诉你cell内代码的单次运行时间信息。
%timeit 使用了Python的 timeit 模块，该模块运行某语句100，000次（默认值），然后提供最快的3次的平均值作为结果。
%prun: 告诉你程序中每个函数消耗的时间
%%writefile myFirstBook.py # 这里，myFirstBook.py是任意你想保存的文件名 
%%pcat

%pdb调试程序
%debug
在调试模式下，我们也可以通过输入“up”来对外层函数进行调试，查看其中的变量情况。同样的，也可以通过“down”进入内层函数。

3、在notebooke中执行 %pdb on 可以设置为当异常发生时自动进入调试模式，在某些特殊的情况下，这么做可能会更为方便：


# 执行多个shell命令
%%!
ls -l
pwd
who


%%bash
for i in {1..5}
do
   echo "i is $i"
done


# 捕获输出。
可以直接从子进程中捕获stdout/err到Python变量中, 替代直接进入stdout/err。


%%bash --out output --err error
echo "hi, stdout"
echo "hello, stderr" >&2
可以直接访问变量名了。
print(error)
print(output)



```