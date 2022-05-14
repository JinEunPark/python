from 자료구조.minHeap import minheap

def make_tree(freq,n):
    min = minheap()
    
    for i in freq:
        min.insert(i)

    for i in range(0,n):
        m1 = min.delete()
        m2 = min.delete()
        min.insert(m1+m2)
        print("(%d + %d)"%(m1,m2))


