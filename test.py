i, j = 2, 4
bucket = [1, 2, 3, 4, 5, 6]
bucket = bucket[:i-1]+bucket[i-1:j][::-1]+bucket[j:]
print(bucket)
