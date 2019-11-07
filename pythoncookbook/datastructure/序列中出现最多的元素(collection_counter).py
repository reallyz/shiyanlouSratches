
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import  Counter
words_count=Counter(words)
print(words_count.most_common(3),type(words_count))
print(words_count)
# 注意 Counter的底层实现是字典映射，将元素出现的次数映射到元素上
# 所以元素必须是可hash的，比如字符串，int,元组

# 追加计数
more_words = ['why','are','you','not','looking','in','my','eyes']
for i in more_words:
    words_count[i]+=1
print(words_count)
# 或者
words_count.update(more_words)
print(words_count)

# Counter可以做数学运算
temp=Counter(more_words)
c=words_count-temp
print(c)