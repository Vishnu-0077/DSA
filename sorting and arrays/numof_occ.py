def hashing(array,n):
    hash_array = [False]*n
    for i in range(n):
        if hash_array[i]==True:
            continue
        count=1
        for j in range(i+1,n):
            if array[j]==array[i]:
                hash_array[j]=True
                count=count+1
        print(array[i], "occurs", count, "times")

hashing([5,10,15,5,10],5)