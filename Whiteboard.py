# Implement a function to calculate the sum of the numerical values in a nested list. For example :
# sum_nested([1, [2, [3, [4]]]]) -> 10
# Some more test cases:
# sum_nested([])  ->  0
# sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]])   ->   8
# have to return the sum of all nested numbers 



def sum_nested(x):
    total = 0
    for i in x:
        if isinstance(i, int):
            total += i
        else:
            total += sum_nested(i)
        
    return total


print(sum_nested([1, [2, [3, [4]]]]))