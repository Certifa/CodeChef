# Update the '_' in the code below

#accept the count of test cases given in the the 1st line
t = int(input())
#Run a loop to accept 't' inputs
for i in range(t):     
    #accept an integer N in each test case
    N = int(input())         
    #output the number mirror for each test case
    print(N)       


















    """
    Wat uitleg om de loop te begrijpen.

    de variable t 
    : in t word de input opgeslagen die gegeven word door bijvoorbeeld CodeChef.
    t word ook geintrpreteerd als Test cases, test cases is de hoeveelheid input die je krijgt.

    de variable i
    : in i word de loop opgeslagen, de loop is de hoeveelheid keer dat de code word uitgevoerd.
    de loop is de hoeveelheid test cases die je krijgt.

    range(t)
    : range(t) is de hoeveelheid keer dat de loop word uitgevoerd.
    range(t) is dus de hoeveelheid test cases die je krijgt.

    de variable N
    : in N word de input opgeslagen die gegeven word door bijvoorbeeld CodeChef.
    N word ook geintrpreteerd als Number, Number is de input die je krijgt.
    Je kan denken, maar N en T is toch allebei input? Ja dat klopt, maar N is de input die je krijgt in de loop, en met die input word gewerkt.

    Denk aan dit voorbeeld:

Input:
3
1
22
33

Output:
1
22
33

Maar waarom heeft de input 4 cijfers en de output 3 cijfers?
Dat komt omdat de 1e input word opgeslagen in t!
dat is de hoeveelheid test cases die je krijgt. and each test case had 1 line of input.
De 2e, 3e en 4e input word opgeslagen in N!
dat is de input die je krijgt in de loop.
De 1e, 2e en 3e output word opgeslagen in print(N)!
dat is de output die je krijgt in de loop.
    """


#accept the count of test cases given in the the 1st line
t = int(input())       
#run a loop to accept 't' inputs
for i in range(t):     
    #accept 2 integers on the 1st line of each test case
    A, B = map(int, input().split())      
    #accept 3 integers on the 2nd line of each test case
    C, D, E = map(int, input().split())   
    #output the 5 integers on a single line for each test case    
    print(A, B, C, D, E)

"""
Input                  
3
1 2
3 4 5
11 22
33 44 55
1 23
456 789 101112
----
Output
1 2 3 4 5
11 22 33 44 55
1 23 456 789 101112
----
"""


#accept the count of testcases given in the the 1st line
t = int(input())
#run a loop to accept 't' testcases
for i in range(t):
    #accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())     
    #accept 1 string on the 2nd line of each test case
    C = input()
    #output the 2 integers and 1 string on a single line for each test case
    print(A, B, C)  




#accept the count of test cases given in the the 1st line
t = int(input())        
#run a loop to accept 't' inputs
for i in range(t):      
    #accept 1 integer on the 1st line of each test case
    N = int(input())        
    #output the negative integer - i.e. (-N)
    print(-N)

"""
Input

5
1
2
3
-4
-5

Output

-1
-2
-3
4
5
"""

t = int(input())
for i in range(t):
    S = str(input())
    #create a variable X which stores the value of string S concatenated with itself
    X = S + S           
    #output the variable X
    print(X)            


#Input * 2 rekenmachine ish
t = int(input())
for i in range(t):
    N = int(input())
    print(2*N)



t = int(input())
for i in range(t): 
    X, Y = map(int, input().split())
    S = X * Y  
    print(S)
    
"""
X, Y = map(int, input().split()) is handig om te weten, want je kan het gebruiken om 2 inputs op 1 lijn te krijgen. 
Vaak word het gebruikt wanneer je 2 inputs moet krijgen, maar je moet er 1 berekening mee doen.
"""

x,y=map(int,input().split())
print(x-y)

"""
Niet overal hoeft een loop, een testcase input of iets anders het kan ook zo simpel als dit.
"""