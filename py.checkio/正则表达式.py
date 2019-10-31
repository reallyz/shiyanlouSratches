# 如果使用次数多，应该先把pattern compile
# 正则表达式match是完全匹配，通常是检查输入的合法性
# findall,列表返回找到的所有字符串
# split,sub等
import re
def is_valid_email(addr):
    if re.match(r'([0-9a-zA-Z\.]*)@(.*com)',addr):
        return True

l=[]
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
def name_of_email(addr):
    if re.match(r'^<',addr):
        return re.match(r'<([a-zA-Z\s]+)>.*',addr).group(1)
    else:
        return re.match(r'([a-zA-Z]+).*',addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

comusername=re.compile(r'^[0-9a-zA-Z_]{6,20}$')
comuserid=re.compile(r'^[1_9]/d{4,11}$')
