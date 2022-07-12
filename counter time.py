import time
def countdown(t):
    while t > 0:
        print(t)
        t = t-1
        time.sleep(1)
    print("OFF!")

print("How many seconds? Enter a digit:")
seconds = input()
seconds = int(seconds)
countdown(seconds)