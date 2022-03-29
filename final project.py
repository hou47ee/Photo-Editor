import matplotlib.pyplot as plt

mypath = input("Input the address of photo: ")
file = plt.imread(mypath) #讀取圖片
#顯示圖片
plt.figure(figsize=(12,12))
plt.imshow(file)
plt.show()

newphoto = file.copy() 

def tograyscale(photo):
    global newphoto
    for i in range(0,len(photo)):
        for j in range(0,len(photo[0])):
            m = (photo[i][j][2]*0.299 + 0.5) + (photo[i][j][1]*0.587+0.5) + (photo[i][j][0]*0.114+0.5)
            if m > 255:
                newphoto[i][j][2] = 255
                newphoto[i][j][1] = 255
                newphoto[i][j][0] = 255
            else:
                newphoto[i][j][2] = m
                newphoto[i][j][1] = m
                newphoto[i][j][0] = m

def lighter(photo):
    global newphoto
    for i in range(0,len(photo)):
        for j in range(0,len(photo[0])):
            for k in range(0,len(photo[0][0])):
                value = photo[i][j][k] + 10
                if value <= 255:
                    newphoto[i][j][k] = value
                else:
                    newphoto[i][j][k] = 255
def darker(photo):
    global newphoto
    for i in range(0,len(photo)):
        for j in range(0,len(photo[0])):
            for k in range(0,len(photo[0][0])):
                value = photo[i][j][k] - 10
                if value >= 0:
                    newphoto[i][j][k] = value
                else:
                    newphoto[i][j][k] = 0
def blur(photo):
    global newphoto
    for i in range(1,len(photo)-1):
        for j in range(1,len(photo[0])-1):
            for k in range(0,len(photo[0][0])):
                m = (int(photo[i - 1][j + 1][k]) + 
                                     int(photo[i + 0][j + 1][k]) + 
                                     int(photo[i + 1][j + 1][k]) + 
                                     int(photo[i - 1][j + 0][k]) + 
                                     int(photo[i + 0][j + 0][k]) + 
                                     int(photo[i + 1][j + 0][k]) + 
                                     int(photo[i - 1][j - 1][k]) + 
                                     int(photo[i + 0][j - 1][k]) + 
                                     int(photo[i + 1][j - 1][k]))/9 + 0.5
                if m > 255:
                    newphoto[i][j][k] = 255
                else:
                    newphoto[i][j][k] = m
            
def picture():
    global newphoto
    for i in range(0,len(newphoto)):
        for j in range(0,len(newphoto[0])):
            for k in range(0,len(newphoto[0][0])):
                if 0 <= newphoto[i][j][k] < 24:
                    newphoto[i][j][k] = 12
                elif 20 <=  newphoto[i][j][k] < 48:
                    newphoto[i][j][k] = 36
                elif 48 <=  newphoto[i][j][k] < 72:
                    newphoto[i][j][k] = 60
                elif 72 <=  newphoto[i][j][k] < 96:
                    newphoto[i][j][k] = 84
                elif 96 <=  newphoto[i][j][k] < 120:
                    newphoto[i][j][k] = 108
                elif 120 <=  newphoto[i][j][k] < 144:
                    newphoto[i][j][k] = 132
                elif 144 <=  newphoto[i][j][k] < 168:
                    newphoto[i][j][k] = 156
                elif 168 <=  newphoto[i][j][k] < 192:
                    newphoto[i][j][k] = 180
                elif 192 <=  newphoto[i][j][k] < 216:
                    newphoto[i][j][k] = 204
                elif 216 <=  newphoto[i][j][k] < 240:
                    newphoto[i][j][k] = 228
                elif 240 <=  newphoto[i][j][k] < 256:
                    newphoto[i][j][k] = 248
                    
def reset():
    global newphoto
    newphoto = file.copy()

while 1:
    print("Choose the number of the feature You want to apply:\n")
    print("1 ToGrayScale\n")
    print("2 Lighter\n")
    print("3 Darker\n")
    print("4 Blur\n")
    print("5 ToPicture\n")
    print("6 Reset\n")
    print("7 Save Photo\n")
    print("8 Quit\n")
    print("---------------------------------------\n")
    choice = int(input())
    if choice == 1:
        tograyscale(newphoto)
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 2:
        lighter(newphoto)
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 3:
        darker(newphoto)
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 4:
        blur(newphoto)
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 5:
        picture()
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 6:
        reset()
        plt.figure(figsize=(12,12))
        plt.imshow(newphoto)
        plt.show()
    elif choice == 7:
        name = str(input("Please input the save name with address you want to place: "))
        plt.imsave(name,newphoto) 
    elif choice == 8:
        break
    else:
        print("Invalid input\n")

