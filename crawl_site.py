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
	if not pageUrl.startswith(domain):
		pageUrl = domain + pageUrl
	bsObj = getBSObj(pageUrl)
	if(bsObj is not None):
		for link in bsObj.findAll("a",href=re.compile("^(?!http).*")):
			if 'href' in link.attrs:
				if link.attrs['href'] not in pages:
					newPage = link.attrs['href']
					print(newPage)
					pages.add(newPage)
					getLinks(newPage)



crawl('https://www.sigient.com')

