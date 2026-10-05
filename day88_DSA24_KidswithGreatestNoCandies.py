'''Problem 2: LeetCode 1431: Kids With the Greatest Number of Candies

Problem statement: You are given a list candies where each number is how many candies a kid currently has, and a number extra. For
each kid, check: if you give that kid all extra candies, would they have the most candies among all kids (greater than or equal to
the current maximum)? Return a list of True/False, one per kid.

Expected output:
candies = [2, 3, 5, 1, 3], extra = 3 -> [True, True, True, False, True] (kid 0: 2+3=5 which ties the max 5, so True; kid 3: 1+3=4 
which is less than 5, so False)
candies = [4, 2, 1, 1, 2], extra = 1 -> [True, False, False, False, False]
candies = [12, 1, 12], extra = 10 -> [True, False, True]
candies = [1], extra = 5 -> [True]'''

def greatesCandies(candies,extra):
    list1=[]
    maximum_no = max(candies)

    for kidsC in candies:
        kidsC = kidsC +extra

        if kidsC >= maximum_no:
            list1.append(True)
        else:
            list1.append(False)
    return list1
print(greatesCandies([2,3,5,1,3],3))
print(greatesCandies([4,2,1,1,2],1))
print(greatesCandies([12,1,12],10))
print(greatesCandies([1],5))
