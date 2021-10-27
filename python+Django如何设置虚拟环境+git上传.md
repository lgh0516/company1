# blog
python+django_blog

激活虚拟环境 workon blog

2. 克隆项目代码仓库
1.进入本地项目目录

cd Desktop/
2.克隆仓库
使用 Git Bash/ cmd
git clone https://github.com/qruihua/itheima_blog.git
3. 创建美多商城工程
1.进入本地项目仓库

cd itheima_blog/
2.创建美多商城虚拟环境，安装Django框架

$ mkvirtualenv -p python3 blog
$ pip install django==2.2
3.创建美多商城Django工程

$ django-admin startproject blog
创建工程完成后：运行程序，测试结果。

git add .
git commit -m 'createproject'
#########https://copyfuture.com/blogs-details/20210915051639331p#######

建議把 token 直接添加遠程倉庫鏈接中，這樣就不用每次提交代碼都要輸入token 了

git remote set-url origin https://<your_token>@github.com/<USERNAME>/<REPO>.git
<your_token>：換成你自己得到的 token
<USERNAME>：是你自己 github 的用戶名
<REPO>：是你的倉庫名稱

e.g.
git remote set-url origin https://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@github.com/lgh0516/itheima_blog.git

git push
/or/
git push --set-upstream origin <master>




