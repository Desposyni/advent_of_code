from collections import Counter

with open('d3p1.in') as f:
    reports = f.read().split("\n")
backup_reports = reports[:]

def get_column(rows: list[str], idx: int) -> list[str]:
    column = [row[idx] for row in rows]
    column.sort(reverse=True)
    print(column)
    return column

def most_common(column: list[str]) -> str:
    most = Counter(column).most_common(1)[0][0]
    print(most)
    return most

def least_common(column: list[str]) -> str:
    least = Counter(column).most_common()[-1][0]
    print(least)
    return least

for i in range(len(reports)):
    if len(reports) == 1:
        break
    x = most_common(get_column(reports, i))
    reports = list(filter(lambda report: report[i] == x, reports))
    print(reports)
print(oxy:=int(reports[0], base=2))

reports = backup_reports[:]
for i in range(len(reports)):
    if len(reports) == 1:
        break
    x = least_common(get_column(reports, i))
    reports = list(filter(lambda report: report[i] == x, reports))
    print(reports)
print(co2:=int(reports[0], base=2))
print(oxy * co2)