
#-----imports--------
import time as time

class Simulator:
	""" 
	The purpose of this class is to simulate different types
	head orientation data that are projected to exist, so that
	the analysis algorithms can be demonstrated to work properly

	The interface design is as follows:
		-head orientation is specified using pitch, roll and yaw
		-applied in that order, and body centric. 
		-this is an assumption, as the documentation is not
		well definied for the kinect

	time stamps are generated using the python time module
		- time will be written using time.time() function as
		seconds since the epoch

	"""
	def __init__(self):
		"""
		initialize class datavariables that are shared between class functions
		"""
		self.birth =  time.time() # time that the simulator object was created.
		self.n     = 0  #counter for total number of samples in simulation.  
		self.sr    = 30 #sample rate for simulator
		self.



	def leftBias(self, alpha, sec):
		"""
		creates sec, seconds of random samples of head orientation data to simulate a Left
		head orientational bias of alpha degrees of yaw (positive by kinect convention)
		"""


	def rightBias(self, alpha, sec ):
		"""
		creates n random samples of head orientation data to simulate a Right
		head orientational bias of -alpha degrees of yaw (negative by kinect convention)
		"""

	def leftHeadTurn(self, amplitude, sec):
		"""
		turns head left (yaw) by amplitude degrees, over sec of time.
		"""


	def rightHeadTurn(self, amplitude,sec):
		"""
		turns head left (yaw) by amplitude degrees, over sec of time.
		"""


	def nod(self, sec):
		"""
		simulates a nod event (one up and down) about the pitch axis
		taking place over sec number or seconds
		"""

	def simlulateTimes(self):
		"""
		simulates sequential time stamps, starting with the birth time of the 
		simulation object. 
		"""



	def publish(self, filename):
		"""
		writes all events in the simulator's object data structure to a file
		for processing by data analysis scripts. 
		"""

	def test():
		"""
		consider putting the testing functions within the class, as this
		is compelling from an organizational standpoint
		"""
		pass









