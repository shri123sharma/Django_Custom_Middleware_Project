import random

my_list= ['shrikant',"arun",'pradeep','vishal','shrikant']

# Shuffle the list randomly
random.shuffle(my_list)

# Sample elements from the list to create pairs
sampled_elements = random.sample(my_list, len(my_list))

# Create pairs using zip()
pairs = list(zip(sampled_elements[::2], sampled_elements[1::2]))

# Print the pairs
print("Pairs:")
for pair in pairs:
    print(pair)


import random

# Define a list
my_list = [1, 2, 3, 4, 5]

# Generate a random index within the length of the list
random_index = random.randint(0, len(my_list) - 1)

# Replace the element at the random index with a new value
new_value = random.randint(6, 10)  # Generate a random value to replace
my_list[random_index] = new_value

# Print the updated list
print(my_list)

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [7]

result = [x for x in zip(list1, list2, list3)]

print(result)
