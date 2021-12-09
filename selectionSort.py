#implementation of selection sort
#ascending order

def selectionSort(arr):
    for i in range(0,len(arr)):
        add=arr[i]
        index=i
        for j in range(i, len(arr)):
            if arr[j]<add:
                add=arr[j]
                index=j
        swap=arr[i]
        arr[i]=add
        arr[index]=swap
    return arr
        




if __name__ == '__main__':
    print("testcase 1: empty list.")
    print("expected output: []")
    print("actual output: " + str(selectionSort([])))

    print("")

    print("testcase 2: singleton list.")
    print("expected output: [-8]")
    print("actual output: " + str(selectionSort([-8])))

    print("")

    print("testcase 3: twin elements.")
    print("expected output: [-1, 0]")
    print("actual output: " + str(selectionSort([0,-1])))

    print("")
    
    print("testcase 4: twin equal elements.")
    print("expected output: [0, 0]")
    print("actual output: " + str(selectionSort([0,0])))

    print("")

    print("testcase 5: three equal elements.")
    print("expected output: [-9, -9, -9]")
    print("actual output: " + str(selectionSort([-9,-9,-9])))

    print("")
    
    print("testcase 6: sorted list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(selectionSort([-2,-1,0,1,2])))

    print("")

    print("testcase 7: reversed list.")
    print("expected output: [-2, -1, 0, 1, 2]")
    print("actual output: " + str(selectionSort([2,1,0,-1,-2])))

    print("")
    print("testcase 8: normalcy.")
    print("expected output: [-5, -2, -1, 0, 9, 10, 12]")
    print("actual output: " + str(selectionSort([0,12,9,10,-2,-1,-5])))

    print("END OF TEST CASES.")
