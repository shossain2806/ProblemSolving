    
def sortedSum(a):
    # Write your code here
    length = len(a)
    final = 0
    stored = {}
    for n in range(length):
        if stored[n] == None:
            curr = list(a[0:n + 1])
            curr.sort() 
            res = 0
            for index, num in enumerate(curr):
                num1 = ((index + 1) * num) % (1000000000 + 7)
                num2 = res
                final = (final + ( (num1 + num2) % (1000000000 + 7))) % (1000000000 + 7)
            stored[n] = final
        else:
            final += stored[n]
    return final

print(sortedSum([4,3,2,1]))
print(sortedSum([9,5,8]))
print(sortedSum([5,9]))
# print(sum('123','123'))