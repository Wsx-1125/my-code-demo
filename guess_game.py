import random

def guess_number_game():
    print("===== 猜数字小游戏 =====")
    print("我已经想好了一个1~100之间的整数，你来猜猜看！")
    secret_num = random.randint(1, 100)
    count = 0

    while True:
        try:
            user_input = input("\n请输入你猜的数字：")
            guess = int(user_input)
            count += 1

            if guess < secret_num:
                print("猜小了！再试试！")
            elif guess > secret_num:
                print("猜大了！再试试！")
            else:
                print(f"🎉恭喜你猜对啦！答案就是{secret_num}")
                print(f"你一共猜了 {count} 次")
                break
        except ValueError:
            print("❌输入无效！请输入一个整数！")

if __name__ == "__main__":
    guess_number_game()
