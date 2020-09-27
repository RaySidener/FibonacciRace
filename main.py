import multiprocessing
import time

rtfive = 2.2360679775

#how to allocate arrays?
def Fibo1(n, arr):
    arr[0] = 0
    if (n > 1):
        arr[1] = 1
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
    return arr

def getVal(i, arr=None):
    '''Returns the ith value of the fibo sequence. Fills arr[i] with this value
    if parameter arr is provided.'''
    if i == 0:
        val = 0
    elif i == 1:
        val = 1
    else:
        val = ((1+rtfive)/2)**i-((1-rtfive)/2)**i
        val = val/rtfive
        val = int(val)
    if arr:
        arr[i] = val
    return val

def Fibo2(n, arr):
    processes = []
    for i in range(n):#TODO maybe set this up to have 4 processes each doing a quarter of the work
        p = multiprocessing.Process(target=getVal, args=(i,arr,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    return arr

def main():
    n = 100
    arr1 = [None] * n
    man = multiprocessing.Manager()
    arr2 = man.list(range(n))
    t1 = time.time()
    arr1 = Fibo1(n, arr1)
    t2 = time.time()
    arr2 = Fibo2(n, arr2)
    t3 = time.time()
#    for i in range(10):
#        print(str(arr1[i]))
#        print(str(arr2[i]))
    print("N = " + str(n))
    print("Fibo1 time: " + str(t2-t1))
    print("Fibo2 time: " + str(t3-t2))
if __name__ == "__main__":
    main()
