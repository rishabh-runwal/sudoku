from random import sample    # import sample function from random module
import random                # import random module for randint function
a='_'
b=list(a*9)
li=[]
[li.append(b.copy()) for _ in range(9)]
# create a list of random non-repeating numbers from 1-9

num1  = sample(range(1,10),9)          
num2  = sample(range(1,10),9)
num3  = sample(range(1,10),9)
k=0

# Fill the diagonal 3*3 boxes first

for i in range(3):                   
    for j in range(3):
        li[i][j]=num1[k]
        k=k+1
k=0
for i in range(3,6):
    for j in range(3,6):
        li[i][j]=num2[k]
        k=k+1
k=0
for i in range(6,9):
    for j in range(6,9):
        li[i][j]=num3[k]
        k=k+1
        
# Use other functions to generate the puzzle using backtracking algorithm

def solver(li):
    z = zeros(li)
    if not z:
        return 1
    else:
        r, c = z

    for a in range(1,10):
        if valid(li, a, r, c):
            li[r][c] = a

            if solver(li):
                return 1

            li[r][c] = '_'

    return 0

# Check if their is a blank space in matrix and return its position

def zeros(li):
    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] == '_':
                return (i, j) 

# Check if the matrix is valid according to rows, columns and boxes 

def valid(li, num, i,j):
    for r in range(len(li[0])):     # Check if no. repeats in a row
        if(num==li[i][r]):
                return 0
    for c in range(len(li)):        # Check if no. repeats in a column
        if(num==li[c][j]):
                return 0
    i=((i)//3)*3                    # Done for accessing box elements
    j=((j)//3)*3
    for l in range(3): 
        for m in range(3): 
            if(li[i+l][j+m] == num):    # Check if no. repeats in a box
                return 0
    return 1
   
# Remove some amount of numbers from the generated matrix according difficulty  

def remove_nums(li):
    while 1:
        a=random.randint(0,8)
        b=random.randint(0,8)
        if li[a][b]=='_':
            continue
        else:
            li[a][b]='_'
            break

# Print board separating different boxes
    
def print_board(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("─────────────────────── ")
        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" │ ", end="")
            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")

solver(li)

LoD=int(input("Enter level of difficulty\n1.Amateur\n2.Intermediate\n3.Pro\n"))
if(LoD==1):
    l=30
if(LoD==2):
    l=35
if(LoD==3):
    l=40
for i in range(l):
    remove_nums(li)
print("Generated puzzle is : ")

print_board(li)
input("Press Enter to view Solution")
solver(li)
print("Solved puzzle is:\n ")
print_board(li)

