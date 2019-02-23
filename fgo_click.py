import os,sys
import time

#-----以下参数请根据分辨率自行调整-----
adb_address = '127.0.0.1:7555'

lottery_buttom = '350 380' #抽10次按钮
change_buttom = '912 226' #重置礼物按钮
ok_buttom = '670 480' #执行按钮
ok2_buttom = '516 488' #确认按钮
#---------------------------------------

os.system('adb kill-server && adb connect %s && adb devices' % adb_address)

def click(position):
	os.system('adb shell input tap %s' % position)

i = 0
count = 0
i = input('要抽的池数: ')
dis = int(int(i) - 1)
print('将要抽的池数：%d池' % int(i))
for c in range(int(i)*93):
	click(lottery_buttom)
	time.sleep(0.2)	
	count += 1
	if count>94:
		count = 0
		print('剩余池数：%d池' % dis)
		dis -= 1
		click(change_buttom)
		time.sleep(1)
		click(ok_buttom)
		time.sleep(1)
		click(ok2_buttom)
		time.sleep(0.1)
		