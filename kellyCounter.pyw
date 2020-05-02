#Kelly Counter Version 2.1
#Added input for large numbers
from datetime import *
import tkinter as tk

#Variables
oneReturn = 0
twoReturn = 0
threeReturn = 0
onePackage = 0
twoPackage = 0
threePackage = 0
imac = 0
monitor = 0
usbc_hdmi = 0
usbc_dvi = 0
mdp_dvi = 0
mdp_vga = 0
vga = 0
dvi = 0
imac_power = 0
power = 0
ethernet = 0
keyboard = 0
headset = 0
webcam = 0
ipod = 0

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

#Log
def logFunction():
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

#One Return Label
rlBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=rlColor)
rlBox.rowconfigure(0, minsize=60, weight=1)
rlBox.columnconfigure([0,1,2], minsize=60, weight=1)
rlLabel = tk.Label(master=rlBox, text="RL", bg=rlColor, fg='white')
rlCounter = tk.Label(master=rlBox, text=oneReturn, bg=rlColor, fg='white')
def rlPlus():
    global oneReturn
    rlEntry = rlEntryZone.get()
    if len(rlEntry) == 0:
        oneReturn+=1
        rlValue = int(rlCounter["text"])
        rlCounter["text"] = f"{rlValue + 1}"
    elif int(rlEntry) >= 1:
        oneReturn+=int(rlEntry)
        rlValue = int(rlCounter["text"])
        rlCounter["text"] = f"{rlValue + int(rlEntry)}"
    rlEntryZone.delete(first=0, last=10)
    logFunction()
rlPlusButton = tk.Button(master=rlBox, text='+', height=1, width=5, command=rlPlus, bg=rlColor, fg='white')
def rlMinus():
    global oneReturn
    rlEntry = rlEntryZone.get()
    if len(rlEntry) == 0:
        oneReturn-=1
        rlValue = int(rlCounter["text"])
        rlCounter["text"] = f"{rlValue - 1}"
    elif int(rlEntry) >= 1:
        oneReturn-=int(rlEntry)
        rlValue = int(rlCounter["text"])
        rlCounter["text"] = f"{rlValue - int(rlEntry)}"
    rlEntryZone.delete(first=0, last=10)
    logFunction()
rlMinusButton = tk.Button(master=rlBox, text='-', height=1, width=5, command=rlMinus, bg=rlColor, fg='white')
rlEntryZone = tk.Entry(master=rlBox, width=5, justify='center')


rlLabel.grid(row=0, column=1, sticky='nsew')
rlMinusButton.grid(row=1, column=0, sticky='nsew')
rlCounter.grid(row=1, column=1, sticky='nsew')
rlPlusButton.grid(row=1, column=2, sticky='nsew')
rlEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rlBox.grid(row=0, column=0)

#Two Return Labels
rl2Box = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=rlColor)
rl2Box.rowconfigure(0, minsize=60, weight=1)
rl2Box.columnconfigure([0,1,2], minsize=60, weight=1)
two_rlLabel = tk.Label(master=rl2Box, text="2RL", bg=rlColor, fg='white')
two_rlCounter = tk.Label(master=rl2Box, text=twoReturn, bg=rlColor, fg='white')
def two_rlPlus():
    global twoReturn
    two_rlEntry = two_rlEntryZone.get()
    if len(two_rlEntry) == 0:
        twoReturn+=1
        two_rlValue = int(two_rlCounter["text"])
        two_rlCounter["text"] = f"{two_rlValue + 1}"
    elif int(two_rlEntry) >= 1:
        twoReturn+=int(two_rlEntry)
        two_rlValue = int(two_rlCounter["text"])
        two_rlCounter["text"] = f"{two_rlValue + int(two_rlEntry)}"
    two_rlEntryZone.delete(first=0, last=10)
    logFunction()
two_rlPlusButton = tk.Button(master=rl2Box, text='+', height=1, width=5, command=two_rlPlus, bg=rlColor, fg='white')
def two_rlMinus():
    global twoReturn
    rl2Entry = two_rlEntryZone.get()
    if len(rl2Entry) == 0:
        twoReturn-=1
        two_rlValue = int(two_rlCounter["text"])
        two_rlCounter["text"] = f"{two_rlValue - 1}"
    elif int(rl2Entry) >= 1:
        twoReturn-=int(rl2Entry)
        two_rlValue = int(two_rlCounter["text"])
        two_rlCounter["text"] = f"{two_rlValue - int(rl2Entry)}"
    two_rlEntryZone.delete(first=0, last=10)
    logFunction()
two_rlMinusButton = tk.Button(master=rl2Box, text='-', height=1, width=5, command=two_rlMinus, bg=rlColor, fg='white')
two_rlEntryZone = tk.Entry(master=rl2Box, width=5, justify='center')

two_rlLabel.grid(row=0, column=1, sticky='nsew')
two_rlMinusButton.grid(row=1, column=0, sticky='nsew')
two_rlCounter.grid(row=1, column=1, sticky='nsew')
two_rlPlusButton.grid(row=1, column=2, sticky='nsew')
two_rlEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rl2Box.grid(row=1, column=0)

#Three Return Label
rl3Box = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=rlColor)
rl3Box.rowconfigure(0, minsize=60, weight=1)
rl3Box.columnconfigure([0,1,2], minsize=60, weight=1)
three_rlLabel = tk.Label(master=rl3Box, text="3RL", bg=rlColor, fg='white')
three_rlCounter = tk.Label(master=rl3Box, text=threeReturn, bg=rlColor, fg='white')
def three_rlPlus():
    global threeReturn
    three_rlEntry = three_rlEntryZone.get()
    if len(three_rlEntry) == 0:
        threeReturn+=1
        three_rlValue = int(three_rlCounter["text"])
        three_rlCounter["text"] = f"{three_rlValue + 1}"
    elif int(three_rlEntry) >= 1:
        threeReturn+=int(three_rlEntry)
        three_rlValue = int(three_rlCounter["text"])
        three_rlCounter["text"] = f"{three_rlValue + int(three_rlEntry)}"
    three_rlEntryZone.delete(first=0, last=10)
    logFunction()
