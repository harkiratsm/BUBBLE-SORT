from random import randint
def bubble_sort(my_list):
    n=len(my_list)
    for i in range(n):
        for j in range(0,n-1-i):
            if my_list[j]>my_list[j+1]:
                my_list[j+1],my_list[j]=my_list[j],my_list[j+1]
    return my_list
my_list=[]
for i in range(0,100):
    n = random.randint(1,100)
    my_list.append(n)
print("BEFORE SORTING",my_list)
bubble_sort(my_list)
print("AFTER SORTING",my_list)
