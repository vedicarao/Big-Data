#!/usr/bin/python3
import math
import json
import sys
key = sys.argv[1]
k=sys.argv[2]	
k=int(k)
f=sys.stdin
for line in f:
			j=json.loads(line)
			if not all(x.isalpha() or x.isspace() for x in j['word']):
				continue
			if(j["countrycode"].isupper() == False or len(j["countrycode"])!=2 ):
				continue

			if not isinstance(j["recognized"], bool):
				continue

			if(j["key_id"].isnumeric()== False or len(j["key_id"])!=16):
				continue

			if len(j['drawing']) < 1: 
				continue

			if len(j['drawing']) > 1:
				flag=1
				for i in j["drawing"]:
					if(len(i) !=2 or (len(i[0])!= len(i[1]))):
						flag=0
						break
				
				if flag==0:
					 continue
			if (math.sqrt(((j['drawing'][0][0][0])**2) + ((j['drawing'][0][1][0])**2)) > k) and (j['word']==key):
				print('%s\t%s' % (j['countrycode'],1))





