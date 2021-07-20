def process_number_sum(array):
    left = 0
    right = len(array) - 1
    leftSum, rightSum = array[left], array[right]
    finished = False
    while left <= right and not finished:
        if rightSum == leftSum and left == right:
            finished = True
        elif rightSum == leftSum:
            left += 1
            right -= 1
            leftSum += array[left]
            rightSum += array[right]
        elif leftSum < rightSum:
            left += 1
            leftSum += array[left]
        elif rightSum < leftSum:
            right -= 1
            rightSum += array[right]
    return left, leftSum, array[:left + 1], array[-(len(array) - left):]