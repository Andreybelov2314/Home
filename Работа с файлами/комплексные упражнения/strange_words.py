def strange_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data=f.readlines()
        normal=''
        strange=''
        for line in data:
            line2=line.split(' ')
            for i in line2:
                if 'ie' in i:
                    index=i.index('i')
                    if i[index-1]=='c':
                        strange+=i+' '
                    else:
                        normal+=i+' '
                elif 'ei' in i:
                    index = i.index('e')
                    if i[index - 1] != 'c':
                        strange += i + ' '
                    else:
                        normal += i + ' '
        return f'{strange}-{len(strange.split(' '))} {normal}-{len(normal.split(' '))}'




