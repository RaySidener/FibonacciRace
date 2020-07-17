from multiprocessing import Pool


rtfive = 2.2360679775
#how to allocate arrays?
def Fibo1(n):
    arr = [None] * n
    arr[0] = 0
    if (n > 1):
        arr[1] = 1
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
    return arr

def getVal(i):#returns ith value of the fibo sequence
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        val = ((1+rtfive)/2)**i-((1-rtfive)/2)**i
        val = val/rtfive
        val = int(val)
        return val

def Fibo2(n):
    #arr = [None] * n
    with Pool(5) as p:
        arr = p.map(getVal, range(n))
    return arr

def main():
    n = 20
    arr1 = Fibo1(n)
    arr2 = Fibo2(n)
    for i in range(n):
        print(str(arr1[i]))
        print(str(arr2[i]))

if __name__ == "__main__":
    main()
