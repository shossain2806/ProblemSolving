
def minTime(files, numCores, limit):
    # Write your code here
    res = 0
    files.sort(reverse=True)
    for file in files:
        if limit > 0:
            if file % numCores == 0:
                res += file / numCores
                limit -=1
            else:
                res += file
        else:
            res += file

    return int(res)

print(minTime([5,3,1], 5, 5))
print(minTime([3,1,5], 1, 5))
print(minTime([4,1,3,2, 8], 4, 1))
