from API import API
import random
#from proxy import prox

while(1):
	#try:
		a=API()
		_device=random.randint(1,2)
		#_proxy,_port=random.choice(prox).split(':')
		#a.setProxy(_proxy,_port)
		a.setDevice(_device)
		a.reroll()
	#except:
	#	pass
