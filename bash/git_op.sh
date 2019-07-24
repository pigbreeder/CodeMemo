#!/bin/bash
#https://www.zhihu.com/question/21215715
# 设置颜色
git config --global color.status auto  
git config --global color.diff auto  
git config --global color.branch auto  
git config --global color.interactive auto  
#
#git 冲突处理
$ git checkout - -ours xxx/A.java # 选取当前分支的结果
$ git checkout - -theirs xxx/A.java # 选取非分支结果

#用于保存和恢复工作进度
#https://gist.github.com/subchen/3409a16cb46327ca7691
git stash #保存当前的工作进度。会分别对暂存区和工作区的状态进行保存
git stash save "message..." #这条命令实际上是第一条 git stash 命令的完整版
git stash list #显示进度列表。此命令显然暗示了git stash 可以多次保存工作进度，并用在恢复时候进行选择
git stash pop [--index] [<stash>]
#如果不使用任何参数，会恢复最新保存的工作进度，并将恢复的工作进度从存储的工作进度列表中清除。
#如果提供参数（来自 git stash list 显示的列表），则从该 <stash> 中恢复。恢复完毕也将从进度列表中删除 <stash>。
#选项--index 除了恢复工作区的文件外，还尝试恢复暂存区。
git stash apply [--index] [<stash>] #除了不删除恢复的进度之外，其余和 git stash pop 命令一样
git stash clear #删除所有存储的进度


# 删除
git clean -fd #删除UNtrack文件
git branch -dr <remote>/<branch> # Shorter删除远程分支
git clean  -f 清除未追踪文件 
git clean -fd清除未追踪文件、文件夹


#撤销
git reset HEAD file #可以将暂存区的修改撤销掉，重新放回工作区
1. 已经提交上github，想要撤销
git reset - -hard <commit_id>
git push origin HEAD - -force
2. 本地撤销
git checkout -- file可以丢弃工作区的修改;
git reset HEAD file可以把暂存区的修改撤销掉，重新放回工作区状态;
git reset --hard HEAD^回退到“add distributed”版本时的状态；
 git reset –soft：（仅重新修改commit内容）回退到某个版本，只回退了commit的信息，不会恢复到index file一级。如果还要提交，直接commit即可

查看某个文件的历史
git log --pretty=oneline filename
git log -- stat  仅显示区分文件 后可接参数 -n
git diff --name-status master origin/develop  #查看文件差异
git show commitId
git log filename #查看某个文件历史
git diff commit1 commit2 file/path #查看某个文件变动
git diff branch1 branch2 # 查看分支的不同

查看所有被git管理的文件
git ls-files


分支操作
拉取分支 git fetch origin
切换到远程分支 git checkout origin/remoteName -b remoteName
创建新分支 git checkout -b newBranch  ; 
推送到远端 git push origin newBranch:newBranch  git push <远程主机名> <本地分支名>:<远程分支名>
删除远程分支 git push origin -- delete <branchName> 
git push origin :<branchName>
删除本地分支 git branch -d <branchName>
重命名 git branch -m <branchName> <newBranchName>
获取远程分支 git pull origin remoteBranchName:localBranchName  或者 git checkout -b remoteBranchName git pull ...
创建分支 git branch Name
创建并切换 git checkout -b Name

