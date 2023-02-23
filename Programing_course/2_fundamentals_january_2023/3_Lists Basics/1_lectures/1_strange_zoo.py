order = []

# normal_order = [head, body, tail]
# print(normal_order)

for _ in range(3):
    data = input()
    order.append(data)

order[0], order[2] = order[2], order[0]

print(order)
