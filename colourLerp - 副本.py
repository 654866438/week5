first=input('Enter the first colour: ')
sec=input('Enter the second colour: ')
total=int(input('Enter the number of colours to generate inbetween: '))

Red1=int(first[2:4],16)
Red2=int(sec[2:4],16)
if(Red1>Red2):
    tmp=first
    first=sec
    sec=tmp

Red1=int(first[2:4],16)
Green1=int(first[4:6],16)
Blue1=int(first[6:8],16)

Red2=int(sec[2:4],16)
Green2=int(sec[4:6],16)
Blue2=int(sec[6:8],16)
    
channelR = round((Red2-Red1)/(total+1))
channelG = round((Green2-Green1)/(total+1))
channelB = round((Blue2-Blue1)/(total+1))

print('Colours:')
print(first.lower())
for i in range(1,total+1):
    pixelR = (hex(Red1 + (i * channelR))[2:]).zfill(2)
    pixelG = (hex(Green1 + (i * channelG))[2:]).zfill(2)
    pixelB = (hex(Blue1 + (i * channelB))[2:]).zfill(2)
    pixel = '0x' + pixelR + pixelG + pixelB
    print(pixel.lower())
print(sec.lower())