three_rlPlusButton = tk.Button(master=rl3Box, text='+', height=1, width=5, command=three_rlPlus, bg=rlColor, fg='white')
def three_rlMinus():
    global threeReturn
    threeReturn-=1
    three_rlValue = int(three_rlCounter["text"])
    three_rlCounter["text"] = f"{three_rlValue - 1}"
    logFunction()
three_rlMinusButton = tk.Button(master=rl3Box, text='-', height=1, width=5, command=three_rlMinus, bg=rlColor, fg='white')
three_rlEntryZone = tk.Entry(master=rl3Box, width=5, justify='center')

three_rlLabel.grid(row=0, column=1, sticky='nsew')
three_rlMinusButton.grid(row=1, column=0, sticky='nsew')
three_rlCounter.grid(row=1, column=1, sticky='nsew')
three_rlPlusButton.grid(row=1, column=2, sticky='nsew')
three_rlEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rl3Box.grid(row=2, column=0)

#One Return Label w/ Packaging
rlpBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=rlpColor)
rlpBox.rowconfigure(0, minsize=60, weight=1)
rlpBox.columnconfigure([0,1,2], minsize=60, weight=1)
rlpLabel = tk.Label(master=rlpBox, text="RLP", bg=rlpColor, fg='white')
rlpCounter = tk.Label(master=rlpBox, text=onePackage, bg=rlpColor, fg='white')
def rlpPlus():
    global onePackage
    rlpEntry = rlpEntryZone.get()
    if len(rlpEntry) == 0:
        onePackage+=1
        rlpValue = int(rlpCounter["text"])
        rlpCounter["text"] = f"{rlpValue + 1}"
    elif int(rlpEntry) >= 1:
        onePackage+=int(rlpEntry)
        rlpValue = int(rlpCounter["text"])
        rlpCounter["text"] = f"{rlpValue + int(rlpEntry)}"
    rlpEntryZone.delete(first=0, last=10)
    logFunction()
rlpPlusButton = tk.Button(master=rlpBox, text='+', height=1, width=5, command=rlpPlus, bg=rlpColor, fg='white')
def rlpMinus():
    global onePackage
    rlpEntry = rlpEntryZone.get()
    if len(rlpEntry) == 0:
        onePackage-=1
        rlpValue = int(rlpCounter["text"])
        rlpCounter["text"] = f"{rlpValue - 1}"
    elif int(rlpEntry) >= 1:
        onePackage-=int(rlpEntry)
        rlpValue = int(rlpCounter["text"])
        rlpCounter["text"] = f"{rlpValue - int(rlpEntry)}"
    rlpEntryZone.delete(first=0, last=10)
    logFunction()
rlpMinusButton = tk.Button(master=rlpBox, text='-', height=1, width=5, command=rlpMinus, bg=rlpColor, fg='white')
rlpEntryZone = tk.Entry(master=rlpBox, width=5, justify='center')

rlpLabel.grid(row=0, column=1, sticky='nsew')
rlpMinusButton.grid(row=1, column=0, sticky='nsew')
rlpCounter.grid(row=1, column=1, sticky='nsew')
rlpPlusButton.grid(row=1, column=2, sticky='nsew')
rlpEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rlpBox.grid(row=0, column=1)

#Two Return Label w/ Packaging
rlp2Box = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=rlpColor)
rlp2Box.rowconfigure(0, minsize=60, weight=1)
rlp2Box.columnconfigure([0,1,2], minsize=60, weight=1)
two_rlpLabel = tk.Label(master=rlp2Box, text="2RLP", bg=rlpColor, fg='white')
two_rlpCounter = tk.Label(master=rlp2Box, text=twoPackage, bg=rlpColor, fg='white')
def two_rlpPlus():
    global twoPackage
    two_rlpEntry = two_rlpEntryZone.get()
    if len(two_rlpEntry) == 0:
        twoPackage+=1
        two_rlpValue = int(two_rlpCounter["text"])
        two_rlpCounter["text"] = f"{two_rlpValue + 1}"
    elif int(two_rlpEntry) >= 1:
        twoPackage+=int(two_rlpEntry)
        two_rlpValue = int(two_rlpCounter["text"])
        two_rlpCounter["text"] = f"{two_rlpValue + int(two_rlpEntry)}"
    two_rlpEntryZone.delete(first=0, last=10)
    logFunction()
two_rlpPlusButton = tk.Button(master=rlp2Box, text='+', height=1, width=5, command=two_rlpPlus, bg=rlpColor, fg='white')
def two_rlpMinus():
    global twoPackage
    two_rlpEntry = two_rlpEntryZone.get()
    if len(two_rlpEntry) == 0:
        twoPackage-=1
        two_rlpValue = int(two_rlpCounter["text"])
        two_rlpCounter["text"] = f"{two_rlpValue - 1}"
    elif int(two_rlpEntry) >= 1:
        twoPackage-=int(two_rlpEntry)
        two_rlpValue = int(two_rlpCounter["text"])
        two_rlpCounter["text"] = f"{two_rlpValue - int(two_rlpEntry)}"
    two_rlpEntryZone.delete(first=0, last=10)
    logFunction()
two_rlpMinusButton = tk.Button(master=rlp2Box, text='-', height=1, width=5, command=two_rlpMinus, bg=rlpColor, fg='white')
two_rlpEntryZone = tk.Entry(master=rlp2Box, width=5, justify='center')

two_rlpLabel.grid(row=0, column=1, sticky='nsew')
two_rlpMinusButton.grid(row=1, column=0, sticky='nsew')
two_rlpCounter.grid(row=1, column=1, sticky='nsew')
two_rlpPlusButton.grid(row=1, column=2, sticky='nsew')
two_rlpEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rlp2Box.grid(row=1, column=1)

#Three Return Label w/ Packaging
rlp3Box = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=rlpColor)
rlp3Box.rowconfigure(0, minsize=60, weight=1)
rlp3Box.columnconfigure([0,1,2], minsize=60, weight=1)
three_rlpLabel = tk.Label(master=rlp3Box, text="3RLP", bg=rlpColor, fg='white')
three_rlpCounter = tk.Label(master=rlp3Box, text=threePackage, bg=rlpColor, fg='white')
def three_rlpPlus():
    global threePackage
    three_rlpEntry = three_rlpEntryZone.get()
    if len(three_rlpEntry) == 0:
        threePackage+=1
        three_rlpValue = int(three_rlpCounter["text"])
        three_rlpCounter["text"] = f"{three_rlpValue + 1}"
    elif int(three_rlpEntry) >= 1:
        threePackage+=int(three_rlpEntry)
        three_rlpValue = int(three_rlpCounter["text"])
        three_rlpCounter["text"] = f"{three_rlpValue + int(three_rlpEntry)}"
    three_rlpEntryZone.delete(first=0, last=10)
    logFunction()
