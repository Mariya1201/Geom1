import os # Для проверки на пустоту файла
import math



def autotest(): # Автотесты
    # 1-ый
    points_1 = readFile("autotest1.txt")
    count1 = pointsCount(points_1, (0.0, 0.0), (10.0, 10.0))

    # 2-ой
    points_2 = readFile("autotest2.txt")
    count2 = pointsCount(points_2, (-5.0, 10.0), (22.4, -5.8))

  
    return (count1 == 2 and count2 == 3)



def readFile(filename): # Функция чтения данных из файла
    try: 
        file = open(filename)
    except OSError: 
        print("Error! Cannot open file!\n")
        input()
        exit()

    if (os.stat(filename).st_size == 0): # Проверка файла на пустоту
        print("Error! The file cannot be empty!\n")
        input()
        exit()

    coords = [] # Сюда запишутся все точки с координатами
    lines = file.readlines() 
    file.close()

    for i in range(len(lines)): 
        try: # разделит строку на координаты точек через символ ', '
            x, y = map(float, lines[i].split(', '))
        except:
            print("Error! File read error! Wrong data!\n")
            input()
            exit()

        coords.append((x, y))

    return coords



# Проверим лежит ли точка point внутри прямоугольника
def check(point, corner1 = (0, 0), corner2 = (1, 1)):
    x, y = point[0], point[1]

    x1, y1 = corner1[0], corner1[1]
    x2, y2 = corner2[0], corner2[1]

    if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
        # corner1 - левый нижний угол
        # corner2 - правый верхний угол
        return True
    elif (x >= x2 and x <= x1 and y >= y2 and y <= y1):
        # corner1 - правый верхний угол
        # corner2 - левый нижний угол
        return True
    elif (x >= x1 and x <= x2 and y <= y1 and y >= y2):
        # corner1 - левый верхний угол
        # corner2 - правый нижний угол
        return True
    elif (x >= x2 and x <= x1 and y <= y2 and y >= y1):
        # corner1 - правый нижний угол
        # corner2 - левый верхний угол
        return True

    return False



# Функция подсчитывает кол-во точек
def pointsCount(points, corner1, corner2):
    count = 0 
    for point in points:
        if check(point, corner1, corner2):
            count += 1
    return count



if autotest(): # Если автотесты успешно прошли
    print("Autotest are succesfully completed!\n")

    filename = input("Input file name: ")
    points = readFile(filename) # Массив точек, прочитанный из файла

    print("\nEnter opposite corners of the rectangle:")
    corner1X = input("Corner 1 x = ")
    corner1Y = input("Corner 1 y = ")
    corner2X = input("Corner 2 x = ")
    corner2Y = input("Corner 2 y = ")


    count = pointsCount(points, (float(corner1X), float(corner1Y)), (float(corner2X), float(corner2Y)))

    print("\nThere are " +str(count)+ " point(s) inside the given rectangle\n")

else: # Если автотесты не прошли
    print("Autotest failed!\n")
input()
