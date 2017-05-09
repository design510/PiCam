'''
MIT License

Copyright (c) 2017 willdevgh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# !/usr/bin/python
# coding=utf-8
# 控制树莓派摄像头录像

import picamera, sys, os, time, string, io

t = 8 # 录制时间
p = './' # 默认保存路径

try:
	if len(sys.argv) >= 2:
		t = string.atoi(sys.argv[1], 10)

	if len(sys.argv) >= 3:
		if not os.path.exists(sys.argv[2]):
			print('给出的路径不存在[%s]' % sys.argv[2])
			exit()
		else:
			p = sys.argv[2]

except ValueError:
    print('参数为整数')
    exit()
else:
	print('录制时间[%d]' %t)
	print('录像保存至[%s]' %p)

print('start recording...')

filename = str(time.time()) + '.h264'	

with open(p + filename, 'wb') as vedio:
	with picamera.PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.start_recording(vedio, format='h264', quality=23)
		camera.wait_recording(t)
		camera.stop_recording()
		vedio.flush()

print('done!')

# end of file
