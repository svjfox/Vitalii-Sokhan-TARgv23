import json
# 1. Создайте файл json, в котором будет информация о вас: ФИО, возраст, наличие очков/линз.
# 2. Откройте файл и выведите информацию в консоль.
# 3. Внесите изменения в файл и сохраните.
# 4. Откройте файл и выведите информацию в консоль.
# 5. Внесите изменения в файл и сохраните.
# 6. Откройте файл и выведите информацию в консоль.


json_data = '{"name": "Vitalii", "age": 18, "on_prillid":true}'
data_= json.loads(json_data)
for id_,data in enumerate(data_):
    print(f'{id_} : {data}')
for key, value in data_.items():
    print(f'{key} : {value}')
print(data_)

data_1= json.loads(json_data)
print(data_1)