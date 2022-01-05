[TOC]

# 注册github账号

在https://github.com/上注册github账号

# 下载git

在https://git-for-windows.github.io/下载git，安装。

# 使用git

- 登录github账号，在首页点击New新建一个项目

![image-20220105161407510](F:\typoro\img\image-20220105161407510.png)

- 填写项目信息

  Repository name: 仓库名称（输入名字，最好不要使用中文）

  Description(可选): 仓库描述介绍

  Public, Private : 仓库权限（公开共享，私有或指定合作者）

  Initialize this repository with a README: 添加一个README.md

  gitignore: 不需要进行版本管理的仓库类型，对应生成文件.gitignore

  license: 证书类型，对应生成文件LICENSE

  ![image-20220105161709199](F:\typoro\img\image-20220105161709199.png)

- 创建成功

  ![image-20220105161914016](F:\typoro\img\image-20220105161914016.png)

- git到本地

  - 在本地文件夹下右击选择Git Bash Here。如下图在F盘的git文件夹下右击选择Git Bash Here。

    ![image-20220105162505860](F:\typoro\img\image-20220105162505860.png)

  - 把github上面的仓库克隆到本地

  ![image-20220105162843129](F:\typoro\img\image-20220105162843129.png)

  - 在本地文件夹里操作，修改本地项目learning中的文件

  - 将本地项目文件的修改更新到远程仓库

    ![image-20220105164633467](F:\typoro\img\image-20220105164633467.png)

    ![image-20220105164422547](F:\typoro\img\image-20220105164422547.png)

  - 此时本地上的修改已经同步到github上

# 遇到的问题

- ```linux
  git push origin master报错
  ```

  - 其含义是：将本地的 master 分支推送到 origin 主机的 master 分支。

  - ```
    git push <远程主机名> <本地分支名>:<远程分支名>
    如果本地分支名与远程分支名相同，可以写为
    git push <远程主机名> <本地分支名>
    ```

  - 但是新版本的github的主分支叫main,而本地主分支为master,所有可以修改本地分支为main,再$ git push origin main

    ![image-20220105165348057](F:\typoro\img\image-20220105165348057.png)

    ![image-20220105170439793](F:\typoro\img\image-20220105170439793.png)

- github项目中不要用中文命名

  ![image-20220105170704449](F:\typoro\img\image-20220105170704449.png)

- 删除远程仓库（github)中的文件——将远程仓库里面的项目拉下来，在本地操作删除某文件，再上传到gitHub
  - git pull origin master 将远程仓库里面的项目拉下来
  - git rm 文件名 删除本地文件
  - git commit -m "提交描述"