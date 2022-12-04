#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?"

def two_add_up(lst, num):
    for i in lst:
        test = num - i
        if test in lst:
            return True
        else:
            return False

#test 1

lst = [10, 15, 3, 7]
num = 17
           
print(two_add_up(lst, num))

#test 2

lst = [20, 10, 30, 2]
num = 100

print(two_add_up(lst, num))
    
        
