def quadratic(a, b, c): 
    d=b**2-4*a*c
    q=str(d)
    p='The discriminant is '+q+'.'
    return p
print(quadratic(2,2,3))
