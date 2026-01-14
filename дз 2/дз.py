import csv
import json
def shop_info():
    with open('data.csv', 'r', encoding='utf-8', newline='') as f:
        data=csv.DictReader(f)
        date=input('Введите дату для отчетности (формат YYYY-MM-DD): ')
        s1 = 0
        s2 = 0
        dct={'Apple':0, 'Banana':0, 'Orange':0}
        for i in data:
            if i['Date']==date:
                if i['Store']=='Store_A':
                    upd=float(i['Price'])*int(i['Quantity'])
                    s1 = s1+upd
                elif i['Store']=='Store_B':
                    upd = float(i['Price']) * int(i['Quantity'])
                    s2 = s2 + upd
                upd=int(i['Quantity'])+int(dct[i['Product']])
                dct[i['Product']]=upd
        if s1 > s2:
            print(f"Наибольшие продажи за {date}: Store_A с объёмом продаж {s1:.0f}")
        elif s2 > s1:
            print(f"Наибольшие продажи за {date}: Store_B с объёмом продаж {s2:.0f}")
        else:
            print(f"Наибольшие продажи за {date}: Оба магазина с объёмом продаж {s1:.0f}")
        data2={
            date:[
                [
                    {
                        "product": "Apple",
                        "total_sales": dct.get('Apple',0)
                    },
                    {
                        "product": "Banana",
                        "total_sales": dct.get('Banana',0)
                    },
                    {
                        "product": "Orange",
                        "total_sales": dct.get('Orange',0)
                    }
                ]

            ]
               }
        with open('data.json','a', encoding='utf-8') as f:
            f.write(json.dumps(data2,ensure_ascii=False))

shop_info()

