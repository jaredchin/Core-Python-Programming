from functools import reduce
def average(numlist):
    sum = reduce(lambda x,y: x+y, numlist)
    return sum/len(numlist)




numlist = [1,2,3,4,5,6,7,8,9,10]
print(average(numlist))