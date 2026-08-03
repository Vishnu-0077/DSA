def game(a, b, k=0, i=0, scores=None):
    if scores is None:
        scores = []

    scores.append(k)

    # BASE CASE: No more turns left
    if i >= len(a):
        return k   # return final score

    # Choices
    blue = k - a[i]
    red  = b[i] - k

    # Recursive calls
    best_blue = game(a, b, blue, i + 1, scores)
    best_red  = game(a, b, red,  i + 1, scores)

    # Return best of both choices
    return max(best_blue, best_red)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(game(a, b))
