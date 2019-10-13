# NewtonRapson Algorithm
# By Amila Pathirana
# Date 2019/10/13


def f(x):
    return x**2+1*x-42


for i in range(-20, 21):
    x = i
    F = (x*2)+1

    if(F == 0):
        print('No output for input: ', x)
        x = x+1

    f1 = (x*2)+1
    tol = 100
    y = x - f(x)/(f1)
    count = 0
    while(abs(tol) > 10**(-5)):
        # https://wiki.openelectrical.org/index.php?title=Newton-Raphson_Power_Flow equation 4
        y = x - (f(x)/f1)
        tol = y - x
        x = y
        count += 1
        if(abs(y) > 10**10):
            print("y is too big for i = ", i)
            count = 0
            break
        if(count == 10000):
            print('no output or input', i)
            count = 0
            break
        if(f1 == 0):
            i = i+1
            print('derivative error')
            count = 0
            break
    print("for initial value ", i, " The Root is ", y, "Total iteration", count)
