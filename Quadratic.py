import re
import math as mh
print('Welcome to the Quadratic Equation Solver')
print("DO NOT indicate power")
eq=input("Enter a Quadratic Equation ====> ")

fo=re.split(r"[x\s+]+", eq)
print(fo)


a = float(fo[0])
b = float(fo[1])
c = float(fo[2])

disc= b ** 2 - 4 *a *c

if disc < 0:
    print(f"No real solutions for {eq}")
    exit()
else:
    disc=mh.sqrt(disc)

    ansr= -b + disc

    ansi = -b - disc

    f= 2* a

    ans = ansr / f

    ans2 = ansi / f

    print(f"x= {ans} or x= {ans2}")