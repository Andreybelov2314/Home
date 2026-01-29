def val(age_str):
    try:
        age = int(age_str)
        if age >= 20 and age<=120 :
            return True
        else:
            return f'{False}, возраст должен быть от 20 до 120'
    except ValueError:
        print('Невозможно преобразовать в число')
print(val(50))
val('пятьдесят')
print(val(130))