three_rlpPlusButton = tk.Button(master=rlp3Box, text='+', height=1, width=5, command=three_rlpPlus, bg=rlpColor, fg='white')
def three_rlpMinus():
    global threePackage
    three_rlpEntry = three_rlpEntryZone.get()
    if len(three_rlpEntry) == 0:
        threePackage-=1
        three_rlpValue = int(three_rlpCounter["text"])
        three_rlpCounter["text"] = f"{three_rlpValue - 1}"
    elif int(three_rlpEntry) >= 1:
        threePackage-=int(three_rlpEntry)
        three_rlpValue = int(three_rlpCounter["text"])
        three_rlpCounter["text"] = f"{three_rlpValue - int(three_rlpEntry)}"
    three_rlpEntryZone.delete(first=0, last=10)
    logFunction()
three_rlpMinusButton = tk.Button(master=rlp3Box, text='-', height=1, width=5, command=three_rlpMinus, bg=rlpColor, fg='white')
three_rlpEntryZone = tk.Entry(master=rlp3Box, width=5, justify='center')

three_rlpLabel.grid(row=0, column=1, sticky='nsew')
three_rlpMinusButton.grid(row=1, column=0, sticky='nsew')
three_rlpCounter.grid(row=1, column=1, sticky='nsew')
three_rlpPlusButton.grid(row=1, column=2, sticky='nsew')
three_rlpEntryZone.grid(row=2, columnspan=3, sticky='nsew')
rlp3Box.grid(row=2, column=1)

#iMac
imacBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=deviceColor)
imacBox.rowconfigure(0, minsize=60, weight=1)
imacBox.columnconfigure([0,1,2], minsize=60, weight=1)
imacLabel = tk.Label(master=imacBox, text="iMac", bg=deviceColor, fg='white')
imacCounter = tk.Label(master=imacBox, text=imac, bg=deviceColor, fg='white')
def imacPlus():
    global imac
    imacEntry = imacEntryZone.get()
    if len(imacEntry) == 0:
        imac+=1
        imacValue = int(imacCounter["text"])
        imacCounter["text"] = f"{imacValue + 1}"
    elif int(imacEntry) >= 1:
        imac+=int(imacEntry)
        imacValue = int(imacCounter["text"])
        imacCounter["text"] = f"{imacValue + int(imacEntry)}"
    imacEntryZone.delete(first=0, last=10)
    logFunction()
imacPlusButton = tk.Button(master=imacBox, text='+', height=1, width=5, command=imacPlus, bg=deviceColor, fg='white')
def imacMinus():
    global imac
    imacEntry = imacEntryZone.get()
    if len(imacEntry) == 0:
        imac-=1
        imacValue = int(imacCounter["text"])
        imacCounter["text"] = f"{imacValue - 1}"
    elif int(imacEntry) >= 1:
        imac-=int(imacEntry)
        imacValue = int(imacCounter["text"])
        imacCounter["text"] = f"{imacValue - int(imacEntry)}"
    imacEntryZone.delete(first=0, last=10)
    logFunction()
imacMinusButton = tk.Button(master=imacBox, text='-', height=1, width=5, command=imacMinus, bg=deviceColor, fg='white')
imacEntryZone = tk.Entry(master=imacBox, width=5, justify='center')

imacLabel.grid(row=0, column=1, sticky='nsew')
imacMinusButton.grid(row=1, column=0, sticky='nsew')
imacCounter.grid(row=1, column=1, sticky='nsew')
imacPlusButton.grid(row=1, column=2, sticky='nsew')
imacEntryZone.grid(row=2, columnspan=3, sticky='nsew')
imacBox.grid(row=0, column=2)

#Monitor
monitorBox = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=deviceColor)
monitorBox.rowconfigure(0, minsize=60, weight=1)
monitorBox.columnconfigure([0,1,2], minsize=60, weight=1)
monitorLabel = tk.Label(master=monitorBox, text="Monitor", bg=deviceColor, fg='white')
monitorCounter = tk.Label(master=monitorBox, text=monitor, bg=deviceColor, fg='white')
def monitorPlus():
    global monitor
    monitorEntry = monitorEntryZone.get()
    if len(monitorEntry) == 0:
        monitor+=1
        monitorValue = int(monitorCounter["text"])
        monitorCounter["text"] = f"{monitorValue + 1}"
    elif int(monitorEntry) >= 1:
        monitor+=int(monitorEntry)
        monitorValue = int(monitorCounter["text"])
        monitorCounter["text"] = f"{monitorValue + int(monitorEntry)}"
    monitorEntryZone.delete(first=0, last=10)
    logFunction()
monitorPlusButton = tk.Button(master=monitorBox, text='+', height=1, width=5, command=monitorPlus, bg=deviceColor, fg='white')
def monitorMinus():
    global monitor
    monitorEntry = monitorEntryZone.get()
    if len(monitorEntry) == 0:
        monitor-=1
        monitorValue = int(monitorCounter["text"])
        monitorCounter["text"] = f"{monitorValue - 1}"
    elif int(monitorEntry) >= 1:
        monitor-=int(monitorEntry)
        monitorValue = int(monitorCounter["text"])
        monitorCounter["text"] = f"{monitorValue - int(monitorEntry)}"
    monitorEntryZone.delete(first=0, last=10)
    logFunction()
monitorMinusButton = tk.Button(master=monitorBox, text='-', height=1, width=5, command=monitorMinus, bg=deviceColor, fg='white')
monitorEntryZone = tk.Entry(master=monitorBox, width=5, justify='center')

monitorLabel.grid(row=0, column=1, sticky='nsew')
monitorMinusButton.grid(row=1, column=0, sticky='nsew')
monitorCounter.grid(row=1, column=1, sticky='nsew')
monitorPlusButton.grid(row=1, column=2, sticky='nsew')
monitorEntryZone.grid(row=2, columnspan=3, sticky='nsew')
monitorBox.grid(row=1, column=2)

