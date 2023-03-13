import math as mt

def step(x):
    if(x > 0.0):
        return 1.0
    else:
        return 0.0
    
def bipolar_step(x):
    if(x >= 0.0):
        return 1.0
    else:
        return -1.0

def symetric_ramp(x, limit):
    if(x > limit):
        return limit
    elif(x < (-1)*limit):
        return (-1)*limit
    else:
        return x

def logistic(x, beta):
    numerator = 1.0
    denominator = 1.0 + mt.exp((-1) * beta * x)
    return numerator/denominator

def tanh(x, beta):
    numerator = 1.0 - mt.exp((-1) * beta * x)
    denominator = 1.0 + mt.exp((-1) * beta * x)
    return numerator/denominator


    
