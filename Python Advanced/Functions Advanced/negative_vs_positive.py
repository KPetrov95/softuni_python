neg = 0
pos = 0
nums = [int(x) for x in input().split()]

for num in nums:
    if num < 0:
        neg += num
    else:
        pos += num

print(neg)
print(pos)
if abs(neg) > pos:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")