#iPod
ipodBox = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=deviceColor)
ipodBox.rowconfigure(0, minsize=60, weight=1)
ipodBox.columnconfigure([0,1,2], minsize=60, weight=1)
ipodLabel = tk.Label(master=ipodBox, text="iPod", bg=deviceColor, fg='white')
ipodCounter = tk.Label(master=ipodBox, text=ipod, bg=deviceColor, fg='white')
def ipodPlus():
    global ipod
    ipodEntry = ipodEntryZone.get()
    if len(ipodEntry) == 0:
        ipod+=1
        ipodValue = int(ipodCounter["text"])
        ipodCounter["text"] = f"{ipodValue + 1}"
    elif int(ipodEntry) >= 1:
        ipod+=int(ipodEntry)
        ipodValue = int(ipodCounter["text"])
        ipodCounter["text"] = f"{ipodValue + int(ipodEntry)}"
    ipodEntryZone.delete(first=0, last=10)
    logFunction()
ipodPlusButton = tk.Button(master=ipodBox, text='+', height=1, width=5, command=ipodPlus, bg=deviceColor, fg='white')
def ipodMinus():
    global ipod
    ipodEntry = ipodEntryZone.get()
    if len(ipodEntry) == 0:
        ipod-=1
        ipodValue = int(ipodCounter["text"])
        ipodCounter["text"] = f"{ipodValue - 1}"
    elif int(ipodEntry) >= 1:
        ipod-=int(ipodEntry)
        ipodValue = int(ipodCounter["text"])
        ipodCounter["text"] = f"{ipodValue - int(ipodEntry)}"
    ipodEntryZone.delete(first=0, last=10)
    logFunction()
ipodMinusButton = tk.Button(master=ipodBox, text='-', height=1, width=5, command=ipodMinus, bg=deviceColor, fg='white')
ipodEntryZone = tk.Entry(master=ipodBox, width=5, justify='center')

ipodLabel.grid(row=0, column=1, sticky='nsew')
ipodMinusButton.grid(row=1, column=0, sticky='nsew')
ipodCounter.grid(row=1, column=1, sticky='nsew')
ipodPlusButton.grid(row=1, column=2, sticky='nsew')
ipodEntryZone.grid(row=2, columnspan=3, sticky='nsew')
ipodBox.grid(row=2, column=2)

#USB-C to HDMI
uhBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=cableColor)
uhBox.rowconfigure(0, minsize=60, weight=1)
uhBox.columnconfigure([0,1,2], minsize=60, weight=1)
usbc_hdmiLabel = tk.Label(master=uhBox, text="USB-C\nHDMI", bg=cableColor, fg='white')
usbc_hdmiCounter = tk.Label(master=uhBox, text=usbc_hdmi, bg=cableColor, fg='white')
def usbc_hdmiPlus():
    global usbc_hdmi
    uhEntry = uhEntryZone.get()
    if len(uhEntry) == 0:
        usbc_hdmi+=1
        uhValue = int(usbc_hdmiCounter["text"])
        usbc_hdmiCounter["text"] = f"{uhValue + 1}"
    elif int(uhEntry) >= 1:
        usbc_hdmi+=int(uhEntry)
        uhValue = int(usbc_hdmiCounter["text"])
        usbc_hdmiCounter["text"] = f"{uhValue + int(uhEntry)}"
    uhEntryZone.delete(first=0, last=10)
    logFunction()
usbc_hdmiPlusButton = tk.Button(master=uhBox, text='+', height=1, width=5, command=usbc_hdmiPlus, bg=cableColor, fg='white')
def usbc_hdmiMinus():
    global usbc_hdmi
    uhEntry = uhEntryZone.get()
    if len(uhEntry) == 0:
        usbc_hdmi-=1
        uhValue = int(usbc_hdmiCounter["text"])
        usbc_hdmiCounter["text"] = f"{uhValue - 1}"
    elif int(uhEntry) >= 1:
        usbc_hdmi-=int(uhEntry)
        uhValue = int(usbc_hdmiCounter["text"])
        usbc_hdmiCounter["text"] = f"{uhValue - int(uhEntry)}"
    uhEntryZone.delete(first=0, last=10)
    logFunction()
usbc_hdmiMinusButton = tk.Button(master=uhBox, text='-', height=1, width=5, command=usbc_hdmiMinus, bg=cableColor, fg='white')
uhEntryZone = tk.Entry(master=uhBox, width=5, justify='center')

usbc_hdmiLabel.grid(row=0, column=1)
usbc_hdmiMinusButton.grid(row=1, column=0, sticky='nsew')
usbc_hdmiCounter.grid(row=1, column=1, sticky='nsew')
usbc_hdmiPlusButton.grid(row=1, column=2, sticky='nsew')
uhEntryZone.grid(row=2, columnspan=3, sticky='nsew')
uhBox.grid(row=0, column=3)

#USB-C to DVI
udBox = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=cableColor)
udBox.rowconfigure(0, minsize=60, weight=1)
udBox.columnconfigure([0,1,2], minsize=60, weight=1)
usbc_dviLabel = tk.Label(master=udBox, text="USB-C\nDVI", bg=cableColor, fg='white')
usbc_dviCounter = tk.Label(master=udBox, text=usbc_dvi, bg=cableColor, fg='white')
def usbc_dviPlus():
    global usbc_dvi
    udEntry = udEntryZone.get()
    if len(udEntry) == 0:
        usbc_dvi+=1
        udValue = int(usbc_dviCounter["text"])
        usbc_dviCounter["text"] = f"{udValue + 1}"
    elif int(udEntry) >= 1:
        usbc_dvi+=int(udEntry)
        udValue = int(usbc_dviCounter["text"])
        usbc_dviCounter["text"] = f"{udValue + int(udEntry)}"
    udEntryZone.delete(first=0, last=10)
    logFunction()
usbc_dviPlusButton = tk.Button(master=udBox, text='+', height=1, width=5, command=usbc_dviPlus, bg=cableColor, fg='white')
def usbc_dviMinus():
    global usbc_dvi
    udEntry = udEntryZone.get()
    if len(udEntry) == 0:
        usbc_dvi-=1
        udValue = int(usbc_dviCounter["text"])
        usbc_dviCounter["text"] = f"{udValue - 1}"
    elif int(udEntry) >= 1:
        usbc_dvi-=int(udEntry)
        udValue = int(usbc_dviCounter["text"])
        usbc_dviCounter["text"] = f"{udValue - int(udEntry)}"
    udEntryZone.delete(first=0, last=10)
    logFunction()
