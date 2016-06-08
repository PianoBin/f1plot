"""
Formula One Bar Graph 1950-2016

author: Shoji Moto
github: https://github.com/PianoBin
website: http://pianobin.us.to/
license: MIT
Please feel free to use and modify this, but keep the above information. Thanks!
"""

from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import style


def graph(drivers, nations, cars, pts):
	top10driv = []
	top10nat = []
	top10car = []
	top10pts = []

	for val in range(0, 10):
		top10driv.append(drivers[val])
		top10nat.append(nations[val])
		top10car.append(cars[val])
		top10pts.append(pts[val])

	count = 10
	ind = np.arange(count)
	
	fig, ax = plt.subplots()
	
	for num in range(0, 10):
		rects = ax.barh(ind[num], top10pts[num])

	#rects = ax.barh(int(ind), top10pts)

	ax.set_ylabel('Standings')
	ax.set_xlabel('Points')
	ax.set_yticks(ind + 0.8)
	ax.set_yticklabels(('10', '9', '8', '7', '6', '5', '4', '3', '2', '1'))

	

	for rect in rects:
		width = rect.get_width()
		ax.text(1.05 * width, rect.get_y(), "Driver: " + top10driv[count - 1] + ", NAT: " + top10nat[count - 1] + ", Car: " + top10car[count - 1] + ", Points: " + top10pts[count - 1])
		count -= 1

	plt.show()


urls = []
part1 = "http://www.formula1.com/content/fom-website/en/results.html/"
part2 = "/drivers.html"

year = 1950

style.use("fivethirtyeight")

fig = plt.figure()

for num in range(1950, 2017):
	url = part1 + str(num) + part2
	urls.append(url)

for address in urls:
	req = urllib.request.Request(address)
	with urllib.request.urlopen(req) as response:
		page = response.read()

	soup = BeautifulSoup(page, "html.parser")
	

	drivers = []
	nations = []
	cars = []
	pts = []

	for span in soup.find_all("span", class_ = 'hide-for-mobile'):
		drivers.append(span.get_text())

	for td in soup.find_all("td", class_ = 'dark semi-bold uppercase'):
		nations.append(td.get_text())

	for a in soup.find_all("a", class_ = 'grey semi-bold uppercase ArchiveLink'):
		cars.append(a.get_text())

	for td in soup.find_all("td", class_ = 'dark bold'):
		pts.append(td.get_text())

	#graph(drivers, nations, cars, pts)

	print (str(year))
	print ("Drivers: ", drivers, "\n")
	print ("Nationalities: ", nations, "\n")
	print ("Cars: ", cars,  "\n")
	print ("Points: ", pts, "\n")

	year += 1

'''
req = urllib.request.Request("http://www.formula1.com/content/fom-website/en/results.html/1950/drivers.html")
with urllib.request.urlopen(req) as response:
	page = response.read()

soup = BeautifulSoup(page, "html.parser")

drivers = []
nations = []
cars = []
pts = []

for span in soup.find_all("span", class_ = 'hide-for-mobile'):
	drivers.append(span.get_text())

for td in soup.find_all("td", class_ = 'dark semi-bold uppercase'):
	nations.append(td.get_text())

for a in soup.find_all("a", class_ = 'grey semi-bold uppercase ArchiveLink'):
	cars.append(a.get_text())

for td in soup.find_all("td", class_ = 'dark bold'):
	pts.append(td.get_text())

print ("Drivers: ", drivers, "\n")
print ("Nationalities: ", nations, "\n")
print ("Cars: ", cars,  "\n")
print ("Points: ", pts, "\n")

#html = soup.prettify()
#html = html.encode("UTF-8")
'''

