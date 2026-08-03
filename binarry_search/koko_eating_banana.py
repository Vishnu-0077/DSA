def brute_force(piles, h):
    """
    Brute force solution to find the minimum eating speed.
    """
    speed=[]
    i=0
    while i<=max(piles):
        i=i+1
        sum=0
        for j in range(len(piles)):
            sum=sum+(piles[j]//i)+(1 if (piles[j]%i)>0 else 0) #sum in the opt method also does the same logic
            if sum>h:
                break
        if sum<=h:
            speed.append(i)
    return min(speed) if speed else -1
print(brute_force([3,6,7,11],9))  # Output: 4

def binpilesy_search(piles,h):
    low=1
    high=max(piles)
    ans=0
    while low<=high:
        mid=(low+high)//2
        sum=0
        for j in range(len(piles)):
            sum += (piles[j] + mid - 1) // mid #read the question u will understand
            if sum>h:
                break
        if sum<=h:
            ans=mid
            high=mid-1 #we need the leastest value of mid.....
        else:
            low=mid+1
    return ans
print(binpilesy_search([3,6,7,11],9))  # Output