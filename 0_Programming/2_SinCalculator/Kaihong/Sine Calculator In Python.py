import math
def get_sin(x, precision):
    a = 0
    for i in range(100):
        a = a + (-1)**(i) * x**(2*i+1)/math.factorial(2*i+1)
    b = round(a,precision)
    error = math.sin(x) - a
    return (b,error)
