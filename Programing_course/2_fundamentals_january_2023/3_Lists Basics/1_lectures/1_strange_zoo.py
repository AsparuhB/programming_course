tail = input()
body = input()
head = input()

# normal_order = [head, body, tail]
# print(normal_order)

order = [tail, body, head]
order[0], order[2] = order[2], order[0]

print(order)
