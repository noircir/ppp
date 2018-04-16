# Joe's solution
def triple_and_filter(list_of_nums):
    return [item*3 for item in list(filter(lambda x:x%4 == 0,list_of_nums))]

# Colt's solution
def triple_and_filter2(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# my solution
def triple_and_filter3(l):
    return list(map(lambda x: x*3, filter(lambda x: x%4==0, l)))

print(triple_and_filter([4,16,24,7,9,11]))
print(triple_and_filter2([4,16,24,7,9,11]))
print(triple_and_filter3([4,16,24,7,9,11]))