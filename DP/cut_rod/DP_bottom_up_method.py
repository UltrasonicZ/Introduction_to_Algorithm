def bottom_up_cut_rod(p, n):
    r = [-1 for _ in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        # q = float("-inf")
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    return r[n]


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    import time
    print('When n = %d' % 10)
    start = time.clock()
    print('We can get q = %d' % bottom_up_cut_rod(p, 10))
    end = time.clock()
    print('running time t = %e' % (end-start))
