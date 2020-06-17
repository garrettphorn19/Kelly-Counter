#Kelly Counter Version 2.2
#Added OOP
from datetime import *
import tkinter as tk

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

window = tk.Tk()
window.title('Kelly Counter')

#Row Frames
row_zero = tk.Frame()
row_one = tk.Frame()
row_two = tk.Frame()

def logFunction():
	oneReturn = rlClass.amount
	twoReturn = two_rlClass.amount
	threeReturn = three_rlClass.amount
	onePackage = rlpClass.amount
	twoPackage = two_rlpClass.amount
	threePackage = three_rlpClass.amount
	imac = iMacClass.amount
	monitor = monitorClass.amount
	usbc_hdmi = usbc_hdmiClass.amount
	usbc_dvi = usbc_dviClass.amount
	mdp_dvi = mdp_dviClass.amount
	mdp_vga = mdp_vgaClass.amount
	vga = vgaClass.amount
	dvi = dviClass.amount
	imac_power = imac_powerClass.amount
	power = powerClass.amount
	ethernet = ethernetClass.amount
	keyboard = keyboardClass.amount
	headset = headsetClass.amount
	webcam = webcamClass.amount
	ipod = ipodClass.amount

	sumPackage = onePackage + twoPackage + threePackage
	sumReturn = oneReturn + twoReturn + threeReturn
	
	file = open(fileName + '.txt','w+')
	file.write('Shipping Log for ' + longDate)
	if imac > 0:
		file.write('\niMac: ' + str(imac))
	if sumReturn > 0:
		file.write('\nReturn Labels: ' + str(sumReturn))
	if sumPackage > 0:
		file.write('\nReturn Labels w/ Packaging: ' + str(sumPackage))
	if monitor > 0:
		file.write('\nMonitors: ' + str(monitor))
	if ipod > 0:
		file.write('\niPod: ' + str(ipod))
	if usbc_hdmi > 0:
		file.write('\nUSB-C to HDMI: ' + str(usbc_hdmi))
	if usbc_dvi > 0:
		file.write('\nUSB-C to DVI: ' + str(usbc_dvi))
	if mdp_dvi > 0:
		file.write('\nMDP to DVI: ' + str(mdp_dvi))
	if mdp_vga > 0:
		file.write('\nMDP to VGA: ' + str(mdp_vga))
	if vga > 0:
		file.write('\nVGA: ' + str(vga))
	if dvi > 0:
		file.write('\nDVI: ' + str(dvi))
	if imac_power > 0:
		file.write('\niMac Power Cable: ' + str(imac_power))
	if power > 0:
		file.write('\nPower Cable: ' + str(power))
	if ethernet > 0:
		file.write('\nCat5: ' + str(ethernet))
	if keyboard > 0:
		file.write('\nKeyboard/Mouse: ' + str(keyboard))
	if headset > 0:
		file.write('\nHeadset: ' + str(headset))
	if webcam > 0:
		file.write('\nWebcam: ' + str(webcam))
	file.close()

class Product:
	def __init__(self, label, color, master_row, column):
		self.label = label
		self.color = color
		self.master_row = master_row
		self.column = column
		self.amount=0
		self.__makeBox(self.label, self.color, self.master_row, self.column, self.amount)

	def __makeBox(self, label, color, master_row, column, amount):
		box = tk.Frame(master=self.master_row, borderwidth=1, padx=5, pady=5, bg=self.color)
		box.rowconfigure(0, minsize=60, weight=1)
		box.columnconfigure([0,1,2], minsize=60, weight=1)
		label = tk.Label(master=box, text=self.label, bg=self.color, fg="white")
		counter = tk.Label(master=box, text=self.amount, bg=self.color, fg="white")
		entryZone = tk.Entry(master=box, width=5, justify="center")
		def __plus():
			entry = entryZone.get()
			if len(entry) == 0:
				self.amount+=1
				value = int(counter["text"])
				counter["text"] = f"{value + 1}"
			elif int(entry) >= 1:
				self.amount+=int(entry)
				value = int(counter["text"])
				counter["text"] = f"{value + int(entry)}"
			entryZone.delete(first=0, last=100)
		plusButton = tk.Button(master=box, text="+", height=1, width=5, command=__plus, bg=self.color, fg="white")
		def __minus():
			entry = entryZone.get()
			if len(entry) == 0:
				self.amount-=1
				value = int(counter["text"])
				counter["text"] = f"{value - 1}"
			elif int(entry) >= 1:
				self.amount-=int(entry)
				value = int(counter["text"])
				counter["text"] = f"{value - int(entry)}"
			entryZone.delete(first=0, last=100)
		minusButton = tk.Button(master=box, text="-", height=1, width=5, command=__minus, bg=self.color, fg="white")

		label.grid(row=0, column=1, sticky="nsew")
		minusButton.grid(row=1, column=0, sticky="nsew")
		counter.grid(row=1, column=1, sticky="nsew")
		plusButton.grid(row=1, column=2, sticky="nsew")
		entryZone.grid(row=2, columnspan=3, sticky="nsew")
		box.grid(row=0, column=self.column)		

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

row_zero.grid(row=0)
row_one.grid(row=1)
row_two.grid(row=2)
window.mainloop()

logFunction()