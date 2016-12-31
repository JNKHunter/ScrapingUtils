from bs_util import getBSObj
import re

pages = set()
domain = ''

def crawl(domainUrl):
	global domain
	domain = domainUrl
	getLinks(domain)

def getLinks(pageUrl):
	global domain
	global pages
	print("Get links called with: " + pageUrl)
	if not pageUrl.startswith(domain):
		pageUrl = domain + pageUrl
	bsObj = getBSObj(pageUrl)
	for link in bsObj.findAll("a",href=re.compile("^(?!http).*")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)



crawl('https://www.sigient.com')

