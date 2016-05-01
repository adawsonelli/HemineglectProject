#Author: Alex Dawson-Elli


#-----imports--------
import time as time
import random 

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
		self.sr    = 25 #sample rate for simulators
		self.sampleList = [] #initialize empty sample list that will contain all samples



	def leftBias(self, alpha, sec):
		"""
		creates sec, seconds of random samples of head orientation data to simulate a Left
		head orientational bias of alpha degrees of yaw (positive by kinect convention)
		"""
		samples = sec*self.sr
		for sample in range(0, samples):
			self.n += 1 #increment sample counter
			time = self.simulateTime()

			#simulate random yaw angle
			pitch =   0.0 + random.gauss(0,1)
			roll  =   0.0 + random.gauss(0,1)
			yaw   = alpha + random.gauss(0,1)
			orientation = [pitch, roll, yaw ]

			#package into sample, and append to sample list
			sample = self.packageSample(time, orientation)
			self.sampleList.append(sample)


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

	#-----------helper methods-----------------------

	def simulateTime(self):
		"""
		self, int -> float
		simulates sequential time stamps, starting with the birth time of the 
		simulation object. 
		"""
		
		return self.birth + (1.0/self.sr * self.n)


	def packageSample(self, timeStamp, orientation):
		"""
		float, list(float, float, float) -> dict
		packages up the timestamp and the orientation data into a dictionary,
		representing a single sample
		"""
		sample = {}
		sample['time'] =  timeStamp
		sample['orientation'] = orientation
		return sample



	def publish(self, filename):
		"""
		writes all events in the simulator's object data structure to a file
		for processing by data analysis scripts. 
		"""

	
	def exampleData(self):
		"""
		uses many of the simulator class methods to simulate
		and publish example data, to be used by analysis scripts
		"""
		#generate simulated activity
		#working at a computer, 
		self.rightBias(5,120)
		self.leftHeadTurn(50,1) #looking left to talk to a collegue,
		self.leftBias(50,30)
		self.nod(2):            #noding in agreement
		self.rightHeadTurn(50,1) #return to work
		self.rightBias(5,20)  

		#publish activity to a file
		self.publish()












