# 开启启动服务

## 为什么要写这个

    如果服务器断电断网,随后修复后重启,服务器内部的服务需要按顺序启动,为了减少人工的操作,进行脚本的编写

## 如何做到开机启动这个脚本

- 讲脚本放到windows下的启动目录
    > 路径 : c:\\Users\\XXXXXX\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup

## 如果开机启动顺序包含两个服务器之间的联动

- 需要通过tcp来进行通讯,用传参数进行启动顺序的调用

## 主要逻辑

- 将**main.exe**和**start.txt**放入开机启动文件夹
    - start.txt 用来存放需要开机启动的文件绝对路径
- 如果需要多台服务器之间有先后顺序的启动的话,进行TCP或者UDP的传输信号