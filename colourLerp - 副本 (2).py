
p1 = int(input("Enter the first colour: "),16)
p2 = int(input("Enter the second colour: "),16)
colours = int(input("Enter the number of colours to generate inbetween: "))

red = (p1 & 0xFF0000) >> 16
green = (p1 & 0x00FF00) >> 8
blue = p1 & 0x0000FF
red2 = (p2 & 0xFF0000) >> 16
green2 = (p2 & 0x00FF00) >> 8
blue2 = p2 & 0x0000FF

red3 = abs((red2-red)/(colours+1))
green3 = abs((green2-green)/(colours+1))
blue3 = abs((blue2-blue)/(colours+1))
print("Colours:")
print('0x%02x%02x%02x' % (red, green, blue))
for i in range(1,colours+1):
	red += red3
	green += green3
	blue += blue3
	print('0x%02x%02x%02x' % (round(red), round(green), round(blue)))
print('0x%02x%02x%02x' % (red2, green2, blue2))

output_colors.append(color)

output_colors.append(max_color)

for c in output_colors:
	print (c)

