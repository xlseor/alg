#Implementation of quickSort
#12-15-21

def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivdex = len(arr)-1
    l=0
    r=pivdex-1
    while l<=r:
        while arr[r]>=arr[pivdex] and r>0:
            if r>0:
                r-=1
        while arr[l]<arr[pivdex]:
            l+=1
        if l<r:
            swap=arr[l]
            arr[l]=arr[r]
            arr[r]=swap

        else:
            break
            
    
    swap=arr[pivdex]
    arr[pivdex]=arr[l]
    arr[l]=swap
    
    a = quickSort(arr[:l])
    c = [arr[l]]
    b = []
    if l<pivdex:
        b = quickSort(arr[l+1:])
    to_ret =  a+c+b
    return to_ret

if __name__ == '__main__':
    print("testcase 1: empty list.")
    print("expected output: []")
    print("actual output: " + str(quickSort([])))

    
    print("")

    print("testcase 2: singleton list.")
    print("expected output: [-8]")
    print("actual output: " + str(quickSort([-8])))
    
    print("")
    
    print("testcase 3: twin elements.")
    print("expected output: [-1, 0]")
    print("actual output: " + str(quickSort([0,-1])))
    
    
    
    print("")
    
    print("testcase 4: twin equal elements.")
    print("expected output: [0, 0]")
    print("actual output: " + str(quickSort([0,0])))

    print("")

    
    print("testcase 5: three equal elements.")
    print("expected output: [-9, -9, -9]")
    print("actual output: " + str(quickSort([-9,-9,-9])))

    print("")

    
    print("testcase 6: sorted list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(quickSort([-2,-1,0,1,2])))

    print("")

    print("testcase 7: reversed list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(quickSort([2,1,0,-1,-2])))

    print("")
    print("testcase 8: normalcy.")
    print("expected output: [-5, -2, -1, 0, 9, 10, 12]")
    print("actual output: " + str(quickSort([0,12,9,10,-2,-1,-5])))

    print("END OF TEST CASES.")
