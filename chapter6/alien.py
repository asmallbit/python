#创建字典 字典即一系列键值对
alien_0 = {'color': 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("\nYou just earned "+str(new_points)+" points!")

#向字典中增加键值对
alien_0['x_position'] = 0
alien_0['y position'] = 25
print(alien_0)

#使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先定义一个空字典
#alien_0 = {}
#alien_0['color'] = red
#要修改字典的值,可依次指定字典名,用方括号括起的键以及与改键关联的新值
#alien_0['color'] = yellow

#删除键值对
del alien_0['color']
del alien_0['points']
print("\nThe edited_alien_0 is:\n"+str(alien_0))

#嵌套 列表嵌套字典,字典嵌套列表,还可以字典嵌套字典等,此处以列表嵌套字典为例
print()
alien_0 ={'color': 'green', 'points':5}
alien_1 ={'color': 'yellow', 'points':10}
alien_2 ={'color': 'red', 'points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
############################################################
print()
print("*****************************************************")

#创建一个用于存储外星人的空列表
aliens = []
for alien_number in range(30):
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print("...")
#显示创建了多少外星人
print("\nTotal number of aliens: "+str(len(aliens)))
print()
print("*****************************************************")
#修改前三个外星人
for alien in aliens[:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['points']=10
for alien in aliens[:5]:
	print(alien)
