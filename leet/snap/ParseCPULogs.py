def parse(bursts):
    cpu_stack = []
    for burst in bursts:
        if burst[1] == 'true':
            cpu_stack.append(burst[0])
        elif burst[1] == 'false' and cpu_stack[-1] == burst[0]:
            temp = cpu_stack.pop()
            print(temp)


if __name__ == '__main__':
    f = open("cpulogs.log", 'r')
    logs = f.read()
    print(logs.split('\n'))
    bursts = []
    for log in logs.split('\n'):
        burst = log.split(' ')
        bursts.append(burst)
    parse(bursts)
