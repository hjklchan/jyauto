import pyautogui as ag
import functions as fns
import constants as consts
import time

def exec_once(index = 0):
    screen_width, screen_height = ag.size()

    fns.force_activate_window("剪映专业版")
    """ 点击创作
    """
    # 请确保已经打开 app
    center_x = ag.size()[0] / 2.0
    center_y = ag.size()[1] / 2.0
    ag.moveTo(center_x, (center_y - (280 * consts.实际比例)) * consts.实际比例, duration=0.5)
    ag.click()
    # 等待打开
    time.sleep(2.8)

    """ 点击导入素材
    """
    ag.moveTo(468 * consts.实际比例, 155 * consts.实际比例, duration=0.5)
    ag.click()
    # 选择素材
    time.sleep(2)
    ag.moveTo((consts.素材首个位置[0] + (index - 1) * 30 * consts.实际比例) * consts.实际比例, consts.素材首个位置[1] * consts.实际比例,
              duration=0.5)
    ag.doubleClick()
    # 选择第一个素材并拖拽到时间线
    ag.moveTo(181, 193)
    time.sleep(0.5)
    ag.dragTo(191, 1105, 0.5)
    ag.click()
    time.sleep(5)

    """ 设置美颜
    """
    ag.click()
    # 移动到画面按钮
    ag.moveTo(2100, 57, 0.3)
    ag.click()
    time.sleep(1)
    # 点击美颜美体
    ag.moveTo(2494, 109, 0.3)
    ag.click()
    time.sleep(1)
    # 点击美颜预设
    ag.moveTo(2253, 160, 0.3)
    ag.click()
    time.sleep(2)
    # 点击首个预设
    ag.moveTo(2195, 266, 0.3)
    ag.click()

    """ 点击识别字幕
    """
    # 点击字幕按钮
    字幕按钮位置 = [327 * consts.实际比例, 58 * consts.实际比例]
    ag.moveTo(字幕按钮位置[0], 字幕按钮位置[1], duration=0.5)
    ag.click()
    time.sleep(4)
    # # 选择只能划重点 (160, 262)
    # ag.moveTo(160, 262, duration=0.5)
    # ag.click()
    # time.sleep(0.5)
    # # 选择智能去水词 (160, 310)
    # ag.moveTo(160, 310, duration=0.5)
    # ag.click()
    # time.sleep(0.5)
    # 点击识别字幕
    开始识别按钮位置 = [770 * consts.实际比例, 746 * consts.实际比例]
    ag.moveTo(开始识别按钮位置[0], 开始识别按钮位置[1], duration=0.5)
    ag.click()
    # 识别字幕等待
    time.sleep(1)
    # 开始识别字幕
    print("准备识别字幕")
    while True:
        print("正在识别字幕")
        中心点坐标 = [screen_width // 2, screen_height // 2]
        # 获取中心点的颜色
        color = ag.pixel(中心点坐标[0], 中心点坐标[1])
        print(color)

        time.sleep(1)
        if color != (0, 0, 0):
            break

    time.sleep(0.8)
    print("准备识别水词")
    # 开始识别水词
    while True:
        print("正在识别水词")
        中心点坐标 = [screen_width // 2, screen_height // 2]
        # 获取中心点的颜色
        color = ag.pixel(中心点坐标[0], 中心点坐标[1])
        print(color)

        time.sleep(1)
        if color != (0, 0, 0):
            break

    time.sleep(0.8)
    print("准备等待加载进度")
    # 等待疑似可能的加载进度
    while True:
        print("等待加载中")
        中心点坐标 = [screen_width // 2, screen_height // 2]
        # 获取中心点的颜色
        color = ag.pixel(中心点坐标[0], 中心点坐标[1])
        print(color)

        time.sleep(0.5)
        if color != (0, 0, 0):
            break

    time.sleep(1)
    # 删除无用字幕
    ag.moveTo(2507, 749)
    ag.click()
    time.sleep(1)

    """ 点击智能包装 (376, 60)
    """
    智能包装按钮位置 = [376, 60]
    ag.moveTo(智能包装按钮位置[0], 智能包装按钮位置[1], duration=0.5)
    ag.click()
    # 选择智能推荐 (162, 188)
    ag.moveTo(162, 188, duration=0.5)
    ag.click()
    # 点击开始匹配 (773, 745)
    ag.moveTo(773, 745, duration=0.5)
    ag.click()
    time.sleep(2)
    # 识别询问是否重新包装
    中心点坐标 = [screen_width // 2, screen_height // 2]
    # 获取中心点的颜色
    color = ag.pixel(中心点坐标[0], 中心点坐标[1])

    time.sleep(1.5)

    if color == (0, 0, 0):
        ag.moveTo(1326, 743, 0.5)
        ag.click()

    time.sleep(2.3)

    print("准备生成智能包装")
    # 智能包装等待
    while True:
        # print(get_center_pixel_color())
        print("智能包装正在生成中")
        中心点坐标 = [screen_width // 2, screen_height // 2]
        # 获取中心点的颜色
        color = ag.pixel(中心点坐标[0], 中心点坐标[1] + 36)
        #
        time.sleep(0.4)
        print(color)
        if color[0] > 25:
            break

    time.sleep(1)
    print("继续操作")

    # 关闭窗口
    ag.moveTo(screen_width - 15, 10, 0.5)
    ag.click()
    time.sleep(1.5)