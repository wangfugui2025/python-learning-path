while True:  # 添加循环确保输入合法
    try:
        height = float(input("请输入您的身高(m):"))
        weight = float(input("请输入您的体重(kg):"))

        # 检查正值
        if height <= 0 or weight <= 0:
            raise ValueError("身高和体重必须大于0")

        break  # 输入有效则退出循环

    except ValueError as e:
        print(f"输入错误: {e}")
        # 继续循环直到输入正确
BMI=weight/(height**2)
if BMI<18.5:
   category="偏瘦"
elif 18.5 <=BMI < 24:
    category = "正常"
else:
    category = "偏重"
print(f"您的BMI分类为:{category}")#  任务代码
