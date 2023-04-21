# # def palindrone(x):
# #     # import pdb;pdb.set_trace()
# #     for i in range(0,int(len(x))):
# #      if x[i]==x[len(x) - 1]:
# #         print('true')
# #     else:
# #         print('false')
# # palindrone("malyalam")

# # x=str(10)
# # for i in range(0,(len(x))):
# #    if x[i]==x[len(x)-1]:
# #     print('this is palindrone')
# #     break
# #    else:
# #      print('this is not palindrone')
# #      break
   
# # I  =           1
# # V   =          5
# # X    =         10
# # L     =        50
# # C      =       100
# # D       =      500
# # M        =     1000
  
# # s=('I', 'V', 'X', 'L', 'C', 'D', 'M')
# # sum=0
# # for i in s:
# #   print(i)

# # import roman
# # r1=roman.toRoman(1000)
# # print(r1)

# # def value(r):

# #   if r=="I":
# #     return 1

# #   if r=="V":
# #     return 5
  
# #   if r=="X":
# #     return 10
  
# #   if r=="L":
# #     return 50
  
# #   if r=="C":
# #     return 100
  
# #   if r=="D":
# #     return 500
  
# #   if r=="M":
# #     return 1000
  
# #   for i in r:
# #     print(i)
  
# # value("LVIII")

# # def isPalindrome(x):
# #         x=str(x)
# #         if x==x[::-1]:
# #             print('this is palindrone')
# #             print("true")
# #         else:
# #             print('this is not palindrone')
# #             print("false")
# # isPalindrome(121)

# # d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

# # def romanToInt(s):
# #     # import pdb;pdb.set_trace()
# #     res, p = 0, 'I'
# #     for value in s[::-1]:
# #         res, p = res - d[value] if d[value] < d[p] else res + d[value], value
# #     print(res)
# # romanToInt("MCMXCIV")

# # d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
# # def roman(s):
# #    import pdb;pdb.set_trace()
# #    res=0
# #    p="I"
# #    for value in s[::-1]:
# #       if d[value]<d[p]:
# #          res=res-d[value]
# #       else:
# #          res+d[value]
# #          res=value     
# # roman("MCMXCIV")

# # def main(s):
# #   d={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
# #   res,p=0,'I'
# #   for value in s[::-1]:
# #       res,p=res-d[value] if d[value]<d[p] else res+d[value],value
# #   # return res
# #   print(res)
# # main("MCMXCIV")
# # import os
# # strs = ["flower","flow","flight"]
# # # strs=["dog","racecar","car"]
# # Output="fl"
# # import pdb;pdb.set_trace()
# # if os.path.commonprefix(strs)=="":
# #     print("")
# # else:
# #     print(os.path.commonprefix(strs))

# # list1=[1,2,4]
# # list2=[1,3,4]
# # for i in list2:
# #   list1.append(i)
# # print(list1)
# # for item in range(0,len(list1)):
# #     for value in range(item+1,len(list1)):
# #       if list1[item]>list1[value]:
# #         list1[item],list1[value]=list1[value],list1[item]
# # print(list1)

# # s1="(",")","{","}","[","]"
# # s="(}"
# # for i in s1:
# #     if i in s:
# #         print("true")
# #         break
# #     else:
# #         print("false")      
# #     print(i)

# # list_1=[[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}]
# # for i in list_1:
# #     for j in i:
# #       print(j)


# # def unpack_nested(data):
# #     if isinstance(data, list):
# #         return [unpack_nested(item) for item in data]
# #     elif isinstance(data, tuple):
# #         return tuple(unpack_nested(item) for item in data)
# #     elif isinstance(data, dict):
# #         return {key: unpack_nested(value) for key, value in data.items()}
# #     else:
# #         # return data
# #         print(data)

# # # data = [1, 2, [3, 4, [5, 6, (7, 8)], 9], 10, {'a': 11, 'b': (12, [13, 14])}]
# # data=[[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}]
# # unpacked_data = unpack_nested(data)

# # data=[[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}]
# # # import pdb;pdb.set_trace()
# # if (data,list):
# #     for item in data:
# #         print(item)

# # data=[1,2,3,4,4,5,6,67,]
# # result=isinstance(data,list)
# # print(result)

# # data=[[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}]
# # import pdb;pdb.set_trace()
# # if isinstance(data,list):
# #     for item_list in data:
# #       print(list(item_list))
# # elif isinstance(data,tuple):
# #     for item_tuple in data:
# #       print(tuple(item_tuple))
# # elif isinstance(data,dict):
# #   for key,value in data.items():
# #     print(dict(key,value))
# # elif isinstance(data,set):
# #     for item_set in data:
# #       print(set(item_set))
# # else:
# #     print(data)

