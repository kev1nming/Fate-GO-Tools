# Fate-GO-Tools
Python Fate/Grand Order
#### Python scripts based on adb([platform-tools](https://developer.android.com/studio/releases/platform-tools))
<br>
利用adb和Android模拟器实现的简单脚本<br>
用于抽取无限池和领取礼物箱中的物品<br>

## Useage

#### First Step
打开文件，在开头修改模拟器的adb连接地址和按钮的位置<br>
*每个厂家模拟器的`adb_address`有所不同，同时按钮位置根据分辨率不同也有所区别*<br>
*可以利用截图或者`pyautogui`等库获取按钮的位置*<br>

#### Second Step
打开模拟器，进入游戏<br>
抽取无限池请使用`fgo_click.py`，进入无限池界面，在命令行中输入`python fgo_click.py`,输入池数后即可开始抽取<br>
*池数过多时请注意礼物箱是否溢出，一池大约会占30~40个礼物箱位置*<br>
领取礼物箱中的物品请点击礼物箱，然后在命令行中输入`python get_giftbox.py`，输入想要领取的数量后即可开始领取<br>
*此时请注意仓库的数量是否足够，比如一个礼物可能含有多个狗粮*<br>

### 脚本实现非常简单，代价就是稳定性不是很高，若是大佬们有更好的想法请多多交流
