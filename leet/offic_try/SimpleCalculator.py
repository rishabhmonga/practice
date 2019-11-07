ops = {'*', '/'}


def calculate_exp(exp):
    exp_stack = []
    idx = 0
    while idx < len(exp):
        if exp[idx] not in ops and exp[idx] is not ' ':
            exp_stack.append(exp[idx])
        elif exp[idx] in ops:
            if exp[idx] is '*' or exp[idx] is '/':
                num1 = exp_stack.pop()
                num2 = exp[idx + 1]
                if exp[idx] is '*':
                    res = int(num1) * int(num2)
                else:
                    res = int(num1) / int(num2)
                exp_stack.append(res)
                idx += 1
        idx += 1

    res = 0
    idx = 0
    while idx < len(exp_stack):
        num1 = exp_stack.pop()
        if len(exp_stack) > 1:
            op = exp_stack.pop()
            num2 = exp_stack.pop()
            if op is '-':
                res += int(num1) - int(num2)
            elif op is '+':
                res += int(num1) + int(num2)
        else:
            res += int(num1)
        idx += 1
    return res


if __name__ == '__main__':
    print(calculate_exp('1+1-4+8'))
