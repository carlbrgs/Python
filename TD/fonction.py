from math import sqrt


#fct(1)

def fct2(x):
    if x >= -1 and x < 3:
     return((4*x**3-6*x**2+1)*sqrt(x+1)/(3-x))
    else:
        print('x doit être compris entre -1 et 3')
"""
x=-1
 
while x<3:
    print(x, fct2(x))
   x+=0.5 
"""
def fibo(n):
    u = [0, 1]
    for i in range (2, n):
        u.append(u[i-1] + u[i-2])
    return u

#print(fibo(10))

#impairs = list(range(1, 20, 2))
#print(impairs)

def impairs(n):
    table = []
    for i in range(n):
        if i % 2 == 1:
            table.append(i)
    return table

#print(impairs(20))


#comprehension = [2*i+1 for i in range(5)]
print([2*i+1 for i in range(5)])