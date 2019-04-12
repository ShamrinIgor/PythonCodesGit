import random

Dictinary = {\
"a" : [7, 31, 50, 63, 66, 77, 84],\
"b" : [11, 64],\
"c" : [17, 33, 49],\
"d" : [10, 27, 51, 76],\
"e" : [25, 26, 28, 32, 48, 67, 69, 72, 75, 79, 82, 85],\
"f" : [8, 9],\
"g" : [44, 83],\
"h" : [19, 20, 21, 54, 70, 87],\
"i" : [2, 3, 29, 53, 68, 73],\
"j" : [18],\
"k" : [41],\
"l" : [42, 81, 86, 95],\
"m" : [40, 52],\
"n" : [0, 43, 80, 88, 89],\
"o" : [16, 30, 61, 65, 91, 94, 96],\
"p" : [1, 62],\
"q" : [15],\
"r" : [4, 24, 39, 58, 71, 99],\
"s" : [6, 34, 56, 57, 59, 90],\
"t" : [5, 23, 35, 37, 38, 60, 74, 78, 92],\
"u" : [13, 14, 36],\
"v" : [22],\
"w" : [45, 46],\
"x" : [12],\
"y" : [55, 93],\
"z" : [47]}

# message = input("Your message: ")
# encrypted_message = ""

def my_encode(message):
	encrypted_message = ""

	for char in message:
	     char = Dictinary[char][random.randint(0,len(Dictinary[char]) - 1)]
	     encrypted_message += str(char) + ' '
	return encrypted_message

def my_decode(message):
    decrypted_message = ""
    numbers = message.split()
    for i in numbers:
        for letter in Dictinary:
            if int(i) in Dictinary[letter]:
                decrypted_message += letter

    return decrypted_message

message = input()
em = my_encode(message)
print(em)
print(my_decode(em))

# for char in message:
#      char = Dictinary[char][random.randint(0,len(Dictinary[char]) - 1)]
#      encrypted_message += str(char) + ' '
#
# print(encrypted_message)
