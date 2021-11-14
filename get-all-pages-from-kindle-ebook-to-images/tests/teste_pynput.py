from pynput.mouse import Button, Controller
 
mouse = Controller()

# left-click
mouse.press(Button.left)
 
# right-click
mouse.press(Button.right)

mouse.move(50, -50)
 
mouse.move(100, -200)
#pynput can control the keyboard, as well. To do that, we need to import the Key class


from pynput.keyboard import Key
#To make your keyboard type, you can use the aptly-named keyboard.type method.

keyboard.type("this is a test")