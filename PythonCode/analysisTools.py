#author Alex Dawson-Elli

#-----imports------

class analysisTools:
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

	def removeZeros():
		"""
		patient may walk away from the computer or step out of the FOV 
		the camera for a period of time. this function trims zero events out 
		"""

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