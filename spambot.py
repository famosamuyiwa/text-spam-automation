import pyautogui, time
time.sleep(20)


f = open("beescript", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(5)


