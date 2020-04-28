import sys
import SudokuBoard


def main():
	'''
	outputs the solution 
	takes argument from cmd as args

	usage: python soduku_solver.py 00000123....
	'''

	Csp = SudokuBoard.SudokuBoard(sys.argv[1])
	SudokuBoard.AC3(Csp)
	Csp.AssignAC3Output()
	Solution = None
	if Csp.IsComplete():
	    Solution = Csp.WriteOutput() + ' AC3'
	    
	elif SudokuBoard.BackTrack(Csp):
	    Solution = Csp.WriteOutput() + ' BTS'
	print(Solution)    

if __name__ == '__main__':
	main()