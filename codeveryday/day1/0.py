from PIL import ImageDraw,Image,ImageFont
import random

n=str(random.randint(1,59)) #str格式
m='是我哦'
im=Image.open('avatar.jpg')
w,h,=im.size
wdrew=w*0.8
hdrew=w*0.08

font=ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',30)
draw=ImageDraw.Draw(im)
draw.text((wdrew,hdrew),m,font=font,fill=(255,33,33))
im.show()