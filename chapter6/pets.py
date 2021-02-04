#Á·Ï°6-8
pets=[]
coco={'name':'coco','kind':'dog','person_name':'jwhan'}
bruh={'name':'bruh','kind':'cat','person_name':'jill'}
killer={'kind':'pig','name':'killer','person_name':'jack'}
pets=[coco,bruh,killer]
num=0
for pet in pets:
	print(pet['name'].title()+" is a "+pet['kind']+". His/Her owner is "+pet['person_name']+".")
