expression = input("Expression: ")
x, y, z, = expression.split(" ")
float_x = float(x)
float_z = float(z)
if y == "+" :
    interpretation = float_x + float_z
elif y == "-" :
    interpretation = float_x - float_z
elif y == "*" :
    interpretation = float_x * float_z
elif y == "/" :
    interpretation = float_x / float_z
print(interpretation)