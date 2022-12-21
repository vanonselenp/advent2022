import json

example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

example2 = """[1,1,3,1,1]
[1,1,5,1,1]"""


# When comparing two values, the first value is called left and the second value is called right. Then:


# If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.

# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

# Using these rules, you can determine which of the pairs in the example are in the right order

def parse(input):
    lines = [pair for pair in input.split('\n\n')]
    pairs = [[eval(pair.split('\n')[0]), eval(pair.split('\n')[1])] for pair in lines]

    return pairs


def compare(left, right):
    # is_left_int = isinstance(left, int)
    # is_right_int = isinstance(right, int)

    for i in range(0, len(left)):
        print(left[i], right[i])
        # If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
        if left[i] < right[i]:
            return True

    return False

    


    # for index in len(left):
            

     

    # for i in range(0, len(left)):
        
    #     answer = True
    #     if isinstance(left[i], list) and isinstance(right[i], int):
    #         answer = compare(left[i], [right[i]])
        
    #     elif isinstance(right[i], list) and isinstance(left[i], int):
    #         answer = compare([left[i]], right[i])

    #     elif isinstance(left[i], list) and isinstance(right[i], list):
    #         answer = compare(left[i], right[i])

    #     elif left[i] > right[i]:
    #         answer = False

    #     if not answer:
    #         return False

    # return True

def main(input):
    compare_pairs = parse(input)

    for pair in compare_pairs:
        print(compare(pair[0], pair[1]))

    # print(json.dumps(compare_pairs, indent=2))

if __name__ == '__main__':
    main(example2)
    # main(example)