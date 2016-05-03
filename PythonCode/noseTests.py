#Author: Alex Dawson-Elli

"""
noseTests.py:
provides tests for the methods and data structures used in
this project. The tests are organized by class, and can be 
run from the command line, using the nosetest command
"""
#-------------------------import libraries------------------------------
import Simulator as Sim
import AnalysisTools as Analysis
from nose.tools import *


#-------------------------Simulator Tests--------------------------------

#instantiate Simulator object
sim = Sim.Simulator()

def test_simulateTime():
	t1 = sim.simulateTime()
	t2 = sim.simulateTime()
	assert  t1-t2 == 0.0

def test_packageSample():
	sample = sim.packageSample(123.456, (0.0,3.5,0.0))
	assert sample['time'] == 123.456
	assert sample['orientation'] == (0.0,3.5,0.0)
	assert sample == {'time': 123.456, 'orientation': (0.0,3.5,0.0)}

	sample = sim.packageSample(0.0 , (0,0,0))
	assert sample == {'time': 0, 'orientation': (0,0,0)}


def test_leftBias():
	#test the samples are is being added properly
	for i in range(1,5):
		initialLength = len(sim.sampleList)
		sim.leftBias( 5, i) # simulate left bias events, and append to sample list
		assert len(sim.sampleList) - initialLength == i*sim.sr

	#test data structure by accessing yaw angle
	for sample in range(0,len(sim.sampleList)):
		yaw = sim.sampleList[sample]['orientation'][2]
		flag = yaw < 5 + 4  and yaw > 5 - 4 
		assert flag == True
		#value should not exceed 4 standard deviations from the mean


def test_genRotationKinematics():
	#test several samples along an example curve
	angle = 20  #degrees
	totalTime  = .5  #seconds to turn head
	modelTime = 0  #time of event

	#test positive values of alpha
	sample = sim.genRotationKinematics(angle, totalTime, modelTime) 
	assert sample == 0
	modelTime = .1
	sample = sim.genRotationKinematics(angle, totalTime, modelTime) 
	assert sample == 1.6
	modelTime = .4
	sample = sim.genRotationKinematics(angle, totalTime, modelTime) 
	assert sample == 18.4
	modelTime = .5
	sample = sim.genRotationKinematics(angle, totalTime, modelTime) 
	assert sample == 20

	#test negative values of alpha
	modelTime = 0  #time of event
	sample = sim.genRotationKinematics(-angle, totalTime, modelTime) 
	assert sample == 0
	modelTime = .1
	sample = sim.genRotationKinematics(-angle, totalTime, modelTime) 
	assert sample == -1.6
	modelTime = .4
	sample = sim.genRotationKinematics(-angle, totalTime, modelTime) 
	assert sample == -18.4
	modelTime = .5
	sample = sim.genRotationKinematics(-angle, totalTime, modelTime) 
	assert sample == -20

	#test for exceptions on ZeroDivisionErrors
	assert_raises(ZeroDivisionError, sim.genRotationKinematics, angle, 0 , modelTime) 
  

def test_sample2string():
  	sample = {'time': 123.456, 'orientation': (0.0,3.5,0.0)}
  	string = sim.sample2string(sample)
  	assert string.strip() == '123.456    0.0    3.5    0.0'  #remove \n with strip method
  	assert string.split() == ['123.456', '0.0', '3.5', '0.0']


#-------------------------AnalysisTools Tests----------------------------

#instantiate analysisTools object
anaTool = Analysis.AnalysisTools()

def test_cleanReadline():
	testFile = open('cleanReadlineTest.txt')
	testList = []
	line = anaTool.cleanReadline(testFile)
	while line != '': #haven't reached the end of the file
		line = line.strip()  # remove newline character
		testList.append(line)
		line = anaTool.cleanReadline(testFile)


	#test 
	print(testList)
	assert testList == ['this', 'is', 'a', 'test']


def test_readInRawData():
	anaTool.readInRawData('readInRawDataTest.txt')

	#test result
	print( anaTool.rawData)
	assert anaTool.rawData[0]['time'] == 123.11
	assert anaTool.rawData[1]['time'] == 123.22
	assert anaTool.rawData[2]['time'] == 123.33
	assert anaTool.rawData[0]['orientation'] == [0, 3.44, 3.55]
	assert anaTool.rawData[1]['orientation'] == [3, .141, 5926]
	assert anaTool.rawData[2]['orientation'] == [2, .718, 2818]




def test_removeZeros():
	#the length of the test vector from readInRawData
	assert len(anaTool.rawData) == 4

	#filter out the zero orientation at the end of the file
	anaTool.removeZeros()

	#test final length
	assert len(anaTool.filtData) == 3 # zero removed

