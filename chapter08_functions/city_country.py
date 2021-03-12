#练习8-6
def city_country(city_name, city_cntry):
	message = city_name.title() + ", " + city_cntry.title()
	print(message)
	
city_country('shanghai','china')
city_country(city_name='london',city_cntry='england')
city_country(city_cntry='america',city_name='san jose')

#练习8-7
def make_album(singer, album_name, songs_num=''):
	if not songs_num:
		message = singer + ", " + album_name
		print(message.title())
	else:
		message = singer.title() + ", " + album_name.title() + ". It has " + songs_num + " songs."
		print(message)
		
make_album('Taylor','fearless')
make_album('jwhan','test album',songs_num='9')
active = ''
print()
print("*************************************************")
while True:
	print("Album Test. Please follow the instructions:")
	if active == 'y':
		break
	else:
		s_name = input("Please enter the singer name: ")
		a_name = input("Please enter the album name: ")
		active = input("Do you want to quit?(y/n)")
