#Gauss Siedel Iteration Method Solving

#func-1

from sys import exit

def eqn_input() :
	try:
		list_1 = list(eval(input("Enter a1 , b1 , c1 , d1 : ")))
		list_2 = list(eval(input("Enter a2 , b2 , c2 , d2 : ")))
		list_3 = list(eval(input("Enter a3 , b3 , c3 , d3 : ")))
	except:
		print("Entered something invalid!!! Please enter valid input...")
		main()
		repeat()
	return list_1 , list_2 , list_3

#func-2

def given_eqns(l1 , l2 , l3) :
	a1 , b1 , c1 , d1 = l1
	a2 , b2 , c2 , d2 = l2
	a3 , b3 , c3 , d3 = l3
	print("The given equations are :-\n")
	print(a1,'x +',b1,'y +',c1,'z = ',d1)
	print(a2,'x +',b2,'y +',c2,'z =', d2 ,"\nand ")
	print(a3,'x +',b3,'y +',c3,'z =',d3 ) 


#func-3
	
def diagonal_dominant(l1 , l2 , l3) :
	
	f1 , f2 , f3 = 0 , 0 , 0
	#must be strictly- diagonally dominant
	# |a1| > |b1| + |c1| for list_1
	#and follows the same for others
	for i in l1 :
		if abs(l1[0]) == abs(l1[1]) + abs(l1[2]) :
			f1 = 2
		elif abs(l1[0]) > abs(l1[1]) + abs(l1[2]) :
			f1 = 1
		else :
			continue
	
	for i in l2 :
		if abs(l2[1]) == abs(l2[0]) + abs(l2[2]) :
			f2 = 2
		elif abs(l2[1]) > abs(l2[0]) + abs(l2[2]) :
			f2 = 1
		else :
			continue
	
	for i in l3 :
		if abs(l3[2]) == abs(l3[0]) + abs(l3[1]) :
			f3 = 2
		elif abs(l3[2]) > abs(l3[0]) + abs(l3[1]) :
			f3 = 1
		else :
			continue
	
	if [f1 , f2 , f3] == [1 , 1 , 1] :
		return bool(1)
	elif [f1 , f2 , f3] == [0 , 0 , 0] :
		return bool(0)
	else:
		return None


#func-4
#prints the rearranged equations.

def rearranged_eqns(l1 , l2 , l3) :
	a1 , b1 , c1 , d1 = l1
	a2 , b2 , c2 , d2 = l2
	a3 , b3 , c3 , d3 = l3
	print("The rearranged equations are :-")
	print('x = (',d1,' - ',b1,'y - ',c1,'z) /',a1)
	print('y = (',d2,' - ',a2,'x - ',c2,'z) /',b2,'\n and ')
	print('z = (',d3,' - ',a3,'x - ',b3,'y) /',c3)


#func-5

def solve(list_1 , list_2 , list_3) :
	a1 , b1 , c1 , d1 = list_1
	a2 , b2 , c2 , d2 = list_2
	a3 , b3 , c3 , d3 = list_3
	
	x , y , z = 0 , 0 , 0 #intial answers assumed
	i = 1  #for calculating iterations and controlling while loop only
	
	while i < 100 :
	 # iterations are not prolonged than 99 times
	 # "i value need not be given , but loop too shouldn't be prolonged way much"
		print(i," : ")
		x = (d1 - (b1 * y) - (c1 * z)) * (1/a1)
		print('x =( ', d1,'-( ',b1,'× ',y,'- ',c1,'× ',z,')) × (1/ ',a1,') =',x)
		y = (d2 - (a2 * x) - (c2 * z)) * (1/b2)
		print('y =( ', d2,'-( ',a2,'× ',x,'- ',c2,'× ',z,')) × (1/ ',b2,') = ',y)
		z = (d3 - (a3 * x) - (b3 * y)) * (1/c3)
		print('z =( ', d3,'-( ',a3,'× ',x,'- ',b3,'× ',y,')) × (1/ ',c3,') = ',z)
		print('\n')
		
		i += 1
		
		if (((a1 * x) + (b1 * y) + (c1 * z)) == d1 and ((a2 * x) + (b2 * y) + (c2 * z)) == d2 and ((a3 * x) + (b3 * y) + (c3 * z)) == d3) :
			break
	
	return x , y , z , i


#_main_ program

def main() :
	print("\nEnter the Equations in a Matrix form (row wise).")
	list_1 , list_2 , list_3 = eqn_input()   #retrieves all the inputted lists
	print("\n")
	given_eqns(list_1 , list_2 , list_3)   #prints the equations
	print("\n")
	input_bool = diagonal_dominant(list_1 , list_2 , list_3)    #gives True or False for declaring dominant or not
	if input_bool is bool(0) :
		print("The given equations are NOT Diagonally Dominant.\nHence not solvable.")
		print('Sorry \U0001F62A !!!')
		repeat()
	elif input_bool is None :
		print("The given equations are Loosely Diagonally Dominant.\n\n")
		rearranged_eqns(list_1 , list_2 , list_3)
		print("\n")
	else:
		print("The given equations are Strictly Diagonally Dominant.\n\n")
		rearranged_eqns(list_1 , list_2 , list_3)
		print("\n")
	print("Intially , we assume the values of x , y and z to be 'ZERO' i.e.,\nx = 0 ,\ny = 0 ,\nz = 0 .\n\n")
	x , y , z , i = solve(list_1 , list_2 , list_3) #returned the solved values of x,y and z ...also iterations value
	#if str(type(i)) == "<class 'int'>":
	if i < 100 :
		print("The given equations took" , i-1 , "iterations to solve.\n")  #checking if type of 'i' is string
	else :
		print("The given equations seems to be non-solvable ......Sorry for the inconvenience \U0001F62A")
		print("The solutions for the given equations (can be assumed) are\nx = 0\ny = 0\nz = 0")
		print("Thank You!!!")
		repeat()
		#no of iterations took to solve the problem are provided
	print("The solutions for the given equations are\nx=",x   ,"~", round(x , 2), "\ny =",y   ,"~", round(y , 2),"\nz=",z   ,"~", round(z , 2))
	#solutions and the rounded figures are given
	#if needed can use math module to round off the solutions to teo decimal places

def repeat() :
	ch = input("Do you want to continue (y/n) :")
	if ch.lower() == "y" :
		print("\n")
		main()
	elif ch.lower() == "n" :
		print("\nThank You...\U0001F917")
		exit()
	else :
		print("Please select the correct choice.")
		repeat()

#program starts from here
if __name__ == "__main__" :
	print("Gauss Siedel Iteration Method\nfor given 3 equations")
	main()
	print("\n")
	repeat()

#The End
