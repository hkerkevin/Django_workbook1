# class Reverse:
    #Just reverse the list of number without using reverse() method, slice is okay.
#     @staticmethod
#     def reverse(numbers):
#         """
#         :param numbers: (list of ints) The list of numbers.
#         """
#         numbers = numbers[::-1]
#         for num in numbers:
#             return numbers
        

# print(Reverse.reverse([3, 5, 1, 8, 2]))

# Part 2: Write a function that, when passed a list and a target sum, returns two distinct zero-based indices
# of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function return None
class TwoSum:
    
    @staticmethod
    def find_two_sum(numbers, target_sum):
        lst=[]
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1, -1, -1):
                if numbers[i] + numbers[j] == target_sum and i != j:
                    if (j, i) not in lst:
                        lst.append((i,j))
                    
        if lst == []:
            return None
        else:
            return lst

print(TwoSum.find_two_sum([3,1,5,7,5,9], 10))