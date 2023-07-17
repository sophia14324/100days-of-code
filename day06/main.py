def insertion_sort(A):
    for i in range (1, len(A)):

        # Store current element in a variable
        curNum = A[i]
        for j in range(i-1, 0, -1):
            
            # If the previous element is greater, shift it to the right
            if A[j] > curNum:
                A[j+1] = A[j]

            # If the previous element is smaller or equal, insert the current element at this position and break the loop
            else:
                A[j+1] = curNum
                break
A = [7,8,5,6,4,1,3]
print(insertion_sort(A))