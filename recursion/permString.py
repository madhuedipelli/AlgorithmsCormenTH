def recPermute(soFar, rest):
    if rest == '':
        print(soFar)
    else:
        for i in range(len(rest)):
            next = soFar + rest[i]
            c_rest = rest[:i] + rest[i+1:]
            recPermute(next,c_rest)

recPermute('','abc')
