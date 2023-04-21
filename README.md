# Campus-network-automatic-login
常州信息职业技术学院的自动登录
#开机自动登录，
可以更改代码里的账号密码,固定住可以在一下方法实现是先开机自启，免除手动登录的麻烦，把无线网络设置自动连接这样无论是学习的ccit-wlan还是宿舍校园网都可以自动连接
在 Windows 系统中，可以使用以下方法让计算机开机后自动执行一个 Python 脚本：

创建一个批处理文件（.bat 文件），在其中添加要执行的 Python 脚本命令。例如，假设你要执行的 Python 脚本名为 my_script.py，那么批处理文件内容可以是：
@echo off
python "C:\path\to\my_script.py"

其中，C:\path\to\my_script.py 是你的 Python 脚本文件路径。

将该批处理文件复制到启动文件夹中。启动文件夹通常位于以下路径之一：
C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
其中，username 是你的用户名。你可以将批处理文件拖放到启动文件夹中，或者使用 Windows 资源管理器将其复制到该文件夹中。

现在，每次计算机开机时，Windows 就会自动运行该批处理文件，并执行其中的 Python 脚本。
