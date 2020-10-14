import pyautogui


#实时获取鼠标的位置
print('Press ctrl-c to quit this')
try:
    while True:
        x,y=pyautogui.position()
        positionStr='X:'+str(x).rjust(4)+'Y:'+str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')
'''
pyautogui.moveTo(414,56)
pyautogui.click()
pyautogui.typewrite(['hello world','a','left','left','b','b'])
pyautogui.doubleClick()
pyautogui.dragRel(-20,0,mouseDownUp=False)
'''
print('x',end='')
print('y',end='')
import pyautogui
import time

#实时获取鼠标的位置
print('Press ctrl-c to quit this')
try:
    while True:
        time.sleep(3)
        x,y=pyautogui.position()
        positionStr='X:'+str(x).rjust(4)+'Y:'+str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')