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



	def leftBias(self, gamma, sec):
		"""
		creates sec, seconds of random samples of head orientation data to simulate a Left
		head orientational bias of gamma egrees of yaw (positive by kinect convention)
		"""
		samples = sec*self.sr
		for sample in range(0, samples):
			self.n += 1 #increment sample counter
			time = self.simulateTime()

			#simulate random yaw angle
			orientation = self.changeOrientationAddNoise(0,0,gamma)

			#package into sample, and append to sample list
			sample = self.packageSample(time, orientation)
			self.sampleList.append(sample)


	def rightBias(self, gamma, sec ):
		"""
		creates n random samples of head orientation data to simulate a Right
		head orientational bias of -gamma degrees of yaw (negative by kinect convention)
		"""
		self.leftBias(-gamma, sec)


	def headTurnGeneral(self, angle, sec, p, y, r ):
		"""
		float, float, bool, bool, bool -> none
		abstract (private) function that that can create any of the principle 
		rotations, but only one at a time, not two or more simultaniously.
		"""

		#----model angle at each time step, and then add some noise----
		samples = sec*self.sr
		samplePeriod = 1/self.sr

		for sample in range(0, samples):
			self.n += 1 #increment sample counter
			runTime = self.simulateTime()
			modelTime = sample * samplePeriod

			#model rotation at current time step
			theta = self.genRotationKinematics(angle, sec, modelTime)

			#simulate random rotation angle, add noise 
			orientation = self.changeOrientationAddNoise(angle*p, angle*y, angle*r)

			#package into sample, and append to sample list
			sample = self.packageSample(runTime, orientation)
			self.sampleList.append(sample)



	def leftHeadTurn(self, angle, sec):
		"""
		turns head left (yaw) by "angle" degrees, over sec of time, 
		assuming a constant (magnitude) acceleration trajectory. 
		"""
		headTurnGeneral(angle, sec, 0, 1, 0 )
		


	def rightHeadTurn(self, angle,sec):
		"""
		turns head right (yaw) by "angle" degrees, over sec of time,
		assuming a constant (magnituce) acceleration trajectory.
		"""
		headTurnGeneral(-angle, sec, 0, 1, 0 )


	def nod(self, angle, sec):
		"""
		simulates a nod event (one up and down) about the pitch axis
		taking place over sec number or seconds
		"""
		headTurnGeneral( angle/2.0, sec/4.0, 0, 1, 0)
		headTurnGeneral(-angle, sec, 0, 1, 0 )
		headTurnGeneral( angle/2.0, sec/4.0, 0, 1, 0)

	#-----------helper methods-----------------------

	def genRotationKinematics(self, angle, sec, modelTime):
		"""
		float, float, float -> float

		uses constant magnitude acceleration to calcuate head rotation
		kinematics. is implemented as a split function where half the time 
		is spent accelerating, half decelerating

		alpha is acceleration, omega is angular velocity, theta (or angle) is angle
		"""
		#-------this is getting repeatedly executed, which is unnecessary
		try:
			#determine acceleration value to get to halfway point in half the time
			halfTime = sec/2
			halfAngle = angle/2
			alpha = (halfAngle*2.0)/(halfTime**2)

			#determine the values of the model at the halfway point for the second to
			#be used as initial conditions for the second part of the split function
			omegaHalf = alpha*(halfTime)

		except ZeroDivisionError:
			raise ZeroDivisionError('sec parameter must be greater than zero')


		#-------- end

		#model rotation at current time step
		if modelTime < halfTime: #first function of split function
			theta = .5*(alpha)*modelTime**2
		elif modelTime >= halfTime: #second half of the split function
			theta = .5*(-alpha)*(modelTime-halfTime)**2 + omegaHalf*modelTime - halfAngle


		#round output to the proper number of decimal places
		theta = round(theta, 3)
		return theta 


	def changeOrientationAddNoise(self, alpha, beta, gamma):
		"""
		float, float, float -> list
		function to implement rotations alpha, beta, gamma, 
		and add simulated gaussian noise to the measurement
		"""

		pitch =  alpha + random.gauss(0,1)
		roll  =  beta  + random.gauss(0,1)
		yaw   =  gamma + random.gauss(0,1)
		orientation = [pitch, roll, yaw ]
		return orientation


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

#------------put it all together------------------------
	
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
		self.nod(2)         #noding in agreement
		self.rightHeadTurn(50,1) #return to work
		self.rightBias(5,20)  

		#publish activity to a file
		self.publish()












