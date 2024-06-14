expenses = [
    ["january","february","march","april","may"],
    [2200,2350,2600,2130,2190]
]

print(f"1:- {expenses[1][1] - expenses[1][0]}" )
i = 0
summation = 0
while i < 3:
    summation =  summation +  expenses[1][i]
    i = i + 1

print(summation)

# for expens in  expenses:
#     if expenses[1][expens] == 2000:
#         print("you have spent 2000")

if 2000 in expenses[1]:
    print("you have spent 2000")
expenses[0].append("june")
expenses[1].append(1980)
expenses[1].insert(3,expenses[1][3] - 200)
print(expenses[1][3])

