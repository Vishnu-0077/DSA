def brute_force(divident,divisor):
    total=divisor
    count=0
    while total<=divident:
        total+=divisor
        count+=1
    return count

def optimal(divident,divisor):
    ans=0
    while divident>=divisor:
        shift=0
        while divident>=(divisor*(1<<shift)):
            shift+=1
        shift-=1 #here the value just goes above the limit, remember whenerver u use while loop
        divident-=(divisor*(1<<shift))
        ans+=(1<<shift)
    return ans


print(brute_force(22,5))
print(f"optimal solution is {optimal(27,5)}")

#if negative number exits, u can just add the nagative sign at the last using contitional statements

    