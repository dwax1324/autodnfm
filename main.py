import pyautogui
import time

ff = pyautogui


if not (ff.size().width == 1920 and ff.size().height == 1080):
    print("This program requires 1920x1080 resolution")
    exit()

for i in range(5):
    print("program starts in " + str(5-i))
    time.sleep(1)
img_character_swap=img_epic=img_dungeon_select=img_start_battle=img_skip=img_go_home=img_confirm=img_revive=1

def update():
    global img_character_swap
    global img_epic
    global img_dungeon_select
    global img_start_battle
    global img_skip
    global img_go_home
    global img_confirm
    global img_revive
    img_character_swap = ff.locateOnScreen('./imgs/character_swap.png',confidence=0.8)
    img_epic = ff.locateOnScreen('./imgs/epic.png',confidence=0.8)
    img_dungeon_select = ff.locateOnScreen('./imgs/dungeon_select.png',confidence=0.8)
    img_start_battle = ff.locateOnScreen('./imgs/start_battle.png',confidence=0.8)
    img_skip = ff.locateOnScreen('./imgs/skip.png',confidence=0.8)
    img_go_home = ff.locateOnScreen('./imgs/go_home.png',confidence=0.8)
    img_confirm = ff.locateOnScreen('./imgs/confirm.png',confidence=0.8)
    img_revive = ff.locateOnScreen('./imgs/revive.png',confidence=0.8)

def print_all():
    print(ff.position())
    # print(img_character_swap)
    # print(img_epic)
    # print(img_dungeon_select)
    # print(img_start_battle)

def upgrade_equipment():
    ff.press('i') , time.sleep(1)
    ff.click(1134, 947), time.sleep(1)
    ff.click(957, 744),time.sleep(1)
    ff.press('i'),time.sleep(1)
def repair():
    ff.press('i') , time.sleep(1)
    ff.click(1129,1021), time.sleep(1) #x=1129, y=1021
    ff.click(1553,959),time.sleep(1)  #x=1553, y=959
    ff.press('esc'),time.sleep(1)
    ff.press('i'),time.sleep(1)

def sell():
    ff.press('i') , time.sleep(1)
    ff.click(1690,1024), time.sleep(1) #x=1129, y=1021
    ff.click(1604,947),time.sleep(1)  #x=1553, y=959
    ff.click(1126,715),time.sleep(1)  #x=1553, y=959
    ff.press('esc'),time.sleep(1)
    ff.press('esc'),time.sleep(1)
    ff.press('i'),time.sleep(1)
    # x=1690, y=1024)
    # x=1604, y=947)
    # x=1126, y=74
    # esc x 3i
# sell()
def go_battle():
    while True:
        update()
        if img_revive != None:
            ff.click(img_revive)
        for i in ['right','up','left','down']:
            ff.keyDown(i)
            if i == 'right':
                time.sleep(1)
            else:
                time.sleep(0.5)
            ff.keyUp(i)
        ff.keyDown('x')
        time.sleep(12)
        ff.keyUp('x')

        if img_skip != None or img_go_home != None:
            break

    
    while img_go_home == None:
        update()
        if img_skip != None:
            ff.click(img_skip)
        if img_confirm!= None:
            ff.click(img_confirm)

    ff.click(img_go_home)

    time.sleep(3)
    upgrade_equipment()
    repair()
    sell()




while True:
    update()
    print_all()
    if img_epic != None:
        ff.click(img_epic)
    
    if img_dungeon_select != None:
        ff.click(1600,905)
        go_battle()
    
    if img_skip != None:
        ff.click(img_skip)
    if img_confirm != None:
        ff.click(img_confirm)
    time.sleep(1)