total_ppl = int(input())
capacity = int(input())

full_courses = 0
partial_courses = 0

while total_ppl > 0:
    if total_ppl > capacity:
        total_ppl -= capacity
        full_courses += 1
    else:
        partial_courses += 1
        break

print(partial_courses + full_courses)