#
# def combine(n: int, k: int):
#     def solu(n: int, k: int):
#         """The last line is the Pascal formula: https://en.wikipedia.org/wiki/Pascal's_triangle
#         solu(n-1,k) is sets of combination of selecting k item from first n-1 item,
#          [i+[n] for i in solu(n-1,k-1)] is sets of combination of selecting k-1 item from n-1 item,
#          and the k'th item would be n'th item"""
#         if k == 1: return [[i + 1] for i in range(n)]
#         if n == k: return [[i + 1 for i in range(n)]]
#         return solu(n - 1, k) + [i + [n] for i in solu(n - 1, k - 1)]
#     return solu(n, k)
#
# def reverse1(self, x: int):
#     """
#     Given a signed 32-bit integer x,
#     return x with its digits reversed.
#     If reversing x causes the value to go outside
#     the signed 32-bit integer range [-231, 231 - 1],
#     then return 0.
#     """
#     dig = 1
#     res = 0
#     if x < 0:
#         negativ e =1 x*=-1
#     e lse:
#         negative=0
#     w h ile 1*10**dig <= x:
#         dig+=1
#     fo r i in range(dig-1,-1,-1):
#         res += (x%10)*10**i
#         x //=10
#     i f n egative == 1:
#         res*=-1
#     re tu rn res if res <= 2**31-1 and res > = -2**31 else 0