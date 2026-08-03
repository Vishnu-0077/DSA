#dirent for loops is easy, just loops and save... finish

def brute(student,cookies):
    if len(student)==0 or len(cookies)==0:
        return 0
    min_stu = min(student)
    min_coo = min(cookies)
    if min_coo>=min_stu:
        student.remove(min_stu)
        cookies.remove(min_coo)
        return 1 + brute(student,cookies)
    else:
        cookies.remove(min_coo)
        return brute(student,cookies)

#if u want to use proper recursion then use sort.....

def proper_rec(student,cookies):
    student = sorted(student)
    cookies = sorted(cookies)
    def rec(student,cookies,i,j):
        if i == len(student) or j == len(cookies):
            return 0
        if cookies[j]>=student[i]:
            return 1 + rec(student,cookies,i+1,j+1)
        else:
            return rec(student,cookies,i,j+1)
    return rec(student,cookies,0,0)
cookies = [1,2,3]
student = [1,2]
print(proper_rec(student,cookies))
    