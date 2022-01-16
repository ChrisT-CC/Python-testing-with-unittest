""" declare the function to be tested """


def even_number_of_evens(numbers):
    """
    Our function should raise a "TypeError" if a list is not passed into the
    function error message: "A list was not passed into the function"
    if numbers is empty, return False when
    if number of even numbers is odd, return False
    if number of even numbers is 0, return False
    if number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        # if numbers == []:
        #     return False
        # else:

        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1

        evens = evens = sum([1 for n in numbers if n % 2 == 0])

        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
        # convert to single line conditional expression
        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens(5))
