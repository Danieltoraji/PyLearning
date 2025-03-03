from PIL import Image
小黑子漏出鸡脚了吧_香翅捞饭食不食 = list("#@&$%WMNRGPBZJIL{}?+[]()|\>;~:*"",.'' ")
def afeubakidlfnsakdufhlef(r, g, b, alpha=256):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    leng = len(小黑子漏出鸡脚了吧_香翅捞饭食不食)
    jdsalfkjsdlkjfkaljsdkfjlakjfkasjdklfjklasdjfkldsajfklj = int(gray / 256 * leng)
    return 小黑子漏出鸡脚了吧_香翅捞饭食不食[jdsalfkjsdlkjfkaljsdkfjlakjfkasjdklfjklasdjfkldsajfklj]
lsakudfhaliuef = Image.open('input.jpg')
sdajfhfliuah = int(int(lsakudfhaliuef.size[0])*2.1)
小黑子树脂666 = 0
aliuefheflsdufha = int(int(lsakudfhaliuef.size[1])*1.1)
lsakudfhaliuef = lsakudfhaliuef.resize((sdajfhfliuah,aliuefheflsdufha))
jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf = ""
for y in range(aliuefheflsdufha):
    for lahuekfhadf in range(sdajfhfliuah):
        jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf += afeubakidlfnsakdufhlef(*lsakudfhaliuef.getpixel((lahuekfhadf, y)))
    jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf += '\n'
    小黑子树脂666 = 小黑子树脂666 + 1
    print(小黑子树脂666,aliuefheflsdufha)   
print(jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf)
with open("output.jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf",'w') as 你干嘛哎呦:
    你干嘛哎呦.write(jhfdlauehfliuhefiusdgflaiusgfaiewufhblaieufhaf)
