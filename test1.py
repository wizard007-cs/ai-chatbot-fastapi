#!/usr/bin/env python3
'''
number = 7
guess =-1
print("猜数字游戏！")
while guess != number:
    guess = int(input("请输入一个数字："))
    if guess < number:
        print("太小了！")
    elif guess > number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
'''

def http_error(status):
    match status:
        case 400|401|403:
            return "错误的请求"
        case 404:
            return "未找到"
        case 500:
            return "服务器错误"
        case _:
            return "未知错误"

print(http_error(400))
print(http_error(404))
print(http_error(500))
print(http_error(123))

person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

for value in person.values():
    print(value)

string_1 = "Hello, World!"
for i, char in enumerate(string_1):
    print(f"Index {i}: {char}")

while True:
    print("\n ===菜单===")
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")
    choice = input("请输入你的选择(1-4): ")
    if choice == '4':
        print("退出程序。")
        break
    elif choice == '1':
        print("余额:10000元")
    elif choice == '2':
        amount = input("请输入存款金额：")
        print(f"已存款{amount}元")
    elif choice == '3':
        amount = input("请输入取款金额：")
        print(f"已取款{amount}元")
    else:
        print("无效的选择，请重新输入。")

print("程序结束。")