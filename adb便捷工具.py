import os

print("[1]安装APK [2]调整DPI [3]adb shell [4]安装adb [5]关于")
命令 = input()
命令 = int(命令)

if 命令 == 1:
        print("请输入apk位置(无需输入/storage/emulated/0/和.apk)")
        命令 = input()
        命令 = "adb install " + "/storage/emulated/0/" + 命令 + ".apk"
        os.system(命令)
if 命令 == 2:
        print(请输入DPI120～320,默认320)
        命令 = input ()
        命令 = "adb shell wm density " + 命令
        os.system(命令)
if 命令 == 3:
        print("请输入直接adb shell指令")
        命令 = input()
        命令 = "adb shell " + 命令
        os.system(命令)
if 命令 == 4:
        print("是否要安装adb?(仅限termux)")
        print("[1]是 [2]否")
        命令 = input()
        命令 = int(命令)
        if 命令 == 1:
                os.system('bash -c "$(curl -L http://rendiix.github.io/install-repo.sh)"'')
                os.system("pkg install git")
                os.system("git clone https://github.com/rendiix/termux-adb-fastboot.git && cd termux-adb-fastboot && bash install.sh")
if 命令 == 5:
        print("adb便捷工具v1.1")
        print("bilibili@楼下的苦力怕")
        print("基安@楼下的苦力怕")
        print("gayhub:https://github.com/lxdklp/adb-handy-tools")