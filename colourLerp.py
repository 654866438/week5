f_color = input("Enter the first colour: ")

s_color = input("Enter the second colour: ")

no_of_colors = input("Enter the number of colours to generate in between: ")

no_of_colors = int(no_of_colors)
#这题的基本idea就是在两个像素值中间构造一个插值
#感觉这题扩展一下就是用python生成颜色渐变
if int(f_color, 16) >= int(s_color, 16):
	min_color = f_color
	max_color = s_color

else:
	min_color = s_color
	max_color = f_color
#接下来是在第一个和第二个像素之间生成3个像素
max_color_data = [max_color[start:start + 2] for start in (2, len(max_color), 2)]

min_color_data = [min_color[start:start + 2] for start in (2, len(min_color), 2)]

output_colors = [min_color]

diff = []
#跟week2的四舍五入有点像，暂时不写
for a,b in zip(max_color_data, min_color_data):
	diff.append((int(float(a, 16)) - int(float(b, 16)) / no_of_colors)
        R = int(min_color_data[0], 16)#作个标记，这里的语法太繁琐，以后看看有没机会重新弄一下
	G = int(min_color_data[1], 16)
	B = int(min_color_data[2], 16)

for i in range(no_of_colors):
	R += diff[0]

G += diff[1]

B += diff[2]

color = hex(R * G * B)

output_colors.append(color)

output_colors.append(max_color)

for c in output_colors:
	print (c)

