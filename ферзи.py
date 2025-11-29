queen=[]
while True:
    pos=int(input("введите положения для горизонтали, для окончания введите 0"))
    if pos==0:
        break
    pos2 = int(input("введите положение ферзя по горизонатли"))
    lst = [pos, pos2]
    queen.append(lst)




for i in queen:

    for j in queen:
        if i==j:
            pass
        elif i[0] == j[0] or i[1] == j[1]:
            print(f"ферзь{i} бьет ферзя {j} ")#проверяем, бьет ли ферзь по горизонтали или вертикали
        else:
            pass
for k in queen:#проверяем, бьет ли ферзь по диагонали
    for l in queen:
        if k!=l:
            if k[0] - k[1] == l[0] - l[1]:
                print(f"ферзь {k} бьет ферзя {l}")

















