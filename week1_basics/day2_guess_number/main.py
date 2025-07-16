import random

def guess_number_game():
    print("欢迎来到猜数字游戏！")
    num = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_num = int(input("请输入1-100之间的数字："))
            attempts += 1
            
            if user_num < 1 or user_num > 100:
                print("请输入有效范围内的数字！")
                continue
                
            if user_num > num:
                print("偏大")
            elif user_num < num:
                print("偏小")
            else:
                print(f"恭喜你猜中啦！共用了{attempts}次")
                break
                
        except ValueError:
            print("请输入整数！")

if __name__ == "__main__":
    guess_number_game()
