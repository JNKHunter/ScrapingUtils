from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getBSObj(url):

	try:
		html = urlopen(url)
	except HTTPError as e:
		print(e)
		return None
	except URLError as e:
		print(e)
		return None
	else:
	
		try:
			bsObj = BeautifulSoup(html.read(), "html.parser")
		except AttributeError as e:
			print(e)
			return None
		else:
			return bsObj

	return None
