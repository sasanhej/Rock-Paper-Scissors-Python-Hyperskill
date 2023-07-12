#  write your code here 

file = open('./data/dataset/input.txt', 'r')
cnt=0
for line in file:
    if line[:6] == 'summer' and len(line)==7:
        cnt+=1
print(cnt)
file.close()