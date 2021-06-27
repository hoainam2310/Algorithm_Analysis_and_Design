#Cach lam: Chia dieu kien bai toan thanh hai phan:
# - Tim so luong keo toi thieu de dua cho child[i] co xep hang cao hon child[i-1]
# - Tim so luong keo toi thieu de dua cho child[i] co xep hang cao hon child[i+1]

def candy(ratings):
  candies = [1] * len(ratings) #dem so luong keo dua cho hoc sinh hien tai
  for i in range(1, len(ratings)):
    if ratings[i] > ratings[i - 1]: #duyet mang tu trai sang phai
      candies[i] = candies[i - 1] + 1 #neu ratings[i] > ratings [i-1] thi child[i] se co candy[i-1] + 1 vien keo

  for i in range(len(ratings) - 2, -1, -1):
    if ratings[i] > ratings[i + 1]: #duyet mang tu phai sang trai
      candies[i] = max(candies[i], candies[i + 1] + 1) #neu ratings[i] > ratings [i+1] thi child[i] se co candy[i+1] + 1 vien keo roi so sanh tim mang lon nhat
  return sum(candies) 

ratings = list(map(int, input().split()))
print(candy(ratings))