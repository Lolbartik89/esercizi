import time
timer = int(input("Enter seconds: "))
while timer > 0:
    minutes = timer // 60
    second = timer % 60
    time.sleep(1)
    print(f"{minutes:02d}:{second:02d}", end="\r")
    timer -= 1