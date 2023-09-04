
def freq(*args):
    result=dict()
    for value in args:
        if not (value in result):
            result[value] = args.count(value)
    return result

def freq_test():
    f=freq(1,2,2,2,1,3,3,1,4,1,1,5,9,5,1)
    print(f)


if __name__ == "__main__":
    freq_test()