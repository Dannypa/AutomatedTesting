import os
from colorama import Fore
import colors

SEPARATOR = '-' * 30


def read_multiple_lines() -> str:
    """Reads multiple lines input, ignoring empty lines and spaces in the beginning and in the end of the lines"""
    res = ""
    current_line = input()
    while current_line != 'arr':
        current_line = current_line.replace('\n', '').lstrip(' ').rstrip(' ')
        if not current_line:
            current_line = input()
            continue
        res += current_line
        res += '\n'
        current_line = input()
    return res


def get_program_answer(test: str) -> str:
    """Run program on test and returns what it's outputted"""
    with open("testing.in", 'w') as fin:
        fin.write(test)
    os.system("./testing.o")
    with open("testing.out", 'r') as fout:
        answer = ""
        for line in fout.readlines():
            current_line = line.replace('\n', '').lstrip(' ').rstrip(' ')
            if not current_line:
                continue
            answer += current_line
            answer += '\n'
    return answer


def print_test_case(test_case_number: int, test_case: str, answer: str, right_answer=None) -> None:
    """Prints test, program answer and right answer"""
    print(SEPARATOR)
    print(colors.color_test + f"Test case #{test_case_number}:\n" + test_case)
    print(Fore.RESET, end='')
    if right_answer:
        if answer == right_answer:
            color = colors.color_right
        else:
            color = colors.color_wrong
        print(color + "Answer:\n" + answer)
        color = colors.color_right
        print(color + "Right answer is:\n" + right_answer)
        if answer == right_answer:
            print(colors.color_right + "Yay!!")
        else:
            print(colors.color_wrong + "Bruh:(")
            print(colors.color_note + "May be there are multiple answers possible...")
        print(Fore.RESET, end='')
    else:
        print("Answer:\n" + answer)
    print(SEPARATOR)


def is_integer(a: str) -> bool:
    """Check if string can be converted to an integer"""
    digits = set("1234567890")
    for c in a:
        if c not in digits:
            return False
    return True


def build(cpp_name: str) -> None:
    """Copy the source c++ file into 'testing.cpp' with file IO added and build testing file."""
    with open(cpp_name, 'r') as fin, open("testing.cpp", 'w') as fout:
        fout.write("#include <cstdio>\n")
        for line in fin.readlines():
            fout.write(line)
            fout.write('\n')
            if "intmain(" in line.replace(' ', ''):
                fout.write('freopen("testing.in", "r", stdin);\n'
                           'freopen("testing.out", "w", stdout);\n')
    os.system("g++ testing.cpp -o testing.o")


def add_test(tests: list, test_case_number: int) -> None:
    """Reads test case and adds it to program"""
    print(f"Input test case {test_case_number}, please. In the end input 'arr' on a new line to continue.")
    current_test = read_multiple_lines()
    tests.append(current_test)
    print("Test added!")
    print()


def set_right_answer(test: str, test_case_number: int, answers: list) -> None:
    """Asks if program answer is correct, and if not, asks to input right answer"""
    answer = get_program_answer(test)
    print(f"Is that the answer to the test case #{test_case_number}?\n")
    print_test_case(test_case_number, test, answer)
    good = input("y/n >> ")
    if good.lower() == "y":
        answers.append(answer)
    else:
        print("Input correct answer, please. In the end input 'arr' on a new line to continue.\n>> ", end='')
        answers.append(read_multiple_lines())


def main():
    print("Hi! I'm a simple testing system!")
    print("I remember tests you've inputted and make it easier to retest your program - you don't have to copy and "
          "paste tests from site with a problem million times:)")
    print("Something about me:\n"
          "1. As it should be obvious from the name of repository, I work only with c++ files.\n"
          "2. The main method in your c++ file should start with 'int main(', without any additional words between "
          "those. Spaces are allowed:)\n"
          "3. I use file input/output for testing, so I most probably will work incorrectly if your program uses "
          "file IO.\n"
          "4. While testing, I am ignoring:\n"
          "\t•empty lines;\n"
          "\t•spaces in the end and in the beginning of the lines.\n"
          "5. You can change colors in 'colors.py'.")
    print("With that being said, good luck^)")
    print("Just do things I ask.")
    while True:
        name = input("Input full path to c++ file, please\n>> ")
        build(name)
        number_of_tests = input("How many tests will there be (number)?\n>> ")
        while not is_integer(number_of_tests):
            number_of_tests = input("Input a number, please!\n>> ")
        number_of_tests = int(number_of_tests)
        tests = []
        answers = []
        for i in range(number_of_tests):
            add_test(tests, i + 1)
            set_right_answer(tests[len(tests) - 1], i + 1, answers)
            if i != number_of_tests - 1:
                print("Moving to the next test!")
            else:
                print("All done!")
        while True:
            command = input("Now, input 'r' to rebuild and retest, 'c' to continue to the next problem,"
                            "'+' to add a test, or 'q' to quit.\n>> ")
            if command == 'q':
                print("Bye!!")
                exit(0)
            elif command == 'c':
                print("Ok, moving on!")
                break
            elif command == 'r':
                build(name)
                for i in range(number_of_tests):
                    test = tests[i]
                    answer = get_program_answer(test)
                    print_test_case(i + 1, test, answer, right_answer=answers[i])
            elif command == '+':
                add_test(tests, len(tests) + 1)
                test = tests[len(tests) - 1]
                set_right_answer(test, len(tests), answers)
                number_of_tests += 1
                print("All done!")


if __name__ == '__main__':
    main()
