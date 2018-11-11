# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    # print(numbers)
    first_max = numbers.pop(numbers.index(max(numbers)))
    # print(first_max)
    second_max = max(numbers)
    # print(second_max)
    max_product = first_max * second_max
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
