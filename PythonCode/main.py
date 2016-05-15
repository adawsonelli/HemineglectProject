import Simulator as Sim
import AnalysisTools as Analysis

#instantiate simulator
sim = Sim.Simulator()
sim.exampleData()

#read in
anaTool = Analysis.AnalysisTools()
anaTool.loadData('exampleData.txt')


#display statistics
anaTool.displayPlot()
anaTool.displayStatistics()