# print welcome message
print('I am here to calculate your BMI')

print()

# Inputs
print('Please input weight in Kg')
weight = input()
print('Good')
print('Now, please input height in meteres')
height = input()

# logic
height_m = float(height) ** 2
BMI = float(weight) / height_m

print()

# output
print('Your BMI is ' + str(BMI))
