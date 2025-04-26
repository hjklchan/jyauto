import pygetwindow as gw
import time

import os
import shutil


def move_first_file(
        dir_a=None,
        dir_b_name='B',
        new_name=None,
        overwrite=False,
        verbose=True
):
    """
    将指定目录中的第一个文件移动到子目录，并可选择重命名

    :param dir_a: 源目录（默认当前目录）
    :param dir_b_name: 目标子目录名称（默认为'B'）
    :param new_name: 新文件名（可选，包含扩展名。默认为None不重命名）
    :param overwrite: 是否覆盖目标文件（默认为False）
    :param verbose: 是否输出操作详情（默认为True）
    :return: 成功返回移动后的文件路径，失败返回None
    """
    # 设置源目录
    if dir_a is None:
        dir_a = os.getcwd()

    # 验证源目录
    if not os.path.isdir(dir_a):
        if verbose:
            print(f"[错误] 源目录不存在: {dir_a}")
        return None

    # 构建目标目录路径
    dir_b = os.path.join(dir_a, dir_b_name)

    try:
        # 创建目标目录（如果不存在）
        os.makedirs(dir_b, exist_ok=True)

        # 获取源目录文件列表（过滤目录，按名称排序）
        all_items = sorted(os.listdir(dir_a))
        files = [
            item for item in all_items
            if os.path.isfile(os.path.join(dir_a, item))
        ]

        if not files:
            if verbose:
                print(f"[提示] 没有可移动的文件: {dir_a}")
            return None

        # 获取第一个文件
        first_file = files[0]
        src_path = os.path.join(dir_a, first_file)

        # 处理目标文件名
        if new_name:
            dst_filename = new_name
            # 如果新名称没有扩展名，则保留原扩展名
            if '.' not in new_name and '.' in first_file:
                old_ext = first_file.split('.')[-1]
                dst_filename = f"{new_name}.{old_ext}"
        else:
            dst_filename = first_file

        dst_path = os.path.join(dir_b, dst_filename)

        # 检查是否覆盖
        if os.path.exists(dst_path) and not overwrite:
            if verbose:
                print(f"[跳过] 文件已存在: {dst_path}")
            return None

        # 执行文件移动
        shutil.move(src_path, dst_path)

        if verbose:
            action = "移动并重命名" if new_name else "移动"
            print(f"[成功] {action}文件: {first_file} -> {dst_path}")
        return dst_path

    except PermissionError as e:
        if verbose:
            print(f"[错误] 权限不足: {e}")
    except Exception as e:
        if verbose:
            print(f"[错误] 操作异常: {e}")

    return None

def force_activate_window(title):
    try:
        win = gw.getWindowsWithTitle(title)[0]
        if win.isMinimized:
            win.restore()
        win.activate()
        time.sleep(0.5)
        # 双重激活确保焦点
        win.activate()
        time.sleep(0.3)
    except Exception as e:
        print(f"窗口激活失败: {e}")


def count_files_in_directory(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])