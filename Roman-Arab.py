number=(input("Enter a number:"))
roman={1:'I',5:'V',10:'X',50:'L',100:'C'}
arabic={'I':1,'V':5,'X':10,'L':50,'C':100}
roman_number=''
if len(number)==3:
    order=3
elif len(number)==2:
    order=2
else:
    order=1
for i in number:
    if order == 3:
        i = int(i)
        result = roman.get(100) * i
        roman_number = roman_number + str(result)
        order = order - 1
    elif order==2:
        i=int(i)
        result=roman.get(10)*i
        roman_number=roman_number+str(result)
        order = order - 1

    elif order==1:
        i=int(i)
        result=roman.get(1)*i
        roman_number=roman_number+str(result)
roman_2=roman_number
roman_number = roman_number.replace('IIIII', 'V')
roman_number = roman_number.replace('VIIII', 'IX')
roman_number = roman_number.replace('IIII', 'IV')
roman_number= roman_number.replace('XXXXX', 'L')
roman_number = roman_number.replace('LXXXX', 'XC')
roman_number= roman_number.replace('XXXX', 'XL')
print(roman_number)
arab_number=0
for i in roman_2:
    number=int(arabic.get(i))
    arab_number+=number
print(arab_number)


