usbc_dviMinusButton = tk.Button(master=udBox, text='-', height=1, width=5, command=usbc_dviMinus, bg=cableColor, fg='white')
udEntryZone = tk.Entry(master=udBox, width=5, justify='center')

usbc_dviLabel.grid(row=0, column=1)
usbc_dviMinusButton.grid(row=1, column=0, sticky='nsew')
usbc_dviCounter.grid(row=1, column=1, sticky='nsew')
usbc_dviPlusButton.grid(row=1, column=2, sticky='nsew')
udEntryZone.grid(row=2, columnspan=3, sticky='nsew')
udBox.grid(row=1, column=3)

#VGA
vgaBox = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=cableColor)
vgaBox.rowconfigure(0, minsize=60, weight=1)
vgaBox.columnconfigure([0,1,2], minsize=60, weight=1)
vgaLabel = tk.Label(master=vgaBox, text="VGA", bg=cableColor, fg='white')
vgaCounter = tk.Label(master=vgaBox, text=vga, bg=cableColor, fg='white')
def vgaPlus():
    global vga
    vgaEntry = vgaEntryZone.get()
    if len(vgaEntry) == 0:
        vga+=1
        vgaValue = int(vgaCounter["text"])
        vgaCounter["text"] = f"{vgaValue + 1}"
    elif int(vgaEntry) >= 1:
        vga+=int(vgaEntry)
        vgaValue = int(vgaCounter["text"])
        vgaCounter["text"] = f"{vgaValue + int(vgaEntry)}"
    vgaEntryZone.delete(first=0, last=10)
    logFunction()
vgaPlusButton = tk.Button(master=vgaBox, text='+', height=1, width=5, command=vgaPlus, bg=cableColor, fg='white')
def vgaMinus():
    global vga
    vgaEntry = vgaEntryZone.get()
    if len(vgaEntry) == 0:
        vga-=1
        vgaValue = int(vgaCounter["text"])
        vgaCounter["text"] = f"{vgaValue - 1}"
    elif int(vgaEntry) >= 1:
        vga-=int(vgaEntry)
        vgaValue = int(vgaCounter["text"])
        vgaCounter["text"] = f"{vgaValue - int(vgaEntry)}"
    vgaEntryZone.delete(first=0, last=10)
    logFunction()
vgaMinusButton = tk.Button(master=vgaBox, text='-', height=1, width=5, command=vgaMinus, bg=cableColor, fg='white')
vgaEntryZone = tk.Entry(master=vgaBox, width=5, justify='center')

vgaLabel.grid(row=0, column=1)
vgaMinusButton.grid(row=1, column=0, sticky='nsew')
vgaCounter.grid(row=1, column=1, sticky='nsew')
vgaPlusButton.grid(row=1, column=2, sticky='nsew')
vgaEntryZone.grid(row=2, columnspan=3, sticky='nsew')
vgaBox.grid(row=2, column=3)

#MDP to DVI
mdp_dviBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=cableColor)
mdp_dviBox.rowconfigure(0, minsize=60, weight=1)
mdp_dviBox.columnconfigure([0,1,2], minsize=60, weight=1)
mdp_dviLabel = tk.Label(master=mdp_dviBox, text="MDP\nDVI", bg=cableColor, fg='white')
mdp_dviCounter = tk.Label(master=mdp_dviBox, text=mdp_dvi, bg=cableColor, fg='white')
def mdp_dviPlus():
    global mdp_dvi
    mdp_dviEntry = mdp_dviEntryZone.get()
    if len(mdp_dviEntry) == 0:
        mdp_dvi+=1
        mdp_dviValue = int(mdp_dviCounter["text"])
        mdp_dviCounter["text"] = f"{mdp_dviValue + 1}"
    elif int(mdp_dviEntry) >= 1:
        mdp_dvi+=int(mdp_dviEntry)
        mdp_dviValue = int(mdp_dviCounter["text"])
        mdp_dviCounter["text"] = f"{mdp_dviValue + int(mdp_dviEntry)}"
    mdp_dviEntryZone.delete(first=0, last=10)
    logFunction()
mdp_dviPlusButton = tk.Button(master=mdp_dviBox, text='+', height=1, width=5, command=mdp_dviPlus, bg=cableColor, fg='white')
def mdp_dviMinus():
    global mdp_dvi
    mdp_dviEntry = mdp_dviEntryZone.get()
    if len(mdp_dviEntry) == 0:
        mdp_dvi-=1
        mdp_dviValue = int(mdp_dviCounter["text"])
        mdp_dviCounter["text"] = f"{mdp_dviValue - 1}"
    elif int(mdp_dviEntry) >= 1:
        mdp_dvi-=int(mdp_dviEntry)
        mdp_dviValue = int(mdp_dviCounter["text"])
        mdp_dviCounter["text"] = f"{mdp_dviValue - int(mdp_dviEntry)}"
    mdp_dviEntryZone.delete(first=0, last=10)
    logFunction()
mdp_dviMinusButton = tk.Button(master=mdp_dviBox, text='-', height=1, width=5, command=mdp_dviMinus, bg=cableColor, fg='white')
mdp_dviEntryZone = tk.Entry(master=mdp_dviBox, width=5, justify='center')

mdp_dviLabel.grid(row=0, column=1)
mdp_dviMinusButton.grid(row=1, column=0, sticky='nsew')
mdp_dviCounter.grid(row=1, column=1, sticky='nsew')
mdp_dviPlusButton.grid(row=1, column=2, sticky='nsew')
mdp_dviEntryZone.grid(row=2, columnspan=3, sticky='nsew')
mdp_dviBox.grid(row=0, column=4)

