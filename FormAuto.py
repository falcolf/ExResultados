from Driver import FormFiller
f = open('dets.csv','r')
dets = f.read()
dets = dets.split('\n')
for det in dets:
	if det!='':
		det = det.split(',')
		regn = det[1]
		dob = det[2]
		FormFiller(regn,dob)
