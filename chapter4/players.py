players = ["charles","martina","michael","florence","eli"]
print(players[0:3])		#player[0:3]	此处为:
#若未指定起始索引,python将从列表头开始.同理,若为指定终止值,将执行到列表末尾
print(players[:4])
print(players[1:])
#负数索引同样有效,eg -3代表倒数第3个元素
print(players[-3:])
#for循环中同样可使用切片
for player in players[2:]:
	print(player.title())

print("**********************************************************************")
print("The original list is: "+str(players))
print("The first three items in the list are: "+str(players[0:3]))
print("Three items from the middle of the list are: "+str(players[1:4]))
print("The last three items in the list are: "+str(players[-3:]))
