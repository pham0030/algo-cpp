# python3
import sys
import os
import time


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    # Simple Test
    # text = '[](()'

    stack = []
    flag = True
    for i, char in enumerate(text):
        if char == '(' or char == '[' or char == '{':
            stack.append(Bracket(char, i+1))
        elif char != ')' and char != ']' and char != '}':
            continue
        else:
            if len(stack) == 0:
                flag = False
                break
            top = stack.pop()
            if not top.Match(char):
                flag = False
                break
    if not flag:
        print(i+1)
    elif len(stack) != 0:
        print(stack[-1].position)
    else:
        print('Success')

    # Testing all cases in supplied folder
    # time_limit = 5.0  # seconds
    # max_time_used = 0.0  # seconds
    # cwd = os.getcwd()
    # cases = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # for i in range(10, 55):
    #     cases.append(str(i))

    # for c in cases:
    #     print('-'*20)
    #     print('Test case: {}'.format(c))
    #     text_path = os.path.join(cwd, 'tests/', c)
    #     # print(text_path)
    #     t = open(text_path)
    #     text = t.read()
    #     t.close()

    #     result_path = text_path + '.a'
    #     crf = open(result_path)
    #     cr = crf.read()
    #     crf.close()

    #     t0 = time.time()

    #     stack = []
    #     flag = True
    #     for i, char in enumerate(text):
    #         if char == '(' or char == '[' or char == '{':
    #             stack.append(Bracket(char, i+1))
    #         elif char != ')' and char != ']' and char != '}':
    #             continue
    #         else:
    #             if len(stack) == 0:
    #                 flag = False
    #                 break
    #             top = stack.pop()
    #             if not top.Match(char):
    #                 flag = False
    #                 break
    #     if not flag:
    #         r = str(i+1)
    #     elif len(stack) != 0:
    #         r = str(stack[-1].position)
    #     else:
    #         r = 'Success'

    #     t = time.time() - t0
    #     if t > max_time_used:
    #         max_time_used = t

    #     if r != cr[:-1]:  # exclude '\n'
    #         print('Wrong!')
    #         print('Your output: {}'.format(r))
    #         print('Correct output: {}'.format(cr))
    #         break
    #     elif max_time_used > time_limit:
    #         print('Too slow!')
    #         print('Running time: {}'.format(t))
    #         break
    #     else:
    #         print('Passed')

    #     # print('Running time: {}'.format(t))
    # print('-'*20)
    # print('Max time used: {}'.format(max_time_used))
