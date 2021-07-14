# This was one of my first projects!
from datetime import datetime
import time
from time import sleep
import sys
import logging

class bcolors:
    OKGREEN = '\033[92m'; WARNING = '\033[93m';FAIL = '\033[91m';BOLD = '\033[1m';ENDC = '\033[0m';UNDERLINE = '\033[4m'
    HEADER = '\033[95m'

def calculating_anim(word):
    for letter in word:
        for character in letter:
            print(character, end='')
            sys.stdout.flush()
            sleep(0.05)

filename = 'user-input.txt'
game_count = 1
all_operators = ['|+|','|-|','|x|','|/|', '|^|']
total_elapsed = []
def operator_updater(all_operators):
    result = ''
    for operator in all_operators:
        result += operator + ''
    return result[:]

while True:
    try:
        time_start = time.time()
        start = datetime.now()
        start_dt = start.strftime("%d/%m/%Y %H:%M:%S")
        print(start_dt)

        print('---------')
        print('CALCULATE')
        print('---------')
        num1 = float(input("Input 1st Num: "))
        op = input(f"Input Operator {operator_updater(all_operators)}: ")
        num2 = float(input("Input 2nd Num: "))

        if op == "+":
            cal = lambda ans: num1 + num2
            calculating_anim(f'{bcolors.OKGREEN}Calculating...{bcolors.ENDC}\n')
            print(f'{num1} + {num2} = {cal(ans=num1 + num2)}')
        elif op == "-":
            calculating_anim(f'{bcolors.OKGREEN}Calculating...{bcolors.ENDC}\n')
            cal = lambda ans: num1 - num2
            print(f'{num1} - {num2} = {cal(ans=num1 - num2)}')
        elif op == "x":
            calculating_anim(f'{bcolors.OKGREEN}Calculating...{bcolors.ENDC}\n')
            cal = lambda ans: num1 * num2
            print(f'{num1} x {num2} = {cal(ans=num1 * num2)}')
        elif op == "/":
            calculating_anim(f'{bcolors.OKGREEN}Calculating...{bcolors.ENDC}\n')
            cal = lambda ans: num1 / num2
            print(f'{num1} / {num2} = {cal(ans=num1 / num2)}')
        elif op == "^":
            calculating_anim(f'{bcolors.OKGREEN}Calculating...{bcolors.ENDC}\n')
            cal = lambda ans: num1 ** num2
            print(f'{num1} ^ {num2} = {cal(ans=num1 ** num2)}')
        else:
            print(f"{bcolors.FAIL}INVALID OPERATOR")

        if input(f"Continue? {bcolors.OKGREEN}(Y/N){bcolors.ENDC}: ").lower() not in ["y", "yes"]:
            calculating_anim(f'{bcolors.WARNING}Closing...')
            time.sleep(2)
            break
        else:
            print('---------------')
            print('ADDITIONAL INFO')
            print('---------------')
            print(f'>Used {bcolors.HEADER} {game_count} {bcolors.ENDC} time(s)')
            game_count += 1
            time_end = time.time()
            time_elapsed = time_end - time_start
            print(f'>Time spent: {bcolors.UNDERLINE} {time_elapsed:.2f}s {bcolors.ENDC}')

    except ValueError as e_value_error:
        print(f"{bcolors.WARNING} INPUT ONLY NUMBERS {bcolors.ENDC}")
        print(f'>>>{bcolors.FAIL} INFO: {e_value_error} {bcolors.ENDC}<<<')
        logging.info(e_value_error)
    except ZeroDivisionError as e_zero_division:
        print(f'>>>{bcolors.WARNING} CANNOT DIVIDE 0 BY 0 {bcolors.ENDC}<<<')
        print(f'>>>{bcolors.FAIL} INFO: { e_zero_division} {bcolors.ENDC}<<<')
        logging.info(e_zero_division)
    except OverflowError as e_overflow:
        print(f"{bcolors.WARNING} RESULT IS TOO LARGE {bcolors.ENDC}")
        print(f'>>>{bcolors.FAIL} INFO: {e_overflow} {bcolors.ENDC}<<<')
        logging.info(e_overflow)
    except Exception as Unknown_Exception:
        print(f'{bcolors.WARNING} Unknown exception found: {Unknown_Exception} {bcolors.ENDC}')