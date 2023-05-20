divisor = int(input())
boundary = int(input())
target_num = 0
result_target = 0
for i in range(boundary + 1):
    if i % divisor == 0:
        result = i / divisor
        if result > result_target:
            result_target = result
            target_num = i

print(target_num)