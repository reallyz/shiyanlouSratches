from faker import Faker

fake=Faker('zh_cn')
with open('./fakerfun.txt','w+') as f:
    for i in range(10):
        f.writelines([fake.name()+'\n',fake.ascii_email()+'\n'])



