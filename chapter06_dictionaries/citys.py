cities={
	'peking':{
		'country':'china',
		'population':'21536',
		'fact':'China capital'
	},
	'tokyo':{
		'country':'japan',
		'population':'13940',
		'fact':'Janpan capital'
	},
	'london':{
		'country':'england',
		'population':'8673',
		'fact':'England capital'
	}
}

for city,cityinfo in cities.items():
	print(city.title()+" located at "+cityinfo['country'].title()+". Its population is "+
		cityinfo['population']+" thousand. And in fact, it's "+cityinfo['fact'])
