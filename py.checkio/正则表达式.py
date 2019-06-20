
#正则表达式是做完全匹配的
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