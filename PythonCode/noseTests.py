#Author: Alex Dawson-Elli

"""
noseTests.py:
provides tests for the methods and data structures used in
this project. The tests are organized by class, and can be 
run from the command line, using the nosetest command
"""
#-------------------------import libraries------------------------------
import Simulator as Sim


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






	





#-------------------------AnalysisTools Tests----------------------------

