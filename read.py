data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %用来求余数
            print(len(data))
print('档案读取完，总共有', len(data), '笔留言')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    
print('留言的平均长度是', sum_len/len(data))