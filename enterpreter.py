expreesion = input('expreesion: ')
x,y,z = expreesion.split()
x = float(x)
z = float(z)
if y=='-':
    print(x-z)
elif y=='+':
    print(x+z)
elif y=='*':
    print(x*z)
elif y=='/':
    print(x/z)