remainder_list = []

for i in range(10):
    remainder = int(input()) % 42
    remainder_list.append(remainder) \
        if remainder not in remainder_list else 0

print(len(remainder_list))
