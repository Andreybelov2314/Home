import re
def text_analize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.read()
        qua=len(data)
        f.seek(0)
        text2=re.split(r"[., :;\n]", data)
        qua2=len(text2)
        f.seek(0)
        mw=''
        mc=0
        for i in text2:
            mc1=text2.count(i)
            if int(mc1)>mc:
                mw=i
                mc=mc1
            elif int(mc1)==mc and i not in mw.split(' '):
                mw+=i+' '
    return f'файл-{filename},количество символов-{qua}, количество слов-{qua2}, самое частое слово-{mw}'
def res_save(filename):
    info=text_analize(filename)
    with open('C:\\Users\\andre\\Documents\\Py_files\\file_info.txt', 'w', encoding='utf-8') as f:
        f.write(info+'\n')
res_save('C:\\Users\\andre\\Documents\\Py_files\\wishlist.txt')





