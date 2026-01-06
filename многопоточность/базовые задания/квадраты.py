import threading

res = {}
#потоки не могут напрямую работать с return->
def calculate_result(num):
    result = num * num
    res[num]=result
    return result
def proc():
    while True:
        dec=int(input('введите цифру для возведения в степень'))
        if dec==0:
            break
        else:
            t=threading.Thread(target=calculate_result,args=(dec,))
            t.start()
            t.join()
    return res
def proc_rng(num):
    for i in range(num, num+5):
        t=threading.Thread(target=calculate_result,args=(i,))
        t.start()
    return res
print(proc_rng(125))

