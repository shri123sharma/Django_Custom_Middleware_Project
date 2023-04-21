# PROGRAM -1
# import random
# l = ['shrikant',"arun",'pradeep','vishal']
# pairs = {}
# while len(l) > 1:
#     r1 = random.randrange(0, len(l))
#     elem1 = l.pop(r1)

#     r2 = random.randrange(0, len(l))
#     elem2 = l.pop(r2)

#     pairs[elem1] = elem2
# i = 1
# for key, value in pairs.items():
#     print(" {}-to-{} ".format( key, value))

# PROGRAM -2
# my_list= ['shrikant',"arun",'pradeep','vishal']
# pairs = []
# for i in range(len(my_list)):
#     for k in range(i+1,len(my_list)):
#         if i != k:  
#             pairs.append((my_list[i], my_list[k]))

# print("Pairs:")
# for pair in pairs:
#     print(pair)

# PROGRAM -3
  
from itertools import compress
import random
import pdb;pdb.set_trace()
my_list= ['shrikant',"arun",'pradeep',]
my_list_1=random.sample(my_list, len(my_list))

print ("The original list is : " + str(my_list_1))
res = list(zip(my_list_1, my_list_1[1:] + my_list_1[:1]))
print ("The pair list is : " + str(res))










