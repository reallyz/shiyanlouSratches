import multiprocessing


def loop():
    x=2
    while 1:
        x=x**2
if __name__ == '__main__':
    '''
     This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable
    '''
    multiprocessing.freeze_support()
    multils=[]
    for t in range(multiprocessing.cpu_count()):
        multils.append(multiprocessing.Process(target=loop))

    for p in multils:
        p.start()