#MDP to VGA
mdp_vgaBox = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=cableColor)
mdp_vgaBox.rowconfigure(0, minsize=60, weight=1)
mdp_vgaBox.columnconfigure([0,1,2], minsize=60, weight=1)
mdp_vgaLabel = tk.Label(master=mdp_vgaBox, text="MDP\nVGA", bg=cableColor, fg='white')
mdp_vgaCounter = tk.Label(master=mdp_vgaBox, text=mdp_vga, bg=cableColor, fg='white')
def mdp_vgaPlus():
    global mdp_vga
    mdp_vgaEntry = mdp_vgaEntryZone.get()
    if len(mdp_vgaEntry) == 0:
        mdp_vga+=1
        mdp_vgaValue = int(mdp_vgaCounter["text"])
        mdp_vgaCounter["text"] = f"{mdp_vgaValue + 1}"
    elif int(mdp_vgaEntry) >= 1:
        mdp_vga+=int(mdp_vgaEntry)
        mdp_vgaValue = int(mdp_vgaCounter["text"])
        mdp_vgaCounter["text"] = f"{mdp_vgaValue + int(mdp_vgaEntry)}"
    mdp_vgaEntryZone.delete(first=0, last=10)
    logFunction()
mdp_vgaPlusButton = tk.Button(master=mdp_vgaBox, text='+', height=1, width=5, command=mdp_vgaPlus, bg=cableColor, fg='white')
def mdp_vgaMinus():
    global mdp_vga
    mdp_vgaEntry = mdp_vgaEntryZone.get()
    if len(mdp_vgaEntry) == 0:
        mdp_vga-=1
        mdp_vgaValue = int(mdp_vgaCounter["text"])
        mdp_vgaCounter["text"] = f"{mdp_vgaValue - 1}"
    elif int(mdp_vgaEntry) >= 1:
        mdp_vga-=int(mdp_vgaEntry)
        mdp_vgaValue = int(mdp_vgaCounter["text"])
        mdp_vgaCounter["text"] = f"{mdp_vgaValue - int(mdp_vgaEntry)}"
    mdp_vgaEntryZone.delete(first=0, last=10)
    logFunction()
mdp_vgaMinusButton = tk.Button(master=mdp_vgaBox, text='-', height=1, width=5, command=mdp_vgaMinus, bg=cableColor, fg='white')
mdp_vgaEntryZone = tk.Entry(master=mdp_vgaBox, width=5, justify='center')

mdp_vgaLabel.grid(row=0, column=1)
mdp_vgaMinusButton.grid(row=1, column=0, sticky='nsew')
mdp_vgaCounter.grid(row=1, column=1, sticky='nsew')
mdp_vgaPlusButton.grid(row=1, column=2, sticky='nsew')
mdp_vgaEntryZone.grid(row=2, columnspan=3, sticky='nsew')
mdp_vgaBox.grid(row=1, column=4)

#DVI
dviBox = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=cableColor)
dviBox.rowconfigure(0, minsize=60, weight=1)
dviBox.columnconfigure([0,1,2], minsize=60, weight=1)
dviLabel = tk.Label(master=dviBox, text="DVI", bg=cableColor, fg='white')
dviCounter = tk.Label(master=dviBox, text=dvi, bg=cableColor, fg='white')
def dviPlus():
    global dvi
    dviEntry = dviEntryZone.get()
    if len(dviEntry) == 0:
        dvi+=1
        dviValue = int(dviCounter["text"])
        dviCounter["text"] = f"{dviValue + 1}"
    elif int(dviEntry) >= 1:
        dvi+=int(dviEntry)
        dviValue = int(dviCounter["text"])
        dviCounter["text"] = f"{dviValue + int(dviEntry)}"
    dviEntryZone.delete(first=0, last=10)
    logFunction()
dviPlusButton = tk.Button(master=dviBox, text='+', height=1, width=5, command=dviPlus, bg=cableColor, fg='white')
def dviMinus():
    global dvi
    dviEntry = dviEntryZone.get()
    if len(dviEntry) == 0:
        dvi-=1
        dviValue = int(dviCounter["text"])
        dviCounter["text"] = f"{dviValue - 1}"
    elif int(dviEntry) >= 1:
        dvi-=int(dviEntry)
        dviValue = int(dviCounter["text"])
        dviCounter["text"] = f"{dviValue - int(dviEntry)}"
    dviEntryZone.delete(first=0, last=10)
    logFunction()
dviMinusButton = tk.Button(master=dviBox, text='-', height=1, width=5, command=dviMinus, bg=cableColor, fg='white')
dviEntryZone = tk.Entry(master=dviBox, width=5, justify='center')

dviLabel.grid(row=0, column=1)
dviMinusButton.grid(row=1, column=0, sticky='nsew')
dviCounter.grid(row=1, column=1, sticky='nsew')
dviPlusButton.grid(row=1, column=2, sticky='nsew')
dviEntryZone.grid(row=2, columnspan=3, sticky='nsew')
dviBox.grid(row=2, column=4)

#iMac Power Cable
imac_powerBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=cableColor)
imac_powerBox.rowconfigure(0, minsize=60, weight=1)
imac_powerBox.columnconfigure([0,1,2], minsize=60, weight=1)
imac_powerLabel = tk.Label(master=imac_powerBox, text="iMac\nPower", bg=cableColor, fg='white')
imac_powerCounter = tk.Label(master=imac_powerBox, text=imac_power, bg=cableColor, fg='white')
def imac_powerPlus():
    global imac_power
    imac_powerEntry = imac_powerEntryZone.get()
    if len(imac_powerEntry) == 0:
        imac_power+=1
        imac_powerValue = int(imac_powerCounter["text"])
        imac_powerCounter["text"] = f"{imac_powerValue + 1}"
    elif int(imac_powerEntry) >= 1:
        imac_power+=int(imac_powerEntry)
        imac_powerValue = int(imac_powerCounter["text"])
        imac_powerCounter["text"] = f"{imac_powerValue + int(imac_powerEntry)}"
    imac_powerEntryZone.delete(first=0, last=10)
    logFunction()
imac_powerPlusButton = tk.Button(master=imac_powerBox, text='+', height=1, width=5, command=imac_powerPlus, bg=cableColor, fg='white')
def imac_powerMinus():
    global imac_power
    imac_powerEntry = imac_powerEntryZone.get()
    if len(imac_powerEntry) == 0:
        imac_power-=1
        imac_powerValue = int(imac_powerCounter["text"])
        imac_powerCounter["text"] = f"{imac_powerValue - 1}"
    elif int(imac_powerEntry) >= 1:
        imac_power-=int(imac_powerEntry)
        imac_powerValue = int(imac_powerCounter["text"])
        imac_powerCounter["text"] = f"{imac_powerValue - int(imac_powerEntry)}"
    imac_powerEntryZone.delete(first=0, last=10)
    logFunction()
