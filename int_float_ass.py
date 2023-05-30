#assigning integer
num_int = 6

print(num_int) #6
print(type(num_int)) #<class 'int'>

#assigning float

num_float = 243.43
print(num_float) #243.43
print(type(num_float)) #<class 'float'>

#performing calculations on integers/floats

#addition

num1 = 2
num2 = 5
result = num1 + num2
print(result) #7

#shorthand addition

result += 10
print(result) #17

#subtraction

result_diff = num2 - num1
print(result_diff) #3

#shorthand subtraction

result_diff -= 1
print(result_diff) #2

#multiplication

result_prod = num1 * num2
print(result_prod) #10

#shorthand multiplication

result_prod *= 5
print(result_prod) #10

#division

result_div = num2 / num1
print(result_div) # 2.5
print(type(result_div)) #<class 'float'>

#shorthand division

result_div /= 2
print(result_div) #1.25

#floor division

result_norm = 15 / 4
print(result_norm) #3.75
result_floor = 15 // 4
print(result_floor) #3

#shorthand floor division

result_floor //= 2
print(result_floor) #1

#Modulo

num3 = 48
num4 = 5
result_mod = num3 % num4
print(result_mod) #3

#shorthand modulo

result_mod %= 2
print(result_mod) #1

#Exponential

num5 = 3
num6 = 2

cubed = num6 ** num5
print(cubed) #8

#shorthand cubed

cubed **= 3
print(cubed) #512
