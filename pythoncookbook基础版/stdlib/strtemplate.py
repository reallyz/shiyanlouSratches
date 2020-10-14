import time,os
photofiles=['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
from string import Template
class BatchRename(Template):
    delimiter = '%'

fmt=input('Enter rename style (%d-date %n-seqnum %f-format): ')

t=BatchRename(fmt)
date=time.strftime('%d%b%y')
for i,item in enumerate(photofiles):
    base,ext=os.path.splitext(item)
    newname=t.substitute(d=date,n=i,f=ext)
    print(f'{item}--->{newname}')

