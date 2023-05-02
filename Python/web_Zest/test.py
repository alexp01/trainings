
xx = []
aa = ['2028', '2027', '2026', '2025', '2024', '✓\n2023', '2022', '2021', '2020', '2019', '2018']

for bb in aa:
    if "✓\n" in bb:
        year_value = bb[-4:]
    else:
        year_value = bb
    xx.append(year_value)

print(xx)