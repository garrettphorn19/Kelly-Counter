#Kelly Counter Version 2.2
#Added OOP
from datetime import *
import tkinter as tk
from classes.product import Product

#Date/Time
today = date.today()
longDate = today.strftime("%B %d, %Y")
shortDate = today.strftime("%m-%d")
fileName = 'kellyLog' + shortDate

#Colors
rlColor = '#021C1E'
rlpColor = '#004445'
deviceColor = '#2C7873'
cableColor = '#6FB98F'
accessColor = '#78E3A6'

window = tk.Tk() #Starts a window for the program
window.title('Kelly Counter')

#Row Frames
#Used to categorize the rows of products
row_zero = tk.Frame()
row_one = tk.Frame()
row_two = tk.Frame()	

#Creating each Product
rlClass = Product("RL", rlColor, row_zero, 0)
two_rlClass = Product("2RL", rlColor, row_one, 0)
three_rlClass = Product("3RL", rlColor, row_two, 0)

rlpClass = Product("RLP", rlpColor, row_zero, 1)
two_rlpClass = Product("2RLP", rlpColor, row_one, 1)
three_rlpClass = Product("3RLP", rlpColor, row_two, 1)

iMacClass = Product("iMac", deviceColor, row_zero, 2)
monitorClass = Product("Monitor", deviceColor, row_one, 2)
ipodClass = Product("iPod", deviceColor, row_two, 2)

usbc_hdmiClass  = Product("USBC\nHDMI", cableColor, row_zero, 3)
usbc_dviClass = Product("USBC\nDVI", cableColor, row_one, 3)
dviClass = Product("DVI", cableColor, row_two, 3)

mdp_dviClass = Product("MDP\nDVI", cableColor, row_zero, 4)
mdp_vgaClass = Product("MDP\nVGA", cableColor, row_one, 4)
vgaClass = Product("VGA", cableColor, row_two, 4)

imac_powerClass = Product("iMac\nPower", cableColor, row_zero, 5)
powerClass = Product("Power", cableColor, row_one, 5)
ethernetClass = Product("Ethernet", cableColor, row_two, 5)

keyboardClass = Product("Keyboard", accessColor, row_zero, 6)
headsetClass = Product("Headset", accessColor, row_one, 6)
webcamClass = Product("Webcam", accessColor, row_two, 6)

#Places each row into the main window
row_zero.grid(row=0)
row_one.grid(row=1)
row_two.grid(row=2)
window.mainloop()