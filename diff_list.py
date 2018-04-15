# filename: diff_list.py
# 2018-04-15
# Author: Corineru


def difflist(A, B):
    #'''求两个数组的交集'''
    interA_B = list(set(A).intersection(set(B)))

   #'''求两个数组的并集'''
    unionA_B = list(set(A).union(set(B)))

   #'''求两个数组的差集'''
    diffA_B = list(set(A).difference(set(B)))
    diffB_A = list(set(B).difference(set(A)))
   
    return interA_B, unionA_B, diffA_B,diffB_A

#test
A = [1, 3, 4, 5,6]
B = [3,4,5,7]
interA_B, unionA_B, diffA_B, diffB_A= difflist(A, B)
print('interA_B, unionA_B, diffA_B, diffB_A:', interA_B, unionA_B, diffA_B, diffB_A)


