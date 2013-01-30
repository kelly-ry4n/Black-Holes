import itertools

def fileread(fname):

    with open(fname) as f:
        data = f.read()

    data = data.split('=')
    data = [i.strip() for i in data if i.strip() != [] and i.strip() != '']
    data = [i.split() for i in data if i.strip() != [] and i.strip() != '']

    data = list(itertools.chain.from_iterable(data))

    S=[]
    tmp=[]

    for i in data:
        if i == 'supercritical':
            S.append(tmp)
            tmp = []
        else:
            tmp.append(i)

    # Remove empty lists
    while True:
        try:
            S.remove([])
        except ValueError:
            break

    out = []

    for i in S:
        tmp = {}
        while i:
            tmp[i.pop()] = float(i.pop())
        out.append(tmp)

    return out


if __name__ == '__main__':
    data = fileread('attempt1mass3.log')
    print data
