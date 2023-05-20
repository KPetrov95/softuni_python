reps = int(input())
odd_flag = False
for i in range(reps):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        odd_flag = True
        break

if not odd_flag:
    print("All numbers are even.")