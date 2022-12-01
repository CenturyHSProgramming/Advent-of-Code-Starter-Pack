""" main.py by Chris Winikka

Has some functions to get and process test and regular data for Advent of Code.
NOTE: this assumes the data is just a file of numbers.

I may add more sample projects for different types of data processing, but this
is it for now.
"""


def get_numbers(file: str) -> list:
    """ returns a list of each line in the file """
    file = open(file, 'r')
    numbers = file.readlines()
    file.close()
    return numbers


def strip_return(line: str) -> str:
    """ returns line in string form but without line return character """
    if '\n' in line:
        return str_to_int(line[:-1])
    else:
        return str_to_int(line)


def str_to_int(str_number: str) -> int:
    """ returns string number as an integer """
    return int(str_number)


def main():
    # get our list of integers
    # get test data (comment out when solving real solution)
    test_numbers = get_numbers("test.txt")
    test_number_list = list(map(strip_return, test_numbers))

    # get actual data for final answer
    numbers = get_numbers("inputs.txt")
    number_list = list(map(strip_return, numbers))
    
    # prove we have our numbers
    print(test_number_list)
    
    # loop through the data
    for i in number_list:
        print(i)
            

if __name__ == "__main__":
    main()