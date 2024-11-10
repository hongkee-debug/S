print("1:正方形 2:长方形 3:三角形 4:圆形 5:梯形 6:正方体 7:长方体 8:计算器 9:猜数字游戏 10：四舍五入")  #10：数字炸弹 
n=int(input())
if n==1: #正方形
    print("边长：")
    a=int(input())
    print("面积：")
    print((a**2))
    print("周长：")
    print((4*a))
if n==2: #长方形
    print("长：")
    a=int(input())
    print("宽：")
    b=int(input())
    print("面积：")
    print((a*b))
    print("周长：")
    print((2*(a+b)))
if n==3: #三角形
    print("底：")
    a=int(input())
    print("高：")
    h=int(input())
    print("面积：")
    print((a*h/2))
    print("周长：")
    print((a+h+a))
if n==4: #圆形
    print("半径：")
    r=int(input())
    print("面积：")
    print((r**2)*3.14)
    print("周长：")
    print((2*3.14*r))
if n==5: #梯形
    print("上底：")
    a=int(input())
    print("下底：")
    b=int(input())
    print("高：")
    h=int(input())
    print("面积：")
    print(((a+b)*h/2))
    print("周长：")
    print((a+b+h+a))
if n==6: #正方体
    print("边长：")
    a=int(input())
    print("体积：")
    print((a**3))
    print("表面积：")
    print((6*a**2))
if n==7: #长方体
    print("长：")
    a=int(input())
    print("宽：")
    b=int(input())
    print("高：")
    h=int(input())
    print("体积：")
    print((a*b*h))
    print("表面积：")
    print((2*(a*b+a*h+b*h)))

if n==8: #计算器
    print("输入第一个数：")
    a=int(input())
    print("输入运算符：")
    b=input()
    print("输入第二个数：")
    c=int(input())
    if b=="+":
        print(a+c)
    if b=="-":
        print(a-c)
    if b=="*":
        print(a*c)
    if b=="/":
        print(a/c)
    if b=="%":
        print(a%c)
    if b=="**":
        print(a**c)
    if b=="//":
        print(a//c)
if n==9: #猜数字游戏
    print("输入一个数字：")
    a=int(input())
    print("输入一个数字：")
    b=int(input())
    if a==b:
        print("你赢了")
    else:
        print("你输了")
# if n==10: #数字炸弹游戏
#     import random

# def number_bomb_game():
#     target = random.randint(1, 100)  # 随机生成1到100之间的目标数字
#     attempts = 0  # 记录用户尝试的次数

#     print("欢迎来到数字炸弹游戏！")
#     print("我已经想好了一个1到100之间的数字，请你猜猜看。")

#     while True:
#         try:
#             guess = int(input("请输入你猜测的数字："))
#         except ValueError:
#             print("输入无效，请输入一个整数。")
#             continue

#         attempts += 1

#         if guess < target:
#             print("猜小了！")
#         elif guess > target:
#             print("猜大了！")
#         else:
#             print(f"恭喜你，猜对了！目标数字是 {target}，你用了 {attempts} 次尝试。")
#             break
# if __name__ == "__main__":
#     number_bomb_game()
if n==10: #四舍五入
    # 提示用户输入一个数字
    number = float(input("请输入一个数字："))

    # 对输入的数字进行四舍五入
    rounded_number = round(number)

    # 输出四舍五入后的结果
    print("四舍五入后的结果是：", rounded_number)
