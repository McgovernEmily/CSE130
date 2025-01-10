data = [2, 5, 6, 8, 9]

for i in range(10):
    print(i)
    assert 0 <= i < len(data)
    print(data[i])