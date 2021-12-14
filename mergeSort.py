#implementation of mergeSort. (12-13-21)
#takes in an array
#sorts least to greatest


def mergeSort(arr):
    #base case:
    if len(arr)==1 or len(arr)==0:
        return arr
    #divide at midpoint:
    mid=len(arr)//2
    a=arr[:mid]
    b=arr[mid:]
    a=mergeSort(a)
    b=mergeSort(b)
    adex=0
    bdex=0
    for i in range(len(arr)):
        if adex==len(a):
            arr=arr[:i]+b[bdex:]
            break
        if bdex==len(b):
            arr=arr[:i]+a[adex:]
            break
        if a[adex]<b[bdex]:
            arr[i]=a[adex]
            adex+=1
        else:
            arr[i]=b[bdex]
            bdex+=1
    return arr
            
    
    
if __name__ == '__main__':
    print("testcase 1: empty list.")
    print("expected output: []")
    print("actual output: " + str(mergeSort([])))

    print("")

    print("testcase 2: singleton list.")
    print("expected output: [-8]")
    print("actual output: " + str(mergeSort([-8])))

    print("")

    print("testcase 3: twin elements.")
    print("expected output: [-1, 0]")
    print("actual output: " + str(mergeSort([0,-1])))

    print("")
    
    print("testcase 4: twin equal elements.")
    print("expected output: [0, 0]")
    print("actual output: " + str(mergeSort([0,0])))

    print("")

    print("testcase 5: three equal elements.")
    print("expected output: [-9, -9, -9]")
    print("actual output: " + str(mergeSort([-9,-9,-9])))

    print("")
    
    print("testcase 6: sorted list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(mergeSort([-2,-1,0,1,2])))

    print("")

    print("testcase 7: reversed list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(mergeSort([2,1,0,-1,-2])))

    print("")
    print("testcase 8: normalcy.")
    print("expected output: [-5, -2, -1, 0, 9, 10, 12]")
    print("actual output: " + str(mergeSort([0,12,9,10,-2,-1,-5])))

    print("END OF TEST CASES.")
