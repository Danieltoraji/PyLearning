from PIL import Image
ascii_char = list("#@&$%WMNRGPBZJIL{}?+[]()|\>;~:*"",.'' ")

def process(r, g, b, alpha=256):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    leng = len(ascii_char)
    percent = int(gray / 256 * leng)
    return ascii_char[percent]

im = Image.open('input.jpg')
#以下为预设的尺寸
length = int(int(im.size[0])*0.35)
width = int(int(im.size[1])*0.23)
#length = int(int(im.size[0])*1)
#width = int(int(im.size[1])*0.58)
#length = int(int(im.size[0])*2.1)
#width = int(int(im.size[1])*1.1)
im = im.resize((length,width))
txt = ""

a = 0

for y in range(width):
    for x in range(length):
        txt += process(*im.getpixel((x, y)))
    txt += '\n'
    a = a + 1
    print(a,width)
    
print(txt)

with open("output.txt",'w') as f:
    f.write(txt)
