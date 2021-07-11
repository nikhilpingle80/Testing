# def foo(n):
#     if (n == 0):
#         return 0

#     s = 0
#     while (n != 1):
#         if (n%2 == 0):
#             n = n/2
#             print(int(n))
#             s=s+1
#         else:
#             print(int(18446744073709551615 - (2*n)-1))
#             if (n <= 18446744073709551615 - (2*n)-1):
#                 n = (3*n)+1
#                 print(int(n))
#                 s=s+1
#             else:
#                 return 0
        
#     return s            
import math
x = math.pow(2, 63)
x = x-1
print(int(x))