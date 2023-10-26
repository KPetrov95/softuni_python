from collections import deque

DAYS = 7
food_portions = deque(int(x) for x in input().split(', '))
stamina_portions = deque(int(x) for x in input().split(', '))
conquered_peaks = []
result = []
peaks_dict = {
    80: 'Vihren',
    90: 'Kutelo',
    100: 'Banski Suhodol',
    60: 'Polezhan',
    70: 'Kamenitza',
            }
peaks_values = deque(int(x) for x in peaks_dict.keys())

for i in range(DAYS):
    if not peaks_values:
        break
    current_peak = peaks_values.popleft()
    energy = food_portions.pop() + stamina_portions.popleft()
    if energy >= current_peak:
        conquered_peaks.append(peaks_dict[current_peak])
    else:
        peaks_values.appendleft(current_peak)

if peaks_values:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:

    result.append('Conquered peaks:')
    for peak in conquered_peaks:
        result.append(peak)
    print(f"\n".join(result))