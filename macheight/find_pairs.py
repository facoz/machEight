def find_pairs(input_list, target_sum):
    num_dict = {}
    pairs = []

    for i, num in enumerate(input_list):
        complement = target_sum - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = i

    return pairs


lists = input("Enter the numbers separated with comma: ")

numbers = map(int, lists.split(","))
target = int(input("Enter the target Number: "))
result = find_pairs(numbers, target)
print(result) 