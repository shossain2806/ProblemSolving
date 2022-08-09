## bottom-up
def max_heapify(list, size, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2
    if left < size and list[left] > list[largest]:
        largest = left
        
    if right < size and list[right] > list[largest]:
        largest = right
    
    if largest != index:
        list[index], list[largest] = list[largest], list[index]
        max_heapify(list, size, largest)
    
    
items = [3,2,3,1,2,4,5,5,6]

## pick bottom parent
for indx in range(len(items) // 2 - 1, -1, -1):
    max_heapify(items, len(items), indx)
    
print(items)

for indx in range(len(items) - 1, 0 , -1):
    items[0], items[indx] = items[indx], items[0]
    max_heapify(items, indx, 0)
    
print(items)