sorted = []

def mergesort(list,left,right):
    if left <left:
        mid = (left+right)//2

        mergesort(list,left,mid-1)
        mergesort(list, mid,right)
        merge(list,left,mid,right)
def merge(list,left,mid,right):
    global sorted
    left_index = left
    right_index = mid +1
    new = left
    while left_index <= mid and right_index <=right:
        if list[left_index] > list[right_index]:
            sorted[new] = list[left_index]
            new ,left_index = new + 1, left_index + 1
        else:
            sorted[new] = list[right_index]
            new, right_index = new + 1, right_index + 1
    


