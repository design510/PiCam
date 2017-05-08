# !/usr/bin/python
# coding=utf-8
# 控制树莓派摄像头拍照

import time
import picamera
import sys
import string
import os

# 默认参数
n = 1 # 拍照张数
t = 2 # 拍照时间间隔
p = './'

# 参数处理
try:
    if len(sys.argv) >= 2:
	    n = string.atoi(sys.argv[1], 10)

    if len(sys.argv) >= 3:
        t = string.atoi(sys.argv[2], 10)

    if len(sys.argv) >= 4:
        if not os.path.exists(sys.argv[3]):
            print('给出的路径不存在')
            exit()
        else:
            p = sys.argv[3]

except ValueError:
    print('参数为整数')
    exit()
else:
    print('共拍照%s张，每张间隔%s秒。' %(n, t))
    print('保存至[%s]' %p)


with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.start_preview()
    # 曝光补偿
    camera.exposure_compensation = 2
    i = 0
    while (i < n):
        i += 1
        filename = str(time.time()) + '.jpg'
        print('正在拍摄第%d张照片 %s' %(i, filename))
        time.sleep(t)
        camera.capture(p + filename)

    camera.stop_preview()
print('拍摄完成！')
# end of file
