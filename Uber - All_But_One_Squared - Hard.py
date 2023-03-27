#This problem was asked by Uber

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

#with division
def all_but_one(lst):
    new_lst = []
    for i in range(len(lst)):
        product = 1
        for x in lst:
            product = product * x
        product = product / lst[i]
        new_lst.append(int(product))
    return new_lst

#test 1 - expected result [120, 60, 40, 30, 24]
lst = [1,2,3,4,5]

print(all_but_one(lst))

#test 2 - expected result [2, 3, 6]
lst = [3,2,1]

print(all_but_one(lst))      

#without division
def product_all_but_one(lst):
    new_lst = []
    prod_lst = []
    for i in range(len(lst)):
        temp_lst = []
        for y in lst:
            temp_lst.append(y)
        temp_lst.remove(temp_lst[i])
        prod_lst.append(temp_lst)
    for i in prod_lst:
        product = 1
        for x in i:
            product = product * x
        new_lst.append(product)
    return new_lst

#test 1 - expected result [120, 60, 40, 30, 24]
lst = [1,2,3,4,5]

print(product_all_but_one(lst))

#test 2 - expected result [2, 3, 6]
lst = [3,2,1]

print(product_all_but_one(lst))