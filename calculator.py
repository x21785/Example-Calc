print('Calcualtor')
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

print('1.add')
print('2.sub')
print('3.mul')
print('4.div')

ch = input()
if ch in('1','2','3','4'):
    x = float(input("Num1:"))
    y = float(input("Num2:"))

if ch == '1':
    print(x,'+',y,'=',add(x, y))
elif ch == '2':
    print(x,'-',y,'=',sub(x, y))
elif ch == '3':
    print(x,'*',y,'=',mul(x, y))
elif ch == '4':
    print(x,'/',y,'=',div(x, y))
else:
    print('Invalid')