#implementation of insertion sort. (12-14-21)

def insertionSort(arr):
    if len(arr)<=1:
        return arr
    for i in range(1, len(arr)):
        redex=i #reinsertion index
        k=i-1 #backiterator
        pull=arr[i]
        while k>=0:
            if arr[k]>pull:
                arr[k+1]=arr[k]
                redex=k
                k-=1
            else:
                break
        arr[redex]=pull
    return arr



    
    
if __name__ == '__main__':
    print("testcase 1: empty list.")
    print("expected output: []")
    print("actual output: " + str(insertionSort([])))

    print("")

    print("testcase 2: singleton list.")
    print("expected output: [-8]")
    print("actual output: " + str(insertionSort([-8])))

    print("")

    print("testcase 3: twin elements.")
    print("expected output: [-1, 0]")
    print("actual output: " + str(insertionSort([0,-1])))

    print("")
    
    print("testcase 4: twin equal elements.")
    print("expected output: [0, 0]")
    print("actual output: " + str(insertionSort([0,0])))

    print("")

    print("testcase 5: three equal elements.")
    print("expected output: [-9, -9, -9]")
    print("actual output: " + str(insertionSort([-9,-9,-9])))

    print("")
    
    print("testcase 6: sorted list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(insertionSort([-2,-1,0,1,2])))

    print("")

    print("testcase 7: reversed list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(insertionSort([2,1,0,-1,-2])))

    print("")
    print("testcase 8: normalcy.")
    print("expected output: [-5, -2, -1, 0, 9, 10, 12]")
    print("actual output: " + str(insertionSort([0,12,9,10,-2,-1,-5])))

    print("END OF TEST CASES.")
