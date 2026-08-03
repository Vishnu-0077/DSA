def dfs(start,stop,letter_list,word_list,visited,count):
    if start == stop:
        return count
    visited.add(start)
    mini = float('inf')
    for letter in letter_list:
        for i in range(len(start)):
            start = list(start)
            prev = start[i]
            start[i] = letter
            start = list_to_string(start)
            if start in word_list and (start not in visited or start == stop):
                result = dfs(start,stop,letter_list,word_list,visited,count+1)
                mini = min(mini,result)
            else:
                start = list(start)
                start[i] = prev
                start = list_to_string(start)
    return mini
def list_to_string(lst):
    return ''.join(lst)

def main(start,stop,word_list):
    letter_list = []
    for word in word_list:
        for letter in word:
            if letter not in letter_list:
                letter_list.append(letter)
    
    visited = set()
    ans = dfs(start,stop,letter_list,word_list,visited,1)
    return ans

if __name__ == '__main__':
    start = 'der'
    stop = 'dfs'
    word_list = ["des","der","dfr","dgt","dfs"]
    print(main(start,stop,word_list))

