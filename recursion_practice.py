NATO_DICT = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta'}


def flatten(item_sequences):
    if not item_sequences:
        return []

    if type(item_sequences[0]) == list:
        return flatten(item_sequences[0]) + flatten(item_sequences[1:])
    return [item_sequences[0]] + flatten(item_sequences[1:])


def degree_recursion(nb, degree):
    if degree == 1:
        return nb
    return nb * degree_recursion(nb, degree - 1)


def convert2natoalphabet_recursion(word):
    # base case
    if len(word) == 1:
        return NATO_DICT[word[0]]

    # recursion case
    tail = word[1:len(word)]
    return NATO_DICT[word[0]] + ' ' + convert2natoalphabet_recursion(tail)


def total_values_recursion(nbs):
    if len(nbs) == 1:
        return nbs[0]
    x = nbs.pop()
    return x + total_values_recursion(nbs)


def sum_recursion(nb):
    # base case
    if nb == 0:
        return nb
    # recursion case
    return nb + sum_recursion(nb - 1)


def factorial_recursion(nb):
    # base case
    if nb == 1:
        return nb
    # recursion case
    return nb * factorial_recursion(nb - 1)


def fibonacci_nb(nb):
    # base case
    if nb == 0:
        return 0
    if nb == 1:
        return 1
    # recursion case
    return fibonacci_nb(nb - 1) + fibonacci_nb(nb - 2)


def decimal2binary_recursion(nb):
    if int(nb) == 0:
        return '0'
    if int(nb) == 1:
        return '1'
    return str(nb % 2) + str(decimal2binary_recursion(nb // 2))


def greatest_common_divisor_recursion(a, b):
    if b == 0:
        return a
    c = a % b
    return greatest_common_divisor_recursion(b, c)


def main():
    print('sum_recursion func')
    print(sum_recursion(10))
    print('\nfactorial_recursion func')
    print(factorial_recursion(5))
    print('\nfibonacci_nb func')
    for i in range(5):
        print(fibonacci_nb(i))
    print('\ndecimal2binary func')
    print(decimal2binary_recursion(7)[::-1])
    print('\ntotal_values func')
    print(total_values_recursion([1, 1, 3]))
    print('\ngreatest_common_divisors_recursion func')
    print(greatest_common_divisor_recursion(36, 30))
    word = 'abc'
    print(convert2natoalphabet_recursion(word.upper()))
    print(degree_recursion(2, 3))
    print('\nflatten func')
    print(flatten([1, 2, [1, 2, [7, 8, 6, ['a', 'b']]]]))


if __name__ == '__main__':
    main()
