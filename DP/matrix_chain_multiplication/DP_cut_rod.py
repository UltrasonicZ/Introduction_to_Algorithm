def cut_rod(p, n):
    if n == 0:
        return 0
    # q = float("-inf")
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n-i))
    return q


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    import time
    start = time.clock()
    print(cut_rod(p, 10))
    end = time.clock()
    print(end-start)
