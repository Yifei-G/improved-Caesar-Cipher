def encryptLower(codePoint):
	# if the sum of shift and original code point is greater than ord("z") which is 122
	# we need to calculate the difference between codePoint and ord("z")
	# adding the rest to ord("a") then always rest 1
	if codePoint > 122:
		rest = codePoint - 122
		finalCode = ord("a") + rest - 1
		return chr(finalCode)
	else:
		return chr(codePoint)


def encryptUpper(codePoint):
	# the same logic as encryptLower but using ord("Z") which is 90
	if codePoint > 90:
		rest = codePoint - 90
		finalCode = ord("A") + rest - 1
		return chr(finalCode)
	else:
		return chr(codePoint)


def codeEncrypt(codePoint, shift, isLowerCase):
	newCodePoint = codePoint + shift
	if isLowerCase:
		result = encryptLower(newCodePoint)
	else:
		result = encryptUpper(newCodePoint)

	return result
