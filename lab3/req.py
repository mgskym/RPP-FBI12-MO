import requests

# 1.1
requst = requests.get('http://127.0.0.1:5000/number?param=8')
a = requst.json()["number"]

# 1.2
requst = requests.post('http://127.0.0.1:5000/number', json={
    "jsonParam": 8
})
b = requst.json()["number"]
operation_b = requst.json()["operation"]

# 1.3
requst = requests.delete('http://127.0.0.1:5000/number', json={
    "jsonParam": 8
})
c = requst.json()["number"]
operation_c = requst.json()["operation"]

# 1.4
def operations(a, b, operation):
    if operation == 'sum':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    else:
        if b == 0:
            return 'Ошибка: Деление на 0'
        else:
            return a / b

if operation_c == 'mul' or operation_c == 'div':
    result = operations(a, operations(b, c, operation_c), operation_b)
else:
    result = operations(operations(a, b, operation_b), c, operation_c)

print(f'Выражение: {a} {operation_b} {b} {operation_c} {c}')
print(f'Результат: {int(result)}')

# 3 задание

# 1. curl -X GET http://127.0.0.1:5000/number?param=8
# 2. curl -XPOST -d "{\"jsonParam\": 8}" -H "Content-Type: application/json" http://127.0.0.1:5000/number
# 3. curl -XDELETE -d "{\"jsonParam\": 8}" -H "Content-Type: application/json" http://127.0.0.1:5000/number
# 4.