plain = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
cipher = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w", " "]

opt = int(input("Would you like to encrypt or decrypt from the caesar cipher? 1 for encrypt, 2 to decrypt: "))

if opt == 1:
	outputarray = []
	print("Encryption selected")
	en = str(raw_input("Input string: "))
	enc = en.lower()
	encarray = list(enc)
	for i in range (0,len(encarray)):
		x = plain.index(encarray[i])
		y = cipher[x]
		outputarray.append(y)
	listToStr = ''.join([str(elem) for elem in outputarray])
	print("Encrypted as: " + listToStr)

if opt == 2:
	outputarray = []
	print("Decryption selected")
	de = str(raw_input("Input encoded string: "))
	dec = de.lower()
	decarray = list(dec)
	for i in range (0,len(decarray)):
		x = cipher.index(decarray[i])
		y = plain[x]
		outputarray.append(y)
	listToStr = ''.join([str(elem) for elem in outputarray])
	print("Decrypted as: " + listToStr)