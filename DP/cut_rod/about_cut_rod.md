Cut-Rod Problem
================================================================
## Top-Down Recursion

the [DP_cut_rod.py](https://github.com/UltrasonicZ/Introduction-to-Algorithm/blob/master/DP/cut_rod/DP_cut_rod.py) implement the recursion of the cut-rod problem
'''python
def cut_rod(p, n):
    if n == 0:
        return 0
    # q = float("-inf")
    q = 0
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n-i))
    return q
'''
