import time
from tabnanny import errprint

import pyautogui as ag
import pygetwindow as gw
import constants as consts
import scripts
import os
import functions as fns

default_resolution = [1920, 1080]

def get_and_activate_window(window_title):
    try:
        win = gw.getWindowsWithTitle(window_title)[0]
        if win.isMinimized:
            win.restore()
        else:
            win.activate()
    except IndexError:
        print(f"窗口 '{window_title}' 未找到")
        return False

素材数量 = 14
素材 = [34, 58]
素材列表 = [[179, 191]]
素材首个位置 = [374, 170]
素材第二个位置 = [374, 200]
素材列表偏移量 = 30
当前处理素材 = 1


文本按钮位置 = [130 * consts.实际比例, 58 * consts.实际比例]

时间线 = [338, 1102]

工作目录 = "C:\\Users\\hjkl1\\Documents\\todos"
工作处理目录 = "C:\\Users\\hjkl1\\Documents\\todos\\processes"

if __name__ == '__main__':
    # 当前处理进度
    # 从 0 开始
    当前处理进度 = 0
    # 检查工作目录的文件数量
    # 需要循环的次数
    工作目录视频总数量 = fns.count_files_in_directory(工作目录)
    while 当前处理进度 < 工作目录视频总数量:
        移动后文件名 = 当前处理进度 + 1
        if fns.move_first_file(工作目录, 工作处理目录, f"{移动后文件名}") is None:
            errprint("移动文件到工作处理目录时发生错误")
            break
        scripts.exec_once(0)
        当前处理进度 += 1




