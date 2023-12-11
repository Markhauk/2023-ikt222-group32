total_time = 0

a = 'Hallakellær'
b = 'tullingær'

if len(a) != len(b):
    print(total_time)
    exit()

for i in range(len(a)):
    if a[i] != b[i]:
        print(total_time)
        exit()
    total_time += 1

print(total_time)


