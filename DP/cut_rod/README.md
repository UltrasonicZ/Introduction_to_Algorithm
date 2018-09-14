Cut-Rod Problem
================================================================
## Top-Down Recursion(not DP)

the [DP_cut_rod.py](https://github.com/UltrasonicZ/Introduction-to-Algorithm/blob/master/DP/cut_rod/DP_cut_rod.py) implement the recursion of the cut-rod problem

 ```python
def cut_rod(p, n):
    if n == 0:
        return 0
    # q = float("-inf")
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n-i))
    return q
```

 ```python
When n = 10
We can get q = 30
running time t = 4.360000e-04
```

## Top-Down With Memoization

the [DP_memoized_cut_rod.py](https://github.com/UltrasonicZ/Introduction-to-Algorithm/blob/master/DP/cut_rod/DP_memoized_cut_rod.py) implement the recursion of the cut-rod problem

 ```python
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
```

 ```python
When n = 10
We can get q = 30
running time t = 3.600000e-05
```

## Bottom-up Method

the [DP_bottom_up_method.py](https://github.com/UltrasonicZ/Introduction-to-Algorithm/blob/master/DP/cut_rod/DP_bottom_up_method.py) implement the recursion of the cut-rod problem

 ```python
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
```

 ```python
When n = 10
We can get q = 30
running time t = 2.500000e-05
```
