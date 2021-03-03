#练习10-10
def count_words(filename):
	try:
		with open(filename, encoding='UTF-8') as file_object:
			contents = file_object.read()
			contents = contents.split()
	except FileNotFoundError:
		print("The file "+filename+" not found. Please check the document name again.")
	else:
		print("The file "+filename+" has about "+str(len(contents))+" words.")
def count_repeat_word(filename, repeat_word):
	try:
		with open(filename, encoding='UTF-8') as file_object:
			contents = file_object.read()
			word_num = contents.lower().count(repeat_word)
	except FileNotFoundError:
		print("The file"+filename+" not found. Please check the document name again.")
	else:
		return word_num

filename = "resource/Buffalo_bill's_Ruse.txt"
count_words(filename)
repeat_word = 'the'
number = count_repeat_word(filename, repeat_word)
print("The a repeat "+str(number)+" times in the file "+filename)
