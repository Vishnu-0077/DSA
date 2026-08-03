def power_sets(a,power_set=[]):
    if a==[]:
        return
    if a not in power_set:
        power_set.append(a)
    for val in a:
        a_new=a.copy()
        a_new.remove(val)
        power_sets(a_new,power_set)
    return power_set

def sum_of_arr(arr,n=None):
    if n==None:
        n=len(arr)
    if n==1:
        return arr[0]
    return arr[n-1]+sum_of_arr(arr,n-1)

def combination_sum(ind_set,target):
    if sum_of_arr(ind_set)==target:
        print(ind_set)

if __name__== "__main__" :
    arr=[2,5,2,1,2]
    n=len(arr)
    target=5
    total_sets=power_sets(arr)
    for ind_set in total_sets:
        combination_sum(ind_set,target)
