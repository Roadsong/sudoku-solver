from z3 import *

sudoku =   ((0,0,9,8,5,6,0,0,0),
			(0,8,0,0,0,9,0,0,0),
			(2,0,0,0,0,7,0,0,0),
			(7,0,0,0,0,1,3,9,6),
			(9,0,0,0,6,0,0,0,5),
			(5,3,6,2,0,0,0,0,7),
			(0,0,0,9,0,0,0,0,1),
			(0,0,0,3,0,0,0,6,0),
			(0,0,0,6,8,2,4,0,0))


def single_block_req(S, x, y):
	return [Distinct([S[i][j] for i in range(x, x + 2) for j in range(y, y + 2)])]


def main():

	S = [[Int("s_%s_%s" % (i + 1, j + 1)) for j in range(9)] for i in range(9)]

	range_req = [And(S[i][j] >= 1, S[i][j] <= 9) for i in range(9) for j in range(9)]

	row_req = [Distinct(S[i]) for i in range(9)]

	colum_req = [Distinct([S[i][j] for i in range(9)]) for j in range(9)]

	block_req = []
	for i in [1, 4, 7]:
	  	for j in [1, 4, 7]:
	  		block_req += single_block_req(S, i, j)


	logic_req = range_req + row_req + colum_req + block_req
	value_req = [If(sudoku[i][j] == 0, True, S[i][j] == sudoku[i][j]) for i in range(9) for j in range(9)]


	solver = Solver()
	solver.add(logic_req + value_req)

	if solver.check() == sat:
		print("Solved.")
		model = solver.model()
		solved_sudoku = [[model.evaluate(S[i][j]) for j in range(9)] for i in range(9)]

		for row in solved_sudoku:
			print(str(row).replace(',','')[1:][:-1])

	else:
		print("Cannot be solved.")


if __name__ == '__main__':

	main()
