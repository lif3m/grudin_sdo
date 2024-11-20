from datetime import datetime
with open('supplier_b_import.txt','r',encoding='utf-8') as file:
    data=file.readlines()
for i in range(1,len(data)):
    result = []
    arr=data[i].split(",")
    #Наименование поставщика
    title=arr[0].strip()
    #Тип поставщика
    type_psot=arr[1].strip()
    result.append(title)
    result.append(type_psot)
    #ИНН
    inn=arr[2].strip()
    result.append(inn)
    #Рейтин качетва
    str=''
    rait=arr[3].strip()
    for char in rait:
        if char.isdigit():
            str+=char
    result.append(str)
    #Дата начала работы с поставщиком
    date = arr[4].strip()
    # try:
    #     date=datetime.strptime(date,'%Y-%m-%d')
    result.append(date)
    # except ValueError :
    #     if 'апрель' in date:
    #         date.replace('апрель', '04')
    print(result)
