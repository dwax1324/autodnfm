import pyautogui
import time

ff = pyautogui

for i in range(5):
    print("program starts in " + str(5-i))
    time.sleep(1)
img_character_swap = 1

def update():
    global img_character_swap
    img_character_swap = ff.locateOnScreen('./imgs/character_swap.png',confidence=0.8,)

update()
print(img_character_swap)
if img_character_swap != None:
    ff.click(img_character_swap)