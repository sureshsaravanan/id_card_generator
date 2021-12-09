import img as img
import til as til
from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode

image = Image.new('RGB',(1000,900),(255,255,255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf',size=45)
os.system("ID CARD Generator")
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%y\ ID CARD Generator \t  %I:%M:%S %p")
print(reg_format_date)

(x,y) = (50,50)
message = input("\n Enter your company name :")
company = message
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf',size=80)
draw.text((x,y),message,fill=color,font=font)

(x,y) = (600,75)
idno = random.randint(10000000,90000000)
message =str('ID'+str(idno))
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)

(x,y) = (50,250)
message = input("\n Enter your Full name :")
name = message
color = 'rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf',size=45)
draw.text((x,y),message,fill=color,font=font)

(x,y) = (50,350)
message = input("\n Enter your gender :")
color = 'rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y) =(250,350)
message = input("\n Enter your age :")
color = 'rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y) =(50,550)
message = input("\n Enter your Blood group :")
color = 'rgb(255,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y) =(50,650)
message = input("\n Enter your Mobile number :")
temp = message
color = 'rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

(x,y) =(50,750)
message = input("\n Enter your address:")
color = 'rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)

image.save(str(name)+'.png')

image = qrcode.make(str(company)+str(idno))
img.save(str(idno)+'.bmp')

til = Image.open(name+'.png')
img=Image.open(str(idno)+'.bmp')
til.paste(img,(600,350))
til = image.open(name+'.png')

print (('\n\n\n YOUR ID CARD SUCCESSFULY CREATED IN A PNG FILE'+name+'.png'))
eval(input('\n\nPress any key to close program.....!'))



