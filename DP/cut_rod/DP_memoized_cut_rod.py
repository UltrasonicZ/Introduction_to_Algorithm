def memoized_cut_rod(p, n):
    # r = [float("-inf") for _ in range(n+1)]
    r = [-1 for _ in range(n + 1)]

    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        # q = float("-inf")
        q = -1
        for i in range(1, n+1):
            q = max(q, p[i-1] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    import time
    print('When n = %d' % 10)
    start = time.clock()
    print('We can get q = %d' % memoized_cut_rod(p, 10))
    end = time.clock()
    print('running time t = %s' % (end-start))
