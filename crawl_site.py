from bs_util import getBSObj
import re

pages = set()

def getLinks(pageUrl):	
	print("Get links called with: " + pageUrl)
	global pages
	bsObj = getBSObj(pageUrl)
	for link in bsObj.findAll("a",href=re.compile("[^http:]")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)




