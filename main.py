from encrypt import codeEncrypt
while True:
	inputData = input("Please enter the text you want to encrypt:")
	try:
		# shift needs to be int and number only between 1 to 25
		shift = int(input("Please enter the encyption shitf (1-25):"))
		assert (shift >= 1) and (shift <= 25)
		# Use a new String for concadenation and display it to the user.
		output = ""
		isLowerCase = False
		for ch in inputData:
			codePoint = ord(ch)
			# if char's code point between 65 and 90 then it's upper case
			if (codePoint >= 65) and (codePoint <= 90):
				encypted = codeEncrypt(codePoint, shift, isLowerCase)
				output += encypted
			# if char's code point between 97 and 122 then it's lower case
			elif (codePoint >= 97) and (codePoint <= 122):
				isLowerCase = True
				encypted = codeEncrypt(codePoint, shift, isLowerCase)
				output += encypted
			else:
				output += ch
		print(output)

	except ValueError:
		print("You didn't enter a number, please enter a value between 1 to 25!")

	except AssertionError:
		print("The shift you entered is not a number between 1 to 25, please enter a number is that range!")