imac_powerMinusButton = tk.Button(master=imac_powerBox, text='-', height=1, width=5, command=imac_powerMinus, bg=cableColor, fg='white')
imac_powerEntryZone = tk.Entry(master=imac_powerBox, width=5, justify='center')

imac_powerLabel.grid(row=0, column=1)
imac_powerMinusButton.grid(row=1, column=0, sticky='nsew')
imac_powerCounter.grid(row=1, column=1, sticky='nsew')
imac_powerPlusButton.grid(row=1, column=2, sticky='nsew')
imac_powerEntryZone.grid(row=2, columnspan=3, sticky='nsew')
imac_powerBox.grid(row=0, column=5)

#Cat5
ethernetBox = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=cableColor)
ethernetBox.rowconfigure(0, minsize=60, weight=1)
ethernetBox.columnconfigure([0,1,2], minsize=60, weight=1)
ethernetLabel = tk.Label(master=ethernetBox, text="Cat5", bg=cableColor, fg='white')
ethernetCounter = tk.Label(master=ethernetBox, text=ethernet, bg=cableColor, fg='white')
def ethernetPlus():
    global ethernet
    ethernetEntry = ethernetEntryZone.get()
    if len(ethernetEntry) == 0:
        ethernet+=1
        ethernetValue = int(ethernetCounter["text"])
        ethernetCounter["text"] = f"{ethernetValue + 1}"
    elif int(ethernetEntry) >= 1:
        ethernet+=int(ethernetEntry)
        ethernetValue = int(ethernetCounter["text"])
        ethernetCounter["text"] = f"{ethernetValue + int(ethernetEntry)}"
    ethernetEntryZone.delete(first=0, last=10)
    logFunction()
ethernetPlusButton = tk.Button(master=ethernetBox, text='+', height=1, width=5, command=ethernetPlus, bg=cableColor, fg='white')
def ethernetMinus():
    global ethernet
    ethernetEntry = ethernetEntryZone.get()
    if len(ethernetEntry) == 0:
        ethernet-=1
        ethernetValue = int(ethernetCounter["text"])
        ethernetCounter["text"] = f"{ethernetValue - 1}"
    elif int(ethernetEntry) >= 1:
        ethernet-=int(ethernetEntry)
        ethernetValue = int(ethernetCounter["text"])
        ethernetCounter["text"] = f"{ethernetValue - int(ethernetEntry)}"
    ethernetEntryZone.delete(first=0, last=10)
    logFunction()
ethernetMinusButton = tk.Button(master=ethernetBox, text='-', height=1, width=5, command=ethernetMinus, bg=cableColor, fg='white')
ethernetEntryZone = tk.Entry(master=ethernetBox, width=5, justify='center')

ethernetLabel.grid(row=0, column=1)
ethernetMinusButton.grid(row=1, column=0, sticky='nsew')
ethernetCounter.grid(row=1, column=1, sticky='nsew')
ethernetPlusButton.grid(row=1, column=2, sticky='nsew')
ethernetEntryZone.grid(row=2, columnspan=3, sticky='nsew')
ethernetBox.grid(row=1, column=5)

#Headset
headsetBox = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=accessColor)
headsetBox.rowconfigure(0, minsize=60, weight=1)
headsetBox.columnconfigure([0,1,2], minsize=60, weight=1)
headsetLabel = tk.Label(master=headsetBox, text="Headset", bg=accessColor, fg='white')
headsetCounter = tk.Label(master=headsetBox, text=headset, bg=accessColor, fg='white')
def headsetPlus():
    global headset
    headsetEntry = headsetEntryZone.get()
    if len(headsetEntry) == 0:
        headset+=1
        headsetValue = int(headsetCounter["text"])
        headsetCounter["text"] = f"{headsetValue + 1}"
    elif int(headsetEntry) >= 1:
        headset+=int(headsetEntry)
        headsetValue = int(headsetCounter["text"])
        headsetCounter["text"] = f"{headsetValue + int(headsetEntry)}"
    headsetEntryZone.delete(first=0, last=10)
    logFunction()
headsetPlusButton = tk.Button(master=headsetBox, text='+', height=1, width=5, command=headsetPlus, bg=accessColor, fg='white')
def headsetMinus():
    global headset
    headsetEntry = headsetEntryZone.get()
    if len(headsetEntry) == 0:
        headset-=1
        headsetValue = int(headsetCounter["text"])
        headsetCounter["text"] = f"{headsetValue - 1}"
    elif int(headsetEntry) >= 1:
        headset-=int(headsetEntry)
        headsetValue = int(headsetCounter["text"])
        headsetCounter["text"] = f"{headsetValue - int(headsetEntry)}"
    headsetEntryZone.delete(first=0, last=10)
    logFunction()
headsetMinusButton = tk.Button(master=headsetBox, text='-', height=1, width=5, command=headsetMinus, bg=accessColor, fg='white')
headsetEntryZone = tk.Entry(master=headsetBox, width=5, justify='center')

headsetLabel.grid(row=0, column=1)
headsetMinusButton.grid(row=1, column=0, sticky='nsew')
headsetCounter.grid(row=1, column=1, sticky='nsew')
headsetPlusButton.grid(row=1, column=2, sticky='nsew')
headsetEntryZone.grid(row=2, columnspan=3, sticky='nsew')
headsetBox.grid(row=2, column=5)

#Power Cable
powerBox = tk.Frame(master=row_zero, borderwidth=1, padx=5, pady=5, bg=accessColor)
powerBox.rowconfigure(0, minsize=60, weight=1)
powerBox.columnconfigure([0,1,2], minsize=60, weight=1)
powerLabel = tk.Label(master=powerBox, text="Power\nCable", bg=accessColor, fg='white')
powerCounter = tk.Label(master=powerBox, text=power, bg=accessColor, fg='white')
def powerPlus():
    global power
    powerEntry = powerEntryZone.get()
    if len(powerEntry) == 0:
        power+=1
        powerValue = int(powerCounter["text"])
        powerCounter["text"] = f"{powerValue + 1}"
    elif int(powerEntry) >= 1:
        power+=int(powerEntry)
        powerValue = int(powerCounter["text"])
        powerCounter["text"] = f"{powerValue + int(powerEntry)}"
    powerEntryZone.delete(first=0, last=10)
    logFunction()
