from sympy import symbols #sympy for symbolic computation
from sympy import Matrix
import numpy as np
# Calculating the lagrange polynomial without loops

xi = [1,2,3]
yi = [3, 4, 2]
nx = len(xi)
x = symbols('x')

A = x* Matrix.ones(nx)
B = np.tile(np.array(xi).reshape(-1, 1), (1, nx)) 
top = A -B

l1 = np.tril(top, -1)
d1 = np.eye(nx)
u1 = np.triu(top, 1)
top = l1+ u1 +d1;

C = np.tile(np.array(xi), (nx,1))
bot= C- B

l2 = np.tril(bot, -1)
u2 = np.triu(bot, 1)
bot = l2+ d1+ u2

top1 = np.prod(top, axis = 1)
bo1 = np.prod(bot, axis =1)
lag = np.sum(top1/bo1 * np.array(yi))
print(lag)