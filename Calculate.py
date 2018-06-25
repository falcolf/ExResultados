import requests
import codecs
from lxml import html
import sys
class Calculate:

	def __init__(self , filename ):
		file = filename
		f = codecs.open(filename,'r')
		content = f.read()
		self.parser = html.fromstring(content)
		self.name = self.parser.xpath('//div[@id="divResult"]/table/tbody/tr[1]/td[2]/text()')
		self.name = self.name[0].split("[")[0]
		self.regn = self.parser.xpath('//div[@id="divResult"]/table/tbody/tr[2]/td[2]/text()')
		self.getData()
		print(self.regn[0] + ' : ' + str(self.gpa))
		


	def getData(self):
		credits = self.parser.xpath('//table[@id="table1"]/tbody/tr/td[5]/text()')
		grades = self.parser.xpath('//table[@id="table1"]/tbody/tr/td[10]/text()')
		#print(credits)
		#print(grades)
		scores = [ self.convertGrade(str.lower(x)) for x in grades]
		totalscore=0
		totalmarks=0
		for credit,score in zip(credits,scores):
			totalscore+=int(credit)*score
			totalmarks+=int(credit)*10
		cnt = len(credits)
		self.gpa = (totalscore/totalmarks)*10
		


	def convertGrade(self,grade):
		scores = {
			'o': 10,
			'a+' : 9,
			'a' : 8,
			'b+' : 7,
			'b' : 6,
			'c' : 5,
			'p' : 4,
			'f' : 0,
			'ab' : 0,
			'i' : 0
		}
		return scores.get(grade)


if __name__ == "__main__":
	filename = sys.argv[1]
	print(filename)
	Calculate(filename)
