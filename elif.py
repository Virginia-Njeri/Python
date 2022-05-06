x=range(1,100)
for y in x:
    if y%5==0 and y%6==0 and y%7==0 and y%9==0:
        print(f"{y} is divisible by all")
    elif y%5==0:
        print(f"{y} is divisible by 5")
    elif y%6==0:
        print(f"{y} is divisible by 6")
    elif y%7==0:
        print(f"{y} is divisible by 7")
    elif y%9==0:
        print(f"{y} is divisible by 9")
    else:
        print(f"{y} is not divisible by 2 or 3")
        