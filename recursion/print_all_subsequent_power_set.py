def power_sets(a,power_set=[]):
    if a not in power_set:
        power_set.append(a)
    for val in a:
        a_new=a.copy()
        a_new.remove(val)
        power_sets(a_new,power_set)
    return power_set
print(power_sets([1,2,3]))