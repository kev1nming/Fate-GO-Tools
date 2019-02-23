import os,sys
import time

giftbox = '350 567'
gift1 = '410 190'

adb_address = '127.0.0.1:7555'

os.system('adb kill-server && adb connect %s && adb devices' % adb_address)

def click(position):
	os.system('adb shell input tap %s' % position)

i = 0
i = input('领取礼物数量: ')
print('将要领取礼物数量：%d个' % int(i))

#click(giftbox)
for c in range(int(i)):
	click(gift1)
	time.sleep(0.25)	