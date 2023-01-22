num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
               if num % l == 0 and num % k == 0 and num % j == 0 and num % i == 0:
                   print(f"{i}{j}{k}{l}", end=" ")