# # def Unpacking(data):
# #     for item in data:
# #       if isinstance(item,(list,tuple,set,dict)):
# #         for item_set in item:
# #            return Unpacking(item_set)
# # Unpacking([[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}])

# # data=[[1,{2,3,(4,)}],(15,6,{"data":7},"8"),{9:[10,11,(12,13)]}]
# # if isinstance(data,list):
# #     print([num for sublist in  data for num in sublist])

# def unpacking(data):
#       # import pdb;pdb.set_trace()
#       if isinstance(data,list):
#           l1=[]
#           for item in data:
#               l1.append(unpacking(item))
#           return l1

#       elif isinstance(data,tuple):
#           l2=[]
#           for item in data:
#               l2.append(unpacking(item))
#           return tuple(l2)
               
#       elif isinstance(data,set):
#           s1=set()
#           for item in data:
#               s1.add(unpacking(item))
#           return s1
  
#       elif isinstance(data,dict):
#           d1={}
#           for key,value in data.items():
#               d1[key]=unpacking(value)
#           return d1
        
#       else:
#           print(data)

# unpacking([[1,{2,3,(4,)}],(5,6,{"data":7},"8"),{9,(10,11,(12,13,))}])

# # def valid(str):
# #     # import pdb;pdb.set_trace()
# #     s1=[]
# #     d1={"(":")","{":"}","[":"]"}
# #     for item in str:
# #         print(item)
# #         if item in s1:
# #             s1.append(item)
# #             print("true")
# #     else:
# #         print('false')
# # valid("()")

# def valid( str1):
#     # import pdb;pdb.set_trace()
#     stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
#     for parenthese in str1:
#         if parenthese in pchar:
#             stack.append(parenthese)
#             print("true")
#         if len(stack) == 0 or pchar[stack.pop()] != parenthese:
#             print("false")
#     else:
#         return False
# valid("(]")


# def valid(sequence):
#     while True:
#             import pdb;pdb.set_trace()
#             if '()' in sequence :
#                 sequence = sequence.replace ( '()' , '' )
#                 return True
#             elif '{}' in sequence :
#                 sequence = sequence.replace ( '{}' , '' )
#                 return True
#             elif '[]' in sequence :
#                 sequence = sequence.replace ( '[]' , '' )
#                 return True
#             else :
#                 return not sequence

# if __name__ == '__main__':
#    sequence = '()'
# #    sequence = '()[]{}'
# #    sequence = '(]'

# valid(sequence)

# import itertools
# list_1=[["a","b","c"],["d","e","f"]]
# list_2=[]
# for i in list_1:
#     for j in i:
#         list_2.append(j)
# print(list_2)
# for i in itertools.combinations(list_2,2):
#     print(str(i))

# list_1=[["a","b","c"],["d","e","f"]]
# l1=[]
# for item in list_1:
#     print(item)
#     list_2.copy()
#     for value in item:
#         print(value)

# list1 = ["a","b","c"]
# list2 = ["d","e","f"]
# pairs = []
# for sublist in list1:
#     for item1 in sublist:
#         for item2 in list2:
#             pairs.append([item1, item2])
# print(pairs)
# for value in pairs:
#     print("".join(value))

# str="abbacmpabnva"

# def is_valid_parentheses(s):
#     import pdb;pdb.set_trace()
#     stack = []
#     mapping = {")": "(", "}": "{", "]": "["}
#     for char in s:
#         if char in mapping:     
#             if stack==None:
#                 if char == ')' or char == '}' or char == ']':
#                   stack.append(char)
#                   print("true")
#             if stack:
#                 top_element = stack.pop()
#                 if mapping[char] != top_element:
#                     # return False
#                     print("false")
#         else:
#             stack.append(char)
#     return True if not stack else False
# is_valid_parentheses("]")

# def valid_parentheses(s):
#     stack = []
#     for char in s:
#         if char == '(' or char == '[' or char == '{':
#             stack.append(char)
#         elif char == ')' and stack and stack[-1] == '(':
#             stack.pop()
#         elif char == ']' and stack and stack[-1] == '[':
#             stack.pop()
#         elif char == '}' and stack and stack[-1] == '{':
#             stack.pop()
#         else:
#             return False
#     return True if not stack else False
# valid_parentheses("{[]}")
