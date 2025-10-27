kwh = float(input())
if kwh <= 120:
    bill = kwh * 0.53
elif 120>= kwh <= 180:
    bill = 50 * 0.53 + (kwh - 50) * 0.58
elif kwh <= 250:
    bill = 50 * 0.53 + 100 * 0.58 + (kwh - 150) * 0.82
else:
    bill = 50 * 0.53 + 100 * 0.58 + 100 * 0.82 + (kwh - 250) * 0.92
print(f"{bill:.2f}")