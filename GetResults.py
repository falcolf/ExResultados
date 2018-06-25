from Calculate import Calculate
import os
os.system('python FormAuto.py')
f = open('DataInfo.txt','r')
names = f.read()
names = names.split('\n')
for name in names:
	if name!='':
		Calculate('ResultData/'+name)
