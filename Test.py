import numpy as np


#问题1答案
#采用递归算法进行排列组合
#参考文献：http://www.it610.com/article/2329814.htm
def swap(lt,a,b):
    c=lt[a]
    lt[a]=lt[b]
    lt[b]=c
    return lt

result=[]
def perm(lt,k,m):
    if k>m:
        item=''.join(str(e) for e in lt)
        result.append(item)
    else:
        for i in range(m+1):
            lt=swap(lt,k,i)
            perm(lt, k+1, m)
            t=swap(lt,k,i)
            
test=[1,2,3,3]
perm(test, 0, len(test)-1)
result=np.array(result)
print np.unique(result)


#问题2答案
#采用动态规划求最短编辑距离
#在由 Sm   转换的字符串 Dn-1 的末尾增加一个字符，编辑长度计 1，即 C’mn = Cm n-1 + 1；
#在由 Sm-1 转换的字符串 Dn   的末尾删去一个字符，编辑长度计 1，即 C”mn = Cm-1 n + 1；
#在由 Sm-1 转换的字符串 Dn-1 的末尾修改一个字符，编辑长度计 1，即 C”’mn = Cm-1 n-1 + 1
#在由 Sm-1 转换的字符串 Dn-1 的末尾字符相同不修改，无需增加，  即 C”’mn = Cm-1 n-1
#由于编辑距离有路径最短的要求，必须在每一步转换中选择编辑长度最短的方案，以达到局部最优解。
#因此，Cmn 最终的结果可表示为 Cmn = min(C’mn, C”mn, C”’mn)，min(a, b, c) 
#表示取 a, b, c 中最小的数。
#因为 Cmn 的结果只与 Cm-1 n、Cm n-1 和 Cm-1 n-1 三个数有关，所以上述式子构成解决编辑距离问题的递推关系。#
#参考文献：http://luodichen.com/blog/?p=410 

def edit_distance(word1, word2):
    dp = range(len(word1) + 1)
    col_index = 0
    for c in word2:
        col_index += 1
        prev = dp[0]
        for i in xrange(1, len(word1) + 1):
            add = dp[i] + 1
            remove = dp[i - 1] + 1
            replace = prev if c == word1[i - 1] else prev + 1
            prev, dp[i] = dp[i], min(add, remove, replace)
        dp[0] = col_index
    return dp[-1]
print edit_distance('SHello', 'Hiel')

