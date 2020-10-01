import time
import pyautogui

def pressx(string):
    for x in string:
        pyautogui.press(x)

def router1():
    pyautogui.click(100,1050)
    pressx("CMD")
    pyautogui.press("enter")
    time.sleep(0.01)
    pressx("netsh")
    pyautogui.press("enter")
    pressx("wlan")
    pyautogui.press("enter")
    pressx("connect name=(YOUR ROUTERNAME1)")
    pyautogui.press("enter")
    pressx("exit")
    pyautogui.press("enter")
    pressx("exit")
    pyautogui.press("enter")

def router2():
    pyautogui.click(100,1050)
    pressx("CMD")
    pyautogui.press("enter")
    time.sleep(0.01)
    pressx("netsh")
    pyautogui.press("enter")
    pressx("wlan")
    pyautogui.press("enter")
    pressx("connect name=(YOUR ROUTERNAME2)")
    pyautogui.press("enter")
    pressx("exit")
    pyautogui.press("enter")
    pressx("exit")
    pyautogui.press("enter")

while True:
    t = time.localtime()
    current_time = time.strftime("%H", t)
    if int(current_time) == 7:
        router1()
    elif int(current_time) == 14:
        router2()
    time.sleep(500)