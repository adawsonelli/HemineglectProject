#author Alex Dawson-Elli

#-----imports------
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class AnalysisTools:
	"""
	The purpose of this class is to analyse head rotation data
	to develop metrics for characterizing patient head posture asymmetry.
	"""

	#----------------------private Functions-------------------------------
	def __init__(self):
		self.rawData = []
		self.filtData = []


	def readInRawData(self, filename):
		"""
		string -> none
		takes in the filename of a file to analyze, and writes it
		into self.rawData
		"""
		sample = {}
		file = open(filename, 'r')
		line = self.cleanReadline(file) #read first line
		while line != '': #haven't reached the end of the file
			#reset sample
			sample = {}

			#parse line into sample dict
			line = line.split()
			sample['time'] = float(line[0])
			orientationList = [float(line[1]), float(line[2]), float(line[3])]
			sample['orientation'] = orientationList

			#add sample to self.rawData
			self.rawData.append(sample)

			#read next line
			line = self.cleanReadline(file) 

		file.close()

	def removeZeros(self):
		"""
		patient may walk away from the computer or step out of the FOV 
		the camera for a period of time. potentially on a real system, this 
		would cause a bunch of zeros to be recorded for that time.
		this function trims these zero events out .
		"""
		for sample in self.rawData:
			if sample['orientation'] == [0, 0, 0]:
				pass
			else:
				self.filtData.append(sample)


	def removeFarAwayEvents():
		"""
		when patient is entering or exiting the frame, we want to 
		filter out that event so it doesn't get used in our statistics
		(would need information about position to be passed through as well)
		"""
		pass #to be implemented 

	def filterData():
		"""
		none -> none
		filter's self.rawData into self. filtData
		"""

	def cleanReadline(self, file):
		""" 
		file -> str

		this function is a modified version of read line that will be used to 
		clean (remove) comments and blank lines. The function will return the next availible
		line that is not a comment or blank (newline)
		"""
		flag = True
		while flag:
			#init comment and blank
			comment = False
			blank = False
			#readline
			line = file.readline()
			# test for comments
			if  '#' in line:
				comment = True
			#test for blank line
			if line.strip(' ') == '\n':  #strip used to get rid of leading whitespace
				blank = True

			#logic
			flag = comment | blank

		return line


	def filtHeadturns():
		"""
		"""

	def calcAvgHeadPos():
		"""
		none -> list
		finds the average of the filtered head data
		"""

	def calcStdDev():
		"""
		none -> list
		finds the standard deviation of the filtered head data
		"""


	#--------------------- public functions--------------------------------
	def countHeadturns():
		"""
		none -> int, int
		count the total number of head turns during the recorded event
		return the number of left turns, the number of right turns
		"""


	def displayPlot():
		"""
		displays a time plot of the unprocessed data
		"""

	def displayStatistics():
		"""
		displays the head orientation statistics for time interval analised,
		including:
			-the mean
			-the standard deviation
			-a matplotlib histogram of the distrobution (of yaw)
		"""

	def yawRollCorrelation():
		"""
		how often do patients hold their heads simultaniously yawed and 
		rolled, having posture that is single axis?
		"""