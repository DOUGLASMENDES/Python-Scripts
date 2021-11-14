import pyautogui as pag

#im1 = pag.screenshot()
#im2 = pag.screenshot('my_screenshot.png')


im = pag.screenshot(region=(0,0, 300, 400))
im.save('teste.png')