month = ["January", "February", "March", "April", "May"]

expenses = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?

# print("Expenses More : ", expenses[month.index(
    # "February")]-expenses[month.index("January")])

# Find out your total expense in first quarter (first three months) of the year.

total = 0
for expense in expenses[:3]:
    total += expense
# print("Toatl expense in first quarter : ", total)

# Find out if you spent exactly 2000 dollars in any month

for i, expense in enumerate(expenses):
    if expense == 2000:
        print(month[i])
    else:
        # print("Not Found")
        pass

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list


month.append("June")
expenses.append(1980)
# print(month, expenses)


# You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this


april_index = month.index("April")
april_expense = expenses[april_index]
april_expense_after_disc = april_expense-200
expenses[april_index] = april_expense_after_disc
print(expenses)


# ============================================= 2 ==================================
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append("black panther")
heros.remove("black panther")
print(heros.index("hulk"))
heros.insert(heros.index("hulk")+1,"black panther")
heros.remove("thor")
heros.remove("hulk")
heros.append("Dr Strange")
print(sorted(heros))
print(heros)


# ===============3=============
max_nbr = int(input("Please input a max number : "))
list_of_nbr = [i+1 for i in range(max_nbr)]
print(list_of_nbr)