def greater_element(n,arr):
    m=n+1
    while (m-n)!=len(arr):
        if arr[m%(len(arr))]>arr[n]:
            return arr[m%(len(arr))]
        m+=1


def next_greater_element(n,arr):
    stack = []
    for i in range(n):
        if greater_element(i,arr) is not None:
            stack.append(greater_element(i,arr))
        else:
            stack.append(-1)
    return stack

def monotonic_stack_solution(n,arr):
    stack = []
    ans = [-1]*n
    stack[-1] = arr[-1]
    for i in range(1,n+1):
        while stack and arr[-i]>=stack[-1]:
            stack.pop()
        if stack:
            ans[-i]=stack[-1] #if circular... if not circular... then set ans[-1] = 0
        stack.append(arr[-i])
    return ans
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        st = []
        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()


            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i % n])
        return nge #this is the one which is used in the striver



if __name__ == '__main__':
    arr = [1,2,3,4,3]
    n=len(arr)
    print(next_greater_element(n,arr))