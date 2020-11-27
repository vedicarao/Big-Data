#!/usr/bin/python3
import datetime
import json
import sys
key=sys.argv[1]

infile=sys.stdin
for line in infile:
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
			if (j["recognized"]) and (j["word"]==key):
				print('%s\t%s' % ("recognized",1))
			if (not j["recognized"]) and (j["word"]==key):
					date_time_obj = datetime.datetime.strptime(j["timestamp"][:-4], '%Y-%m-%d %H:%M:%S.%f')
					if (date_time_obj.weekday()>=5) :
						print('%s\t%s' % ("unrecognized",1))









