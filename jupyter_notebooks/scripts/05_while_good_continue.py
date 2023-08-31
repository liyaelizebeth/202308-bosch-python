n = int(input("n?"))
x=0
while x<n:
    x+=1
    if x%5==0:
        print(f'\tskipping {x}')
        continue
    print(x)
    