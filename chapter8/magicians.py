#练习8-9,8-10,8-11
def show_magicians(magicians_name):
	for magician_name in magicians_name:
		print("\t"+magician_name.title())

def make_great(magicians_name):
	#修改实参中的元素(通过下标)
	magicians_num = 0
	while magicians_num!=(len(magicians_name)):
		magicians_name[magicians_num] = "the Great "+magicians_name[magicians_num]
		magicians_num += 1
	return magicians_name

magicians_name =['william peter', 'bill joney', 'jw han']
print("The original list is:")
show_magicians(magicians_name)
make_great(magicians_name[:])
print("\nStill the original list:")
show_magicians(magicians_name)
edited_list = make_great(magicians_name)
print("\nThe edited list:")
show_magicians(edited_list)
