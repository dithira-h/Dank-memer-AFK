#this is only for educational purposes only :D
#this is not meant to attack dank memer or to break it :)
#TYPE pip install pyautogui IN YOUR TERMINAL
import pyautogui, time

RED     = '\033[31m'  #the hex color codes for python
YELLOWbg  = '\033[43m' #the hex color codes for python
MAGENTA = '\033[35m' #the hex color codes for python
Laps = 0
dot = 0
before_enter=2 #the variable delay before pressing the enter button

Post_meme= 1035, 728 #this variables are tp be chaged when the discord window position changes according to the button positions
scout= 811,728 #this variables are tp be chaged when the discord window position changes according to the button positions
high_low= 811, 728 #this variables are tp be chaged when the discord window position changes according to the button positions


print(RED + "Dank memer.os bot booting up") #to enhance the terminal 
print("1", time.sleep(1)) ,print("2", time.sleep(1)), print("3", time.sleep(1)), print("4", time.sleep(1)), print("5", time.sleep(1)) #to enhance the terminal 

print(MAGENTA + "Started") #to enhance the terminal 
while(1):
    #fish command
    time.sleep(1)
    pyautogui.typewrite("pls fish")
    time.sleep(before_enter)
    pyautogui.press("enter")

    #hunt command
    pyautogui.typewrite("pls hunt")
    time.sleep(before_enter)
    pyautogui.press("enter")

    #dig command
    pyautogui.typewrite("pls dig")
    time.sleep(before_enter)
    pyautogui.press("enter")

    #beg command
    pyautogui.typewrite("pls beg")
    time.sleep(before_enter)
    pyautogui.press("enter")

    #deposit command
    pyautogui.typewrite("pls dep max")
    time.sleep(before_enter)
    pyautogui.press("enter")

    #high low command
    pyautogui.typewrite("pls hl"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(high_low) #the location of the button from the discord window(has to be re-generated every time the discord window position changes)
    time.sleep(1)

    #postmeme command
    pyautogui.typewrite("pls pm"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(Post_meme) #the location of the button from the discord window(has to be re-generated every time the discord window position changes)
    time.sleep(1)

    #scout command
    pyautogui.typewrite("pls scout"), pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(scout) #the location of the button from the discord window(has to be re-generated every time the discord window position changes)
    time.sleep(1)

    #the lap counter
    print("laps")
    Laps + 1
    time.sleep(15) #this time is nessary to not get 'take a break' messages for dank memer
