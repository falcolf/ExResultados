from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormFiller:
	
	def __init__(self,regn,dob):
		self.regn = regn
		dob = dob.split('/')
		self.date = dob[0]
		self.month = dob[1]
		self.year = dob[2]
		self.fill()

	
	def fill(self):
		driver = webdriver.Firefox()
		driver.get('http://evarsity.srmuniv.ac.in/srmwebonline/exam/onlineResult.jsp') #change url accordingly
		elem = driver.find_element_by_id('txtRegisterno')
		elem.send_keys(self.regn)
		elem = driver.find_element_by_id('txtFromDate')
		elem.send_keys(self.date)
		elemxpath = '//select[@id="selFromMonth"]/option[@value='+self.month+']'
		elem = driver.find_element_by_xpath(elemxpath).click()
		elem = driver.find_element_by_id('txtFromYear')
		elem.send_keys(self.year)
		elem = driver.find_element_by_id('txtvericode')
		elem.send_keys(Keys.RETURN)

		WebDriverWait(driver,100).until(EC.staleness_of(elem))
		
		page_content = driver.page_source
		self.saveToFile(page_content)
		#save name to file
		fname = open('DataInfo.txt','a+')
		fname.write(self.regn+'.html\n')
		fname.close()
		driver.close()

	
	def saveToFile(self,pc):
		f = open('ResultData/'+self.regn+'.html','w')
		f.write(pc)
		f.close()
