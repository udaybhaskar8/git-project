def BMI(weight, height):
    bmi = float(weight)/(height*height)
    return '%.1f' % bmi 
print(BMI(4,6))