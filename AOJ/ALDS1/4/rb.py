# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B"

# Count the number of t's in S as C.

# Constraints: S is sorted ascend; n <= 100_000;
# q <= 50_000; 0 < s <= 10**9;
# 0 <= t <= 10**9;
# t's are never the same with each other.


def bs(arr, qrys):
    cnt = 0
    for qry in qrys:
        left = 0
        right = len(arr)
        while left < right:
            pnt = (left + right) // 2
            if arr[pnt] == qry:
                cnt += 1
                break
            elif qry < arr[pnt]:
                right = pnt
            else:
                left = pnt + 1
    return cnt


dev = 1
if dev:
    S = "0 0 0 0 2 3 3 3 4 5 6 7 8 8 8 9 9 9 10 11 11 12 12 12 12 13 13 7000000 500000000 1000000000"
    S = S.split()
    T = "2 0 5 11 3 16 4 6 1 10 7 14 15 7000000 9 5555555"
    T = T.split()

    c = bs(S, T)
    print(c)  # expect 11
