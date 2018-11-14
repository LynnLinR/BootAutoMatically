import os

def login_local(txt_name):
    with open('./start.txt') as f:
        for line in f.readlines():
            print(line)
            if os.system("start " + line) == 0:
                print("启动成功")
            else:
                print("启动失败")

def main():
    login_local("start.txt")

if __name__ == "__main__":
    main()