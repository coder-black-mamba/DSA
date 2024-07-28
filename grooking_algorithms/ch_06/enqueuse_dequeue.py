from collections import deque

data = deque()

data.appendleft("Sayed")


# this can append only one item that's why it will return error
# data.appendleft("Sehab","Rohim")
# data.append("Sehab","Rohim")

# for appending/adding a whole array/list to quue use "+="
# data+=["Sehab","Rohim"]
print(data)