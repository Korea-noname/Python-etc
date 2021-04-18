star = int(input())
increase = 1

for i in range(1, star + 1):
    for j in range(1, star):
        increase +=1
        if(increase <= i):
            print("*", end ='')
        else:
            print(sep='')
            increase = 0