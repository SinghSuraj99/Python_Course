weight = int(input('What is your weight? '))
unit = input("(L)bs or (K)gs? ")

if unit.upper() == 'L':
    weight_kg = weight * 0.4536
    print(f' Your weight is {weight_kg} kgs')
else:
    weight_lb = weight / 0.4536
    print(f' Your weight is {weight_lb} lbs')