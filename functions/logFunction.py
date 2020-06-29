from classes.product import Product

def logFunction():
	"""Function Used to take the values displayed and export them neatly into a .txt file"""
	sumPackage = rlpClass.amount + two_rlpClass.amount + three_rlpClass.amount
	sumReturn = rlClass.amount + two_rlClass.amount + three_rlClass.amount #Condenses the packing and return labels into one number
	
	file = open(fileName + '.txt','w+') #Creates a new file for the shipping log
	file.write('Shipping Log for ' + longDate)
	if imac > 0:
		file.write('\niMac: ' + str(iMacClass.amount))
	if sumReturn > 0:
		file.write('\nReturn Labels: ' + str(sumReturn))
	if sumPackage > 0:
		file.write('\nReturn Labels w/ Packaging: ' + str(sumPackage))
	if monitor > 0:
		file.write('\nMonitors: ' + str(monitorClass.amount))
	if ipod > 0:
		file.write('\niPod: ' + str(ipodClass.amount))
	if usbc_hdmi > 0:
		file.write('\nUSB-C to HDMI: ' + str(usbc_hdmiClass.amount))
	if usbc_dvi > 0:
		file.write('\nUSB-C to DVI: ' + str(usbc_dviClass.amount))
	if mdp_dvi > 0:
		file.write('\nMDP to DVI: ' + str(mdp_dviClass.amount))
	if mdp_vga > 0:
		file.write('\nMDP to VGA: ' + str(mdp_vgaClass.amount))
	if vga > 0:
		file.write('\nVGA: ' + str(vgaClass.amount))
	if dvi > 0:
		file.write('\nDVI: ' + str(dviClass.amount))
	if imac_power > 0:
		file.write('\niMac Power Cable: ' + str(imac_powerClass.amount))
	if power > 0:
		file.write('\nPower Cable: ' + str(powerClass.amount))
	if ethernet > 0:
		file.write('\nCat5: ' + str(ethernetClass.amount))
	if keyboard > 0:
		file.write('\nKeyboard/Mouse: ' + str(keyboardClass.amount))
	if headset > 0:
		file.write('\nHeadset: ' + str(headsetClass.amount))
	if webcam > 0:
		file.write('\nWebcam: ' + str(webcamClass.amount))
	file.close()