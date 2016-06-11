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

urls = []
part1 = "http://www.formula1.com/content/fom-website/en/results.html/"
part2 = "/drivers.html"

year = 1950

for num in range(1950, 2017):
	url = part1 + str(num) + part2
	urls.append(url)

drivFile = open("drivers.txt", "w")
natFile = open("nations.txt", "w")
carFile = open("cars.txt", "w")
ptFile = open("points.txt", "w")

count = 0
up = 100 / 66

for address in urls:
	req = urllib.request.Request(address)
	with urllib.request.urlopen(req) as response:
		page = response.read()

	soup = BeautifulSoup(page, "html.parser")

	for span in soup.find_all("span", class_ = 'hide-for-mobile'):
		drivFile.write((span.get_text()))
		drivFile.write(",")

	for td in soup.find_all("td", class_ = 'dark semi-bold uppercase'):
		natFile.write(td.get_text())
		natFile.write(",")

	for a in soup.find_all("a", class_ = 'grey semi-bold uppercase ArchiveLink'):
		carFile.write(a.get_text())
		carFile.write(",")

	for td in soup.find_all("td", class_ = 'dark bold'):
		ptFile.write(td.get_text())
		ptFile.write(",")

	drivFile.write("\n")
	natFile.write("\n")
	carFile.write("\n")
	ptFile.write("\n")

	year += 1
	print (str(count * up))
	count += 1


drivFile.close()
natFile.close()
carFile.close()
ptFile.close()
