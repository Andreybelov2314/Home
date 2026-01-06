import csv
def max_and_min_atten(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        data=csv.DictReader(f)
        maxm=0
        minm=100
        maxn=''
        minn=''
        for i in data:
            if int(i['attendance'])>int(maxm):
                maxm=i['attendance']
            if int(i['attendance'])<int(minm):
                minm=i["attendance"]
        f.seek(0)
        data=csv.DictReader(f)
        for i in data:
            if int(i['attendance']) == int(maxm):
                maxn=i['name']
                break
        f.seek(0)
        data=csv.DictReader(f)
        for i in data:
            if int(i['attendance']) == int(minm):
                minn = i['name']
                break
    return (f'минимальная посещаемость-{minn}:{minm} \n'
            f'максимальная посещаемость-{maxn}:{maxm}')
print(max_and_min_atten('C:\\Users\\andre\\Documents\\Py_files\\employees.csv'))