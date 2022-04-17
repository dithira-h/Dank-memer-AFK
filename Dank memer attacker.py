import pyautogui, time

RED     = '\033[31m'
YELLOWbg  = '\033[43m'
MAGENTA = '\033[35m'
Laps = 0
dot = 0
before_enter=2

Post_meme= 1035, 728
scout= 811,728
high_low= 811, 728


print(RED + "Dank memer.os bot booting up")
print("1", time.sleep(1)) ,print("2", time.sleep(1)), print("3", time.sleep(1)), print("4", time.sleep(1)), print("5", time.sleep(1))

print(MAGENTA + "Started")
while(1):
    time.sleep(1)
    pyautogui.typewrite("pls fish")
    time.sleep(before_enter)
    pyautogui.press("enter")

    pyautogui.typewrite("pls hunt")
    time.sleep(before_enter)
    pyautogui.press("enter")

    pyautogui.typewrite("pls dig")
    time.sleep(before_enter)
    pyautogui.press("enter")

    pyautogui.typewrite("pls beg")
    time.sleep(before_enter)
    pyautogui.press("enter")

    pyautogui.typewrite("pls dep max")
    time.sleep(before_enter)
    pyautogui.press("enter")

    pyautogui.typewrite("pls hl"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(high_low)
    time.sleep(1)

    pyautogui.typewrite("pls pm"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(Post_meme)
    time.sleep(1)

    pyautogui.typewrite("pls scout"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(scout)
    time.sleep(1)

    print("laps")
    Laps + 1
    time.sleep(15)
