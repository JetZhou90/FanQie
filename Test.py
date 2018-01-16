import numpy as np

# Q1
# def swap(lt,a,b):
#     c=lt[a]
#     lt[a]=lt[b]
#     lt[b]=c
#     return lt
#
# result=[]
# def perm(lt,k,m):
#     if k>m:
#         item=''.join(str(e) for e in lt)
#         result.append(item)
#     else:
#         for i in range(m+1):
#             lt=swap(lt,k,i)
#             perm(lt, k+1, m)
#             t=swap(lt,k,i)
#
# test=[1,2,3,3]
# perm(test, 0, len(test)-1)
# result=np.array(result)
# print (np.unique(result))

# Q2

def edit_distance(word1, word2):
    dp = list(range(len(word1) + 1))
    col_index = 0
    for c in word2:
        col_index += 1
        prev = dp[0]
        for i in list(range(1, len(word1) + 1)):
            add = dp[i] + 1
            remove = dp[i - 1] + 1
            replace = prev if c == word1[i - 1] else prev + 1
            prev, dp[i] = dp[i], min(add, remove, replace)
        dp[0] = col_index
    return dp[-1]
print (edit_distance('SHello', 'Hiel'))