powerPlusButton = tk.Button(master=powerBox, text='+', height=1, width=5, command=powerPlus, bg=accessColor, fg='white')
def powerMinus():
    global power
    powerEntry = powerEntryZone.get()
    if len(powerEntry) == 0:
        power-=1
        powerValue = int(powerCounter["text"])
        powerCounter["text"] = f"{powerValue - 1}"
    elif int(powerEntry) >= 1:
        power-=int(powerEntry)
        powerValue = int(powerCounter["text"])
        powerCounter["text"] = f"{powerValue - int(powerEntry)}"
    powerEntryZone.delete(first=0, last=10)
    logFunction()
powerMinusButton = tk.Button(master=powerBox, text='-', height=1, width=5, command=powerMinus, bg=accessColor, fg='white')
powerEntryZone = tk.Entry(master=powerBox, width=5, justify='center')

powerLabel.grid(row=0, column=1)
powerMinusButton.grid(row=1, column=0, sticky='nsew')
powerCounter.grid(row=1, column=1, sticky='nsew')
powerPlusButton.grid(row=1, column=2, sticky='nsew')
powerEntryZone.grid(row=2, columnspan=3, sticky='nsew')
powerBox.grid(row=0, column=6)

#Keyboard/Mouse
keyboardBox = tk.Frame(master=row_one, borderwidth=1, padx=5, pady=5, bg=accessColor)
keyboardBox.rowconfigure(0, minsize=60, weight=1)
keyboardBox.columnconfigure([0,1,2], minsize=60, weight=1)
keyboardLabel = tk.Label(master=keyboardBox, text="Keyboard", bg=accessColor, fg='white')
keyboardCounter = tk.Label(master=keyboardBox, text=keyboard, bg=accessColor, fg='white')
def keyboardPlus():
    global keyboard
    keyboardEntry = keyboardEntryZone.get()
    if len(keyboardEntry) == 0:
        keyboard+=1
        keyboardValue = int(keyboardCounter["text"])
        keyboardCounter["text"] = f"{keyboardValue + 1}"
    elif int(keyboardEntry) >= 1:
        keyboard+=int(keyboardEntry)
        keyboardValue = int(keyboardCounter["text"])
        keyboardCounter["text"] = f"{keyboardValue + int(keyboardEntry)}"
    keyboardEntryZone.delete(first=0, last=10)
    logFunction()
keyboardPlusButton = tk.Button(master=keyboardBox, text='+', height=1, width=5, command=keyboardPlus, bg=accessColor, fg='white')
def keyboardMinus():
    global keyboard
    keyboardEntry = keyboardEntryZone.get()
    if len(keyboardEntry) == 0:
        keyboard-=1
        keyboardValue = int(keyboardCounter["text"])
        keyboardCounter["text"] = f"{keyboardValue - 1}"
    elif int(keyboardEntry) >= 1:
        keyboard-=int(keyboardEntry)
        keyboardValue = int(keyboardCounter["text"])
        keyboardCounter["text"] = f"{keyboardValue - int(keyboardEntry)}"
    keyboardEntryZone.delete(first=0, last=10)
    logFunction()
keyboardMinusButton = tk.Button(master=keyboardBox, text='-', height=1, width=5, command=keyboardMinus, bg=accessColor, fg='white')
keyboardEntryZone = tk.Entry(master=keyboardBox, width=5, justify='center')

keyboardLabel.grid(row=0, column=1)
keyboardMinusButton.grid(row=1, column=0, sticky='nsew')
keyboardCounter.grid(row=1, column=1, sticky='nsew')
keyboardPlusButton.grid(row=1, column=2, sticky='nsew')
keyboardEntryZone.grid(row=2, columnspan=3, sticky='nsew')
keyboardBox.grid(row=1, column=6)

#Webcam
webcamBox = tk.Frame(master=row_two, borderwidth=1, padx=5, pady=5, bg=accessColor)
webcamBox.rowconfigure(0, minsize=60, weight=1)
webcamBox.columnconfigure([0,1,2], minsize=60, weight=1)
webcamLabel = tk.Label(master=webcamBox, text="Webcam", bg=accessColor, fg='white')
webcamCounter = tk.Label(master=webcamBox, text=webcam, bg=accessColor, fg='white')
def webcamPlus():
    global webcam
    webcamEntry = webcamEntryZone.get()
    if len(webcamEntry) == 0:
        webcam+=1
        webcamValue = int(webcamCounter["text"])
        webcamCounter["text"] = f"{webcamValue + 1}"
    elif int(webcamEntry) >= 1:
        webcam+=int(webcamEntry)
        webcamValue = int(webcamCounter["text"])
        webcamCounter["text"] = f"{webcamValue + int(webcamEntry)}"
    webcamEntryZone.delete(first=0, last=10)
    logFunction()
webcamPlusButton = tk.Button(master=webcamBox, text='+', height=1, width=5, command=webcamPlus, bg=accessColor, fg='white')
def webcamMinus():
    global webcam
    webcamEntry = webcamEntryZone.get()
    if len(webcamEntry) == 0:
        webcam-=1
        webcamValue = int(webcamCounter["text"])
        webcamCounter["text"] = f"{webcamValue - 1}"
    elif int(webcamEntry) >= 1:
        webcam-=int(webcamEntry)
        webcamValue = int(webcamCounter["text"])
        webcamCounter["text"] = f"{webcamValue - int(webcamEntry)}"
    webcamEntryZone.delete(first=0, last=10)
    logFunction()
webcamMinusButton = tk.Button(master=webcamBox, text='-', height=1, width=5, command=webcamMinus, bg=accessColor, fg='white')
webcamEntryZone = tk.Entry(master=webcamBox, width=5, justify='center')

webcamLabel.grid(row=0, column=1)
webcamMinusButton.grid(row=1, column=0, sticky='nsew')
webcamCounter.grid(row=1, column=1, sticky='nsew')
webcamPlusButton.grid(row=1, column=2, sticky='nsew')
webcamEntryZone.grid(row=2, columnspan=3, sticky='nsew')
webcamBox.grid(row=2, column=6)

row_zero.grid(row=0)
row_one.grid(row=1)
row_two.grid(row=2)
window.mainloop()