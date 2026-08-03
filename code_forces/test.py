

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mn = mx = 0  # before any turn, score is exactly 0

    for i in range(n):
        ai = a[i]
        bi = b[i]

        # compute new extremes after this turn
        new_mx = max(mx - ai, bi - mn)
        new_mn = min(mn - ai, bi - mx)

        mn, mx = new_mn, new_mx

    print(mx)
