import random

색깔 = "\033["
배경 = "\033["
초기화 = "\033[0m"
색1 = random.randint(30, 38)
if 색1 == 38:
    색2 = random.randint(40, 48)
    if 색2 == 48:
        print("그냥 아무렇게")
    배경 = 배경 + str(색2) + "m"
    print(배경, "배경색만 있는 나", 초기화)
else:
    색깔 = 색깔 + str(색1) + "m"
    색2 = random.randint(40, 48)
    if 색2 == 48:
        print(색깔, "글자색만 있는 나", 초기화)
    else:
        배경 = 배경 + str(색2) + "m"
        print(색깔, 배경, "글자색 배경색 모두 있는 나", 초기화)