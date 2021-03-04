# -*- coding: utf-8 -*-
import requests
import re
import json
import sys
import base64
import time
import struct
import socket
import random
import units
import item_master
import io
from crypter import Crypter

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class API(object):
	def __init__(self):
		self.crypter=Crypter()
		self.base='https://g-api.grandsummoners.com/app/'
		self.s=requests.Session()
		self.s.headers.update({'Content-Type':'application/x-www-form-urlencoded','Connection':'keep-alive','User-Agent':'B_megamistrike/53 CFNetwork/808.2.16 Darwin/16.3.0','Accept-Language':'en-gb','Accept-Encoding':'gzip, deflate'})
		self.s.verify=False
		self.app_hash='5f487dc2427b3b369757cb587656c806'
		self.app_version=31
		self.master_version=404
		self.resource_version=183
		self.platform_type = 1
		self.key='ZFlyUU0ycFJaTVlFRkVoaA=='
		self.useNewKey=False
		self.device_id=None
		self.session_id=None

	def setDevice(self,id):
		self.platform_type=id

	def setProxy(self,ip,port):
		part='%s:%s'%(ip,port)
		self.log('using proxy %s'%(part))
		self.s.proxies.update({'http': 'http://%s'%part,'https': 'https://%s'%part,})

	def setNextKey(self,key):
		self.key=base64.b64encode(key)

	def challenge_end(self,challenge_id):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"challenge_id":challenge_id,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def challenge_top(self):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def eventshop_page(self,event_id):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"event_id":event_id,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def eventshop_page(self,event_id):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"event_id":event_id,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def gacha_top(self):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def game_init(self):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"encryption_key":"dYrQM2pRZMYEFEhh\\ZgAEi{I[?ZToT@G","master_version":0,"platform_type":self.platform_type,"resource_version":0})

	def home(self):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def login(self):#done
		res=self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"country_code":"","device_id":"","device_token":"","is_agree":1,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})
		self.useNewKey=True
		return res
	
	def setSessionId(self,id):
		self.session_id=id

	def setDeviceId(self,id):
		self.device_id=id

	def doLogin(self,id1,id2,force=False):
		if force:
			self.useNewKey=False
			self.setSessionId(id2)
			self.setDeviceId(id1)
			return self.login()
		else:
			self.game_init()
			self.version_get()
			self.setSessionId(id2)
			self.setDeviceId(id1)
			return self.login()

	def message_list_get(self,page):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"get_type":0,"master_version":self.master_version,"page":page,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def message_open(self,message_id_list):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"message_id_list":message_id_list,"page":1,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def party_update(self,user_party_list):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"party":{"main_no":0,"user_party_list":user_party_list},"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def quest_end(self,quest_end,tutorial_is_end=None,tutorial_step=None,tutorial_type=None):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"is_ranking_view":False,"master_version":self.master_version,"platform_type":self.platform_type,"quest_end":quest_end,"resource_version":self.resource_version,"tutorial_is_end":tutorial_is_end,"tutorial_step":tutorial_step,"tutorial_type":tutorial_type,"user_unique_id":""})

	def quest_start(self,quest_id,dungeon_id=10100,map_id=10000):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"dungeon_id":dungeon_id,"food_id":0,"map_id":map_id,"master_version":self.master_version,"party":{},"platform_type":self.platform_type,"quest_id":quest_id,"resource_version":self.resource_version,"supporter_id":"0","user_tool_id":0,"user_unique_id":""})

	def register_email(self,mail,password):
		return self.callAPI({"app_hash":"c3cff24218c4d3b7153499beea32cc23","app_version":9,"email":mail,"master_version":self.master_version,"password":password,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def scenario_end(self,played_scenario_id,tutorial_is_end=0,tutorial_step=0,tutorial_type=0):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"played_scenario_id":played_scenario_id,"resource_version":self.resource_version,"tutorial_is_end":tutorial_is_end,"tutorial_step":tutorial_step,"tutorial_type":tutorial_type,"user_unique_id":""})

	def tutorial_unit_add(self,tutorial_step,tutorial_type,unit_no):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"tutorial_step":tutorial_step,"tutorial_type":tutorial_type,"unit_no":unit_no,"user_unique_id":""})

	def tutorial_update(self,tutorial_is_end,tutorial_step,tutorial_type):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":self.master_version,"platform_type":self.platform_type,"resource_version":self.resource_version,"tutorial_is_end":tutorial_is_end,"tutorial_step":tutorial_step,"tutorial_type":tutorial_type,"user_unique_id":""})

	def user_create(self,nickname):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"country_code":"","master_version":self.master_version,"nickname":nickname,"platform_type":self.platform_type,"resource_version":self.resource_version,"user_unique_id":""})

	def version_get(self):#done
		return self.callAPI({"app_hash":self.app_hash,"app_version":self.app_version,"master_version":0,"platform_type":self.platform_type,"resource_version":0})

	def decrypt(self,input):
		return self.crypter.decrypt(input,'ZFlyUU0ycFJaTVlFRkVoaA==' if not self.useNewKey else self.key)

	def encrypt(self,input):
		return self.crypter.encrypt(input,'ZFlyUU0ycFJaTVlFRkVoaA==' if not self.useNewKey else self.key)

	def genRandomIP(self):
		return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	def callAPI(self,idata):
		_caller=sys._getframe(1).f_code.co_name
		r=self.s.post(self.base+_caller,data=json.dumps({'body':self.encrypt(idata),'device_id':'' if not self.device_id else self.device_id,'session_id':'' if not self.session_id else self.session_id}))
		body=json.loads(r.content)['body']
		if len(body)<=100:
			return body
		data= json.loads(self.decrypt(body))
		if 'encryption_key' in data:
    			self.setNextKey(data['encryption_key'])
		if 'session_id' in data:
			self.session_id=data['session_id']
			if 'player_update' in data['result']:
				if 'public_id' in data['result']['player_update']:
					self.log('hello %s:%s'%(data['result']['player_update']['public_id'],data['result']['player_update']['nickname']))
				if 'device_id' in data['result']['player_update']:
					self.device_id=data['result']['player_update']['device_id']
			if 'master_version' in data['result']:
				self.master_version=data['result']['master_version']
				self.resource_version=data['result']['resource_version']
		return data

	def log(self,msg):
		print ('[%s]%s'%(time.strftime('%H:%M:%S'),msg.encode('utf-8')))

	def sappend(self,d,f):
		with io.open(f, 'a', encoding='utf8') as the_file:
			the_file.write('%s\n'%(unicode(d)))

	def genRandomHex(self,n):
		return (''.join([random.choice('0123456789ABCDEF') for x in range(n)]).lower())

	def doMission(self,quest_id,tutorial_is_end=None,tutorial_step=None,tutorial_type=None):
		start=self.quest_start(quest_id)
		defeated_enemies=[]
		for i in start['result']['quest']['battle_list']:
			for j in i['enemy_list']:
				if j==0:
					continue
				defeated_enemies.append(j['enemy_no'])
		quest_end={}
		quest_end['boss_id']=-1
		quest_end['break_count']=0
		quest_end['break_max_damage']=0
		quest_end['clear_time']=13.312557220458984
		quest_end['combo_max']=0
		quest_end['continue_count']=0
		quest_end['crystal_count']=11
		quest_end['dead_count']=0
		quest_end['defeated_enemies']=defeated_enemies
		quest_end['dungeon_id']=1
		quest_end['equipped_item_id_list']=[300018000, 300001050]
		quest_end['fullcharge_kill']=True
		quest_end['is_state_abnormal']=False
		quest_end['live_unit_count']=2
		quest_end['map_id']=10000
		quest_end['max_damage']=3528
		quest_end['multi_user_id_list']=[]
		quest_end['quest_id']=quest_id
		quest_end['reached_battle_no']=len(start['result']['quest']['battle_list'])
		quest_end['rest_boss_hp']=0
		quest_end['result']=1
		quest_end['used_item_count']={}
		return self.quest_end(quest_end,tutorial_is_end,tutorial_step,tutorial_type)	

	def getAllGifts(self):
		message_list=self.message_list_get(1)['result']['message_list']
		message_id_list=[]
		for i in message_list:
			message_id_list.append(i['id'])
		while(True):
			res=self.message_open(message_id_list)['result']['message']['player_message_list']
			if len(res)==0:	break
			message_id_list=[]
			for i in res:
				message_id_list.append(i['id'])

	def getAllChallenges(self):
		challenge=self.challenge_top()['result']['player_update']['challenge']
		for i in challenge:
			if i['clear_value']==i['current_value']:
				self.challenge_end(i['user_challenge_id'])

	def exportUnits(self):
		units={}
		equip={}
		device_id=self.device_id
		session_id=self.session_id
		self.device_id=None
		self.session_id=None
		res=self.doLogin(device_id,session_id,True)
		player_unit_list=res['result']['player']['unit']['player_unit_list']
		player_item_list=res['result']['player']['item']['player_item_list']
		fourstar=0
		for u in player_unit_list:
			name=self.getUnitName(u['unit_id'])
			rare=self.getUnitRarity(u['unit_id'])
			if rare<4:	continue
			if rare>=4 and 'Chicken' not in name:	fourstar+=1
			if u['unit_id'] not in units:
				units[u['unit_id']]={}
				units[u['unit_id']]['name']=name
				units[u['unit_id']]['count']=1
			else:
				units[u['unit_id']]['count']+=1
		units=';'.join(['%s x%s'%(units[x]['name'],units[x]['count']) for x in units])
		fourstare=0
		for u in player_item_list:
			name=self.getEquipName(u['item_id'])
			rare=self.getEquipRarity(u['item_id'])
			if rare<4:	continue
			if rare>=4:	fourstare+=1
			if u['item_id'] not in equip:
				equip[u['item_id']]={}
				equip[u['item_id']]['name']=name
				equip[u['item_id']]['count']=1
			else:
				equip[u['item_id']]['count']+=1
		if True:
			_password=self.genRandomHex(10)
			_mail='%s@gmail.com'%(self.genRandomHex(8))
			self.getAllGifts() 
			print (_mail,_password)
			self.register_email(_mail,_password)
			equip=';'.join(['%s x%s'%(equip[x]['name'],equip[x]['count']) for x in equip])
			self.sappend('%s,%s,%s,%s,%s,%s:%s,%s,%s'%('ios' if self.platform_type==2 else 'android',fourstar,units,fourstare,equip,_mail,_password,device_id,session_id),'reroll.csv')
		else:
			print (fourstar)

	def reroll(self):
		self.game_init()
		self.version_get()
		self.user_create(self.genRandomHex(6))
		self.login()
		self.scenario_end(1000000,0,2,1)
		res=self.doMission(10101,0,4,1)
		self.scenario_end(1010190)
		self.tutorial_update(0,5,1)
		self.scenario_end(10020,0,6,1)
		self.tutorial_update(0,7,1)
		self.home()
		player_unit_list=res['result']['player_update']['unit']['player_unit_list']
		user_party_list=[{"leader_unit_id":player_unit_list[1]['id'],"no":0,"unit":[{"id":player_unit_list[1]['id'],"no":0},{"id":player_unit_list[0]['id'],"no":1},{"id":-1,"no":2},{"id":-1,"no":3}]}]
		self.party_update(user_party_list)
		self.scenario_end(1010201,0,7,1)
		self.scenario_end(10041)
		self.doMission(10102)
		self.scenario_end(1010290)#17
		self.scenario_end(10050,0,9,1)
		self.scenario_end(10060,0,10,1)
		self.scenario_end(10070)#20
		self.doMission(10103)
		self.scenario_end(1010301)
		self.scenario_end(1010390)#25
		self.tutorial_unit_add(12,1,2)
		self.scenario_end(1010399,1,13,1)
		self.gacha_top()
		self.home()
		self.gacha_do(3,10001)
		self.gacha_do(3,20001)
		self.getAllGifts()
		self.eventshop_page(2008000)
		self.scenario_end(201805301)
		self.getAllChallenges()
		#self.gacha_do(2,10017)
		#self.gacha_do(2,10018)
		#self.gacha_do(2,20006)
		#self.gacha_do(2,20007)
		self.home()
		self.exportUnits()

if __name__ == "__main__":
	a=API()
	a.reroll()