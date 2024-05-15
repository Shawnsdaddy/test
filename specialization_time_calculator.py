def calculate(level, match=False, efficient=0, left_hours=0, left_minutes=0, add_on=False, half_off=False):
    hour = 0
    if left_minutes > 0 or left_hours > 0:
        hour = left_minutes / 60 + left_hours
    # 基本5%
    basic = 5
    if add_on:
        # 阿斯卡伦
        basic += 5
    if hour == 0:
        hour = level * 8
    if half_off:
        hour = hour / 2
    left = 5 * (100 + basic + (30 if match else 0)) / 100
    left = hour - left
    res = left * 100 / (100 + efficient + basic) * 60
    print(f"倒计时{res // 60}小时{res % 60}分钟")
    print(f"请始终提前几分钟换人，避免艾丽妮工作时间不足5小时 ")


calculate(1, match=False, efficient=60, left_hours=0, left_minutes=0, add_on=False, half_off=True)
