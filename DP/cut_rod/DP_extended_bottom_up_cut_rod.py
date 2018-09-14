def extended_bottom_up_cut_rod(p, n):
    s, r = [0 for _ in range(n+1)], [-1 for _ in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        # q = float("-inf")
        q = -1
        for i in range(1, j+1):
            if q < p[i-1] + r[j-i]:
                q = p[i-1] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    import time
    print('When n = %d' % 10)
    start = time.clock()
    # print('We can get q = ' + extended_bottom_up_cut_rod(p, 10))
    print(extended_bottom_up_cut_rod(p, 10))
    end = time.clock()
    print('running time t = %e' % (end-start))
    print(print_cut_rod_solution(p, 9))
