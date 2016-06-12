"""
Formula One Bar Graph 1950-2016

author: Shoji Moto
github: https://github.com/PianoBin
website: http://pianobin.us.to/
license: MIT
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import style
import matplotlib.cbook as cbook
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from os.path import abspath
import time
import warnings
warnings.filterwarnings("ignore",category=cbook.mplDeprecation)

####################################
###########FIRST RUN################
####################################
def firstRun(drivers, nations, cars, pts, yr):
	#Top 10
	top10driv = []
	top10nat = []
	top10car = []
	top10pts = []

	#Add top 10 to the top 10 list
	for val in range(0, 10):
		top10driv.append(drivers[val])
		top10nat.append(nations[val])
		top10car.append(cars[val])
		top10pts.append(pts[val])

	#Make all floats
	top10pts = list(map(float, top10pts))

	#Change non decimals to ints
	for count in range(0, 10):
		if top10pts[count] % 1 == 0:
			top10pts[count] = (int)(top10pts[count])

	#Check
	print (top10driv)
	print (top10nat)
	print (top10car)
	print (top10pts)

	count = 10 # run below 10 times
	
	ylocs = np.arange(10) + 0.75 #array of top 10 y spots

	
	while count > 0:
		if top10nat[count - 1] == 'ITA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'r', edgecolor = 'none')
		elif top10nat[count - 1] == 'ARG':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'aqua', edgecolor = 'none')
		elif top10nat[count - 1] == 'AUS':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'navy', edgecolor = 'none')
		elif top10nat[count - 1] == 'AUT':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'indianred', edgecolor = 'none')
		elif top10nat[count - 1] == 'BEL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightseagreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'BRA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'green', edgecolor = 'none')
		elif top10nat[count - 1] == 'CAN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'linen', edgecolor = 'none')
		elif top10nat[count - 1] == 'COL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'goldenrod', edgecolor = 'none')
		elif top10nat[count - 1] == 'DEN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightcoral', edgecolor = 'none')
		elif top10nat[count - 1] == 'ESP':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'y', edgecolor = 'none')
		elif top10nat[count - 1] == 'FIN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lavender', edgecolor = 'none')
		elif top10nat[count - 1] == 'FRA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'steelblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'GBR':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'gold', edgecolor = 'none')
		elif top10nat[count - 1] == 'GER':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'yellow', edgecolor = 'none')
		elif top10nat[count - 1] == 'HUN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'IND':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'peru', edgecolor = 'none')
		elif top10nat[count - 1] == 'IRE':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'springgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'JPN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'white', edgecolor = 'none')
		elif top10nat[count - 1] == 'MEX':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'rosybrown', edgecolor = 'none')
		elif top10nat[count - 1] == 'MON':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightsalmon', edgecolor = 'none')
		elif top10nat[count - 1] == 'NED':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'NZL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'slateblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'POL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkorange', edgecolor = 'none')
		elif top10nat[count - 1] == 'RHO':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'forestgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'RSA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'indigo', edgecolor = 'none')
		elif top10nat[count - 1] == 'RUS':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'deeppink', edgecolor = 'none')
		elif top10nat[count - 1] == 'SWE':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'royalblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'SUI':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'firebrick', edgecolor = 'none')
		elif top10nat[count - 1] == 'THA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'tomato', edgecolor = 'none')
		elif top10nat[count - 1] == 'USA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'crimson', edgecolor = 'none')
		elif top10nat[count - 1] == 'VEN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'pink', edgecolor = 'none')
		else:
			ax.barh(ylocs[10 - count], top10pts[count - 1], edgecolor = 'none')
		count -= 1

	#Stuff that changes each time
	(theMin, theMax) = ax.get_xlim()
	oldDistance = theMax - theMin
	ax.set_xlim([0, oldDistance * 0.2 + oldDistance])

	ax.set_yticks(ylocs + 0.5)
	ax.set_yticklabels(labels, fontsize = 15, fontweight = 'bold', **cfont)
	ax.set_title("Standings for the " + str(yr) + " Formula 1 Season", fontsize = 35, fontweight = 'bold', **cfont)


	rect = 10

	(Min, Max) = ax.get_xlim()
	distance = Max - Min

	while rect > 0: #Show details
		width = (distance * 0.01) + top10pts[rect - 1]
		leng = len(top10driv[rect - 1])
		width2 = top10pts[rect - 1] - (leng * 0.4)
		width3 = top10pts[rect - 1] - (leng * 0.6)
		ax.text(width2, 11 - rect, top10driv[rect - 1], color = 'black', fontweight = 'bold', **cfont)
		if top10nat[rect - 1] == 'ITA':
			abox = AnnotationBbox(ITA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'ARG':
			abox = AnnotationBbox(ARG, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'AUS':
			abox = AnnotationBbox(AUS, (width3, 11 - rect + 0.15))	
		elif top10nat[rect - 1] == 'AUT':
			abox = AnnotationBbox(AUT, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'BEL':
			abox = AnnotationBbox(BEL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'BRA':
			abox = AnnotationBbox(BRA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'CAN':
			abox = AnnotationBbox(CAN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'COL':
			abox = AnnotationBbox(COL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'DEN':
			abox = AnnotationBbox(DEN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'ESP':
			abox = AnnotationBbox(ESP, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'FIN':
			abox = AnnotationBbox(FIN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'FRA':
			abox = AnnotationBbox(FRA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'GBR':
			abox = AnnotationBbox(GBR, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'GER':
			abox = AnnotationBbox(GER, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'HUN':
			abox = AnnotationBbox(HUN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'IND':
			abox = AnnotationBbox(IND, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'IRE':
			abox = AnnotationBbox(IRE, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'JPN':
			abox = AnnotationBbox(JPN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'MEX':
			abox = AnnotationBbox(MEX, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'MON':
			abox = AnnotationBbox(MON, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'NED':
			abox = AnnotationBbox(NED, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'NZL':
			abox = AnnotationBbox(NZL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'POL':
			abox = AnnotationBbox(POL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RHO':
			abox = AnnotationBbox(RHO, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RSA':
			abox = AnnotationBbox(RSA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RUS':
			abox = AnnotationBbox(RUS, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'SWE':
			abox = AnnotationBbox(SWE, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'SUI':
			abox = AnnotationBbox(SUI, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'THA':
			abox = AnnotationBbox(THA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'USA':
			abox = AnnotationBbox(USA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'VEN':
			abox = AnnotationBbox(VEN, (width3, 11 - rect + 0.15))
		ax.add_artist(abox)
		ax.text(width, 11 - rect, top10car[rect - 1] + " | " + str(top10pts[rect - 1]), color = 'white', fontweight = 'bold', **cfont)
		rect -= 1

	plt.pause(3)
	plt.cla()


####################################
##########HOLD GRAPH################
####################################
def holdGraph(drivers, nations, cars, pts, yr):
	#Top 10
	top10driv = []
	top10nat = []
	top10car = []
	top10pts = []

	#Add top 10 to the top 10 list
	for val in range(0, 10):
		top10driv.append(drivers[val])
		top10nat.append(nations[val])
		top10car.append(cars[val])
		top10pts.append(pts[val])

	#Make all floats
	top10pts = list(map(float, top10pts))

	#Change non decimals to ints
	for count in range(0, 10):
		if top10pts[count] % 1 == 0:
			top10pts[count] = (int)(top10pts[count])

	#Check
	print (top10driv)
	print (top10nat)
	print (top10car)
	print (top10pts)

	count = 10 # run below 10 times
	
	ylocs = np.arange(10) + 0.75 #array of top 10 y spots

	
	while count > 0:
		if top10nat[count - 1] == 'ITA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'r', edgecolor = 'none')
		elif top10nat[count - 1] == 'ARG':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'aqua', edgecolor = 'none')
		elif top10nat[count - 1] == 'AUS':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'navy', edgecolor = 'none')
		elif top10nat[count - 1] == 'AUT':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'indianred', edgecolor = 'none')
		elif top10nat[count - 1] == 'BEL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightseagreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'BRA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'green', edgecolor = 'none')
		elif top10nat[count - 1] == 'CAN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'linen', edgecolor = 'none')
		elif top10nat[count - 1] == 'COL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'goldenrod', edgecolor = 'none')
		elif top10nat[count - 1] == 'DEN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightcoral', edgecolor = 'none')
		elif top10nat[count - 1] == 'ESP':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'y', edgecolor = 'none')
		elif top10nat[count - 1] == 'FIN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lavender', edgecolor = 'none')
		elif top10nat[count - 1] == 'FRA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'steelblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'GBR':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'gold', edgecolor = 'none')
		elif top10nat[count - 1] == 'GER':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'yellow', edgecolor = 'none')
		elif top10nat[count - 1] == 'HUN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'IND':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'peru', edgecolor = 'none')
		elif top10nat[count - 1] == 'IRE':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'springgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'JPN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'white', edgecolor = 'none')
		elif top10nat[count - 1] == 'MEX':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'rosybrown', edgecolor = 'none')
		elif top10nat[count - 1] == 'MON':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'lightsalmon', edgecolor = 'none')
		elif top10nat[count - 1] == 'NED':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'NZL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'slateblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'POL':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'darkorange', edgecolor = 'none')
		elif top10nat[count - 1] == 'RHO':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'forestgreen', edgecolor = 'none')
		elif top10nat[count - 1] == 'RSA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'indigo', edgecolor = 'none')
		elif top10nat[count - 1] == 'RUS':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'deeppink', edgecolor = 'none')
		elif top10nat[count - 1] == 'SWE':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'royalblue', edgecolor = 'none')
		elif top10nat[count - 1] == 'SUI':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'firebrick', edgecolor = 'none')
		elif top10nat[count - 1] == 'THA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'tomato', edgecolor = 'none')
		elif top10nat[count - 1] == 'USA':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'crimson', edgecolor = 'none')
		elif top10nat[count - 1] == 'VEN':
			ax.barh(ylocs[10 - count], top10pts[count - 1], color = 'pink', edgecolor = 'none')
		else:
			ax.barh(ylocs[10 - count], top10pts[count - 1], edgecolor = 'none')
		count -= 1

	#Stuff that changes each time
	(theMin, theMax) = ax.get_xlim()
	oldDistance = theMax - theMin
	ax.set_xlim([0, oldDistance * 0.2 + oldDistance])

	ax.set_yticks(ylocs + 0.5)
	ax.set_yticklabels(labels, fontsize = 15, fontweight = 'bold', **cfont)
	ax.set_title("Standings for the " + str(yr) + " Formula 1 Season", fontsize = 35, fontweight = 'bold', **cfont)


	rect = 10

	(Min, Max) = ax.get_xlim()
	distance = Max - Min

	while rect > 0: #Show details
		width = (distance * 0.01) + top10pts[rect - 1]
		leng = len(top10driv[rect - 1])
		width2 = top10pts[rect - 1] - (leng * 0.4)
		width3 = top10pts[rect - 1] - (leng * 0.6)
		ax.text(width2, 11 - rect, top10driv[rect - 1], color = 'black', fontweight = 'bold', **cfont)
		if top10nat[rect - 1] == 'ITA':
			abox = AnnotationBbox(ITA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'ARG':
			abox = AnnotationBbox(ARG, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'AUS':
			abox = AnnotationBbox(AUS, (width3, 11 - rect + 0.15))	
		elif top10nat[rect - 1] == 'AUT':
			abox = AnnotationBbox(AUT, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'BEL':
			abox = AnnotationBbox(BEL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'BRA':
			abox = AnnotationBbox(BRA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'CAN':
			abox = AnnotationBbox(CAN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'COL':
			abox = AnnotationBbox(COL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'DEN':
			abox = AnnotationBbox(DEN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'ESP':
			abox = AnnotationBbox(ESP, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'FIN':
			abox = AnnotationBbox(FIN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'FRA':
			abox = AnnotationBbox(FRA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'GBR':
			abox = AnnotationBbox(GBR, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'GER':
			abox = AnnotationBbox(GER, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'HUN':
			abox = AnnotationBbox(HUN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'IND':
			abox = AnnotationBbox(IND, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'IRE':
			abox = AnnotationBbox(IRE, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'JPN':
			abox = AnnotationBbox(JPN, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'MEX':
			abox = AnnotationBbox(MEX, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'MON':
			abox = AnnotationBbox(MON, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'NED':
			abox = AnnotationBbox(NED, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'NZL':
			abox = AnnotationBbox(NZL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'POL':
			abox = AnnotationBbox(POL, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RHO':
			abox = AnnotationBbox(RHO, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RSA':
			abox = AnnotationBbox(RSA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'RUS':
			abox = AnnotationBbox(RUS, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'SWE':
			abox = AnnotationBbox(SWE, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'SUI':
			abox = AnnotationBbox(SUI, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'THA':
			abox = AnnotationBbox(THA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'USA':
			abox = AnnotationBbox(USA, (width3, 11 - rect + 0.15))
		elif top10nat[rect - 1] == 'VEN':
			abox = AnnotationBbox(VEN, (width3, 11 - rect + 0.15))
		ax.add_artist(abox)
		ax.text(width, 11 - rect, top10car[rect - 1] + " | " + str(top10pts[rect - 1]), color = 'white', fontweight = 'bold', **cfont)
		rect -= 1

	plt.pause(3)
	plt.cla()

####################################
#############Y CHANGE###############
####################################
def yChange(driver, nextYearDrivers, pos):
	changePos = 11
	for num in range(0, 10):
		if nextYearDrivers[num] == driver:
			changePos = np.abs((num + 1) - pos)
	
	if changePos == 0:
		return 0
	elif changePos == 1:
		return 0.025
	elif changePos == 2:
		return 0.05
	elif changePos == 3:
		return 0.075
	elif changePos == 4:
		return 0.1
	elif changePos == 5:
		return 0.125
	elif changePos == 6:
		return 0.15
	elif changePos == 7:
		return 0.175
	elif changePos == 8:
		return 0.2
	elif changePos == 9:
		return 0.225
	elif changePos == 10:
		return 0.25
	elif changePos == 11: #Dropped out of top 10
		return 0.275

####################################
#############Y DIREC################
####################################
def yDirec(driver, nextYearDrivers, pos):
	newPos = 11
	for num in range(0, 10):
		if nextYearDrivers[num] == driver:
			newPos = num + 1
	
	if pos > newPos: #moved up
		return "up"
	elif pos < newPos:
		return "down"
	else:
		return "same"

####################################
#############X CHANGE###############
####################################
def xChange(driver, nextYearDrivers, pts, nextYearPts):
	for num in range(0, 10):
		if nextYearDrivers[num] == driver:
			return ((pts - nextYearPts[num]) / 40)
	return (pts / 40)

####################################
#############ANIMATE################
####################################
def animate(drivers, nations, cars, pts, yr, drivers2, nations2, cars2, pts2):
	#Top 10
	top10driv = []
	top10nat = []
	top10car = []
	top10pts = []

	#Top 10 of next year
	top10driv2 = []
	top10nat2 = []
	top10car2 = []
	top10pts2 = []

	#Add top 10 to the top 10 list
	for val in range(0, 10):
		top10driv.append(drivers[val])
		top10nat.append(nations[val])
		top10car.append(cars[val])
		top10pts.append(pts[val])
		top10driv2.append(drivers2[val])
		top10nat2.append(nations2[val])
		top10car2.append(cars2[val])
		top10pts2.append(pts2[val])

	#Make all floats
	top10pts = list(map(float, top10pts))
	top10pts2 = list(map(float, top10pts2))

	#Change non decimals to ints
	for count in range(0, 10):
		if top10pts[count] % 1 == 0:
			top10pts[count] = (int)(top10pts[count])
		if top10pts2[count] % 1 == 0:
			top10pts2[count] = (int)(top10pts2[count])
	
	yChanges = [] #amount of change each anim for top 10 spots
	yDirections = [] #which direction to move
	xChanges = [] #amount of change each anim for top 10 spots
	ylocs = np.arange(10) + .75

	for val in range(0, 10): #Find y change
		move = yChange(top10driv[val], top10driv2, val + 1)
		yChanges.append(move)
		direc = yDirec(top10driv[val], top10driv2, val + 1)
		yDirections.append(direc)

	for val in range(0, 10): #Find x change
		move = xChange(top10driv[val], top10driv2, top10pts[val], top10pts2)
		xChanges.append(move)

	
	for val in range(0, 10): #apply signs
		if yDirections[val] == "down":
			yChanges[val] = yChanges[val] * -1 #make negative
			xChanges[val] = xChanges[val] * -1 #decrease x


	for times in range(0, 40): #animate 40 times
		count = 10 # run below 10 times
		while count > 0:
			if top10nat[count - 1] == 'ITA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'r', edgecolor = 'none')
			elif top10nat[count - 1] == 'ARG':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'aqua', edgecolor = 'none')
			elif top10nat[count - 1] == 'AUS':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'navy', edgecolor = 'none')
			elif top10nat[count - 1] == 'AUT':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'indianred', edgecolor = 'none')
			elif top10nat[count - 1] == 'BEL':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'lightseagreen', edgecolor = 'none')
			elif top10nat[count - 1] == 'BRA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'green', edgecolor = 'none')
			elif top10nat[count - 1] == 'CAN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'linen', edgecolor = 'none')
			elif top10nat[count - 1] == 'COL':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'goldenrod', edgecolor = 'none')
			elif top10nat[count - 1] == 'DEN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'lightcoral', edgecolor = 'none')
			elif top10nat[count - 1] == 'ESP':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'y', edgecolor = 'none')
			elif top10nat[count - 1] == 'FIN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'lavender', edgecolor = 'none')
			elif top10nat[count - 1] == 'FRA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'steelblue', edgecolor = 'none')
			elif top10nat[count - 1] == 'GBR':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'gold', edgecolor = 'none')
			elif top10nat[count - 1] == 'GER':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'yellow', edgecolor = 'none')
			elif top10nat[count - 1] == 'HUN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'darkgreen', edgecolor = 'none')
			elif top10nat[count - 1] == 'IND':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'peru', edgecolor = 'none')
			elif top10nat[count - 1] == 'IRE':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'springgreen', edgecolor = 'none')
			elif top10nat[count - 1] == 'JPN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'white', edgecolor = 'none')
			elif top10nat[count - 1] == 'MEX':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'rosybrown', edgecolor = 'none')
			elif top10nat[count - 1] == 'MON':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'lightsalmon', edgecolor = 'none')
			elif top10nat[count - 1] == 'NED':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'darkblue', edgecolor = 'none')
			elif top10nat[count - 1] == 'NZL':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'slateblue', edgecolor = 'none')
			elif top10nat[count - 1] == 'POL':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'darkorange', edgecolor = 'none')
			elif top10nat[count - 1] == 'RHO':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'forestgreen', edgecolor = 'none')
			elif top10nat[count - 1] == 'RSA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'indigo', edgecolor = 'none')
			elif top10nat[count - 1] == 'RUS':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'deeppink', edgecolor = 'none')
			elif top10nat[count - 1] == 'SWE':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'royalblue', edgecolor = 'none')
			elif top10nat[count - 1] == 'SUI':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'firebrick', edgecolor = 'none')
			elif top10nat[count - 1] == 'THA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'tomato', edgecolor = 'none')
			elif top10nat[count - 1] == 'USA':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'crimson', edgecolor = 'none')
			elif top10nat[count - 1] == 'VEN':
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), color = 'pink', edgecolor = 'none')
			else:
				ax.barh(ylocs[10 - count] + (yChanges[10 - count] * times), top10pts[count - 1] + (xChanges[10 - count] * times), edgecolor = 'none')
			count -= 1

		#Stuff that changes each time
		(theMin, theMax) = ax.get_xlim()
		distance = theMax - theMin
		ax.set_xlim([0, distance * 0.2 + distance])

		ax.set_yticks(ylocs + 0.5)
		ax.set_yticklabels(labels, fontsize = 15, fontweight = 'bold', **cfont)
		ax.set_title("Standings for the " + str(yr) + " Formula 1 Season", fontsize = 35, fontweight = 'bold', **cfont)


		rect = 10

		while rect > 0: #Show details
			width = (distance * 0.01) + (top10pts[rect - 1] + (xChanges[rect - 1] * times))
			leng = len(top10driv[rect - 1])
			width2 = (top10pts[rect - 1] + (xChanges[rect - 1] * times)) - (leng * 0.5)
			width3 = (top10pts[rect - 1] + (xChanges[rect - 1] * times)) - (leng * 0.1)
			ax.text(width2, 11 - rect + (yChanges[rect - 1] * times), top10driv[rect - 1], color = 'black', fontweight = 'bold', **cfont)
			if top10nat[rect - 1] == 'ITA':
				abox = AnnotationBbox(ITA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'ARG':
				abox = AnnotationBbox(ARG, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'AUS':
				abox = AnnotationBbox(AUS, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))	
			elif top10nat[rect - 1] == 'AUT':
				abox = AnnotationBbox(AUT, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'BEL':
				abox = AnnotationBbox(BEL, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'BRA':
				abox = AnnotationBbox(BRA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'CAN':
				abox = AnnotationBbox(CAN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'COL':
				abox = AnnotationBbox(COL, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'DEN':
				abox = AnnotationBbox(DEN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'ESP':
				abox = AnnotationBbox(ESP, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'FIN':
				abox = AnnotationBbox(FIN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'FRA':
				abox = AnnotationBbox(FRA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'GBR':
				abox = AnnotationBbox(GBR, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'GER':
				abox = AnnotationBbox(GER, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'HUN':
				abox = AnnotationBbox(HUN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'IND':
				abox = AnnotationBbox(IND, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'IRE':
				abox = AnnotationBbox(IRE, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'JPN':
				abox = AnnotationBbox(JPN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'MEX':
				abox = AnnotationBbox(MEX, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'MON':
				abox = AnnotationBbox(MON, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'NED':
				abox = AnnotationBbox(NED, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'NZL':
				abox = AnnotationBbox(NZL, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'POL':
				abox = AnnotationBbox(POL, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'RHO':
				abox = AnnotationBbox(RHO, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'RSA':
				abox = AnnotationBbox(RSA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'RUS':
				abox = AnnotationBbox(RUS, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'SWE':
				abox = AnnotationBbox(SWE, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'SUI':
				abox = AnnotationBbox(SUI, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'THA':
				abox = AnnotationBbox(THA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'USA':
				abox = AnnotationBbox(USA, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			elif top10nat[rect - 1] == 'VEN':
				abox = AnnotationBbox(VEN, (width3, 11 - rect + 0.15 + (yChanges[rect - 1] * times)))
			ax.add_artist(abox)
			ax.text(width, 11 - rect + (yChanges[rect - 1] * times), top10car[rect - 1] + " | " + str(top10pts[rect - 1]), color = 'white', fontweight = 'bold', **cfont)
			rect -= 1

		print ("STOP", str(times))
		plt.pause(0.0001)
		plt.cla()
		settings()

####################################
###########Global images############
####################################
ARG1 = cbook.get_sample_data(abspath('ARG.png'), asfileobj=False)
AUS1 = cbook.get_sample_data(abspath('AUS.png'), asfileobj=False)
AUT1 = cbook.get_sample_data(abspath('AUT.png'), asfileobj=False)
BEL1 = cbook.get_sample_data(abspath('BEL.png'), asfileobj=False)
BRA1 = cbook.get_sample_data(abspath('BRA.png'), asfileobj=False)
CAN1 = cbook.get_sample_data(abspath('CAN.png'), asfileobj=False)
COL1 = cbook.get_sample_data(abspath('COL.png'), asfileobj=False)
DEN1 = cbook.get_sample_data(abspath('DEN.png'), asfileobj=False)
ESP1 = cbook.get_sample_data(abspath('ESP.png'), asfileobj=False)
FIN1 = cbook.get_sample_data(abspath('FIN.png'), asfileobj=False)
FRA1 = cbook.get_sample_data(abspath('FRA.png'), asfileobj=False)
GBR1 = cbook.get_sample_data(abspath('GBR.png'), asfileobj=False)
GER1 = cbook.get_sample_data(abspath('GER.png'), asfileobj=False)
HUN1 = cbook.get_sample_data(abspath('HUN.png'), asfileobj=False)
IND1 = cbook.get_sample_data(abspath('IND.png'), asfileobj=False)
IRE1 = cbook.get_sample_data(abspath('IRE.png'), asfileobj=False)
ITA1 = cbook.get_sample_data(abspath('ITA.png'), asfileobj=False)
JPN1 = cbook.get_sample_data(abspath('JPN.png'), asfileobj=False)
MEX1 = cbook.get_sample_data(abspath('MEX.png'), asfileobj=False)
MON1 = cbook.get_sample_data(abspath('MON.png'), asfileobj=False)
NED1 = cbook.get_sample_data(abspath('NED.png'), asfileobj=False)
NZL1 = cbook.get_sample_data(abspath('NZL.png'), asfileobj=False)
POL1 = cbook.get_sample_data(abspath('POL.png'), asfileobj=False)
RHO1 = cbook.get_sample_data(abspath('RHO.png'), asfileobj=False)
RSA1 = cbook.get_sample_data(abspath('RSA.png'), asfileobj=False)
RUS1 = cbook.get_sample_data(abspath('RUS.png'), asfileobj=False)
SWE1 = cbook.get_sample_data(abspath('SWE.png'), asfileobj=False)
SUI1 = cbook.get_sample_data(abspath('SWI.png'), asfileobj=False)
THA1 = cbook.get_sample_data(abspath('THA.png'), asfileobj=False)
USA1 = cbook.get_sample_data(abspath('USA.png'), asfileobj=False)
VEN1 = cbook.get_sample_data(abspath('VEN.png'), asfileobj=False)
background1 = cbook.get_sample_data(abspath('SPA.jpg'), asfileobj=False)

ARG2 = image.imread(ARG1)
AUS2 = image.imread(AUS1)
AUT2 = image.imread(AUT1)
BEL2 = image.imread(BEL1)
BRA2 = image.imread(BRA1)
CAN2 = image.imread(CAN1)
COL2 = image.imread(COL1)
DEN2 = image.imread(DEN1)
ESP2 = image.imread(ESP1)
FIN2 = image.imread(FIN1)
FRA2 = image.imread(FRA1)
GBR2 = image.imread(GBR1)
GER2 = image.imread(GER1)
HUN2 = image.imread(HUN1)
IND2 = image.imread(IND1)
IRE2 = image.imread(IRE1)
ITA2 = image.imread(ITA1)
JPN2 = image.imread(JPN1)
MEX2 = image.imread(MEX1)
MON2 = image.imread(MON1)
NED2 = image.imread(NED1)
NZL2 = image.imread(NZL1)
POL2 = image.imread(POL1)
RHO2 = image.imread(RHO1)
RSA2 = image.imread(RSA1)
RUS2 = image.imread(RUS1)
SWE2 = image.imread(SWE1)
SUI2 = image.imread(SUI1)
THA2 = image.imread(THA1)
USA2 = image.imread(USA1)
VEN2 = image.imread(VEN1)
background = image.imread(background1)

ARG = OffsetImage(ARG2)
AUS = OffsetImage(AUS2)
AUT = OffsetImage(AUT2)
BEL = OffsetImage(BEL2)
BRA = OffsetImage(BRA2)
CAN = OffsetImage(CAN2)
COL = OffsetImage(COL2)
DEN = OffsetImage(DEN2)
ESP = OffsetImage(ESP2)
FIN = OffsetImage(FIN2)
FRA = OffsetImage(FRA2)
GBR = OffsetImage(GBR2)
GER = OffsetImage(GER2)
HUN = OffsetImage(HUN2)
IND = OffsetImage(IND2)
IRE = OffsetImage(IRE2)
ITA = OffsetImage(ITA2)
JPN = OffsetImage(JPN2)
MEX = OffsetImage(MEX2)
MON = OffsetImage(MON2)
NED = OffsetImage(NED2)
NZL = OffsetImage(NZL2)
POL = OffsetImage(POL2)
RHO = OffsetImage(RHO2)
RSA = OffsetImage(RSA2)
RUS = OffsetImage(RUS2)
SWE = OffsetImage(SWE2)
SUI = OffsetImage(SUI2)
THA = OffsetImage(THA2)
USA = OffsetImage(USA2)
VEN = OffsetImage(VEN2)


####################################
##########FIGURE SETTINGS###########
####################################

fig = plt.figure(1, facecolor = 'white')
ax = fig.add_subplot(1, 1, 1)

ax.set_axis_bgcolor('dimgray')

background[-1, -1, -1] = 0.2
fig.figimage(background, alpha = .5)

style.use("fivethirtyeight")

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

cfont = {'fontname': 'Verdana'}

labels = ['10th', '9th', '8th', '7th', '6th', '5th', '4th', '3rd', '2nd', '1st']

def settings(): #axis settings
	ax.set_ylabel('Standings', fontsize = 20, fontweight = 'bold', **cfont)
	ax.set_xlabel('Points', fontsize = 20, fontweight = 'bold', **cfont)
	
	ax.spines['bottom'].set_color('dimgray')
	ax.spines['top'].set_color('black') 
	ax.spines['right'].set_color('dimgray')
	ax.spines['left'].set_color('dimgray')

	ax.patch.set_alpha(0.75)

	ax.grid(False)
	#gridlines = ax.get_xgridlines()
	#gridlinesy = ax.get_ygridlines()
	#for line in gridlines:
	#	line.set_color('k')
	#	line.set_alpha(0)
	#for line in gridlinesy:
	#	line.set_alpha(0)


####################################
##########READING FILES#############
####################################
with open("drivers.txt") as drivFile:
	drivData = drivFile.readlines()
	num = 67
	drivList = [[] for a in range(num)]
	for val in range(0, 67):
		drivList[val] = drivData[val].split(",")

with open("nations.txt") as natFile:
	natData = natFile.readlines()
	num = 67
	natList = [[] for a in range(num)]
	for val in range(0, 67):
		natList[val]  = natData[val].split(",")

with open("cars.txt") as carsFile:
	carsData = carsFile.readlines()
	num = 67
	carsList = [[] for a in range(num)]
	for val in range(0, 67):
		carsList[val] = carsData[val].split(",")

with open("points.txt") as pointsFile:
	pointsData = pointsFile.readlines()
	num = 67
	pointsList = [[] for a in range(num)]
	for val in range(0, 67):
		pointsList[val] = pointsData[val].split(",")


####################################
###############START################
####################################
for year in range(1950, 2017):
	settings()
	if year == 1950:
		firstRun(drivList[year - 1950], natList[year - 1950], carsList[year - 1950], pointsList[year - 1950], year)
	else:
		holdGraph(drivList[year - 1950], natList[year - 1950], carsList[year - 1950], pointsList[year - 1950], year)
	#settings()
	#animate(drivList[year - 1950], natList[year - 1950], carsList[year - 1950], pointsList[year - 1950], year, drivList[year - 1949], natList[year - 1949], carsList[year - 1949], pointsList[year - 1949]) #current year and the next year


