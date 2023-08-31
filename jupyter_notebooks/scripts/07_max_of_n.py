total = int(input("total?"))
max=None
count=0
while count<total:
    count+=1
    number=int(input(f"number #{count}?"))
    if number>max or max==None:
        max=number

print(f"Max is {max}")
