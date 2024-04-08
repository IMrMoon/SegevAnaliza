from colors import bcolors


def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if p[i] <= point <= p[i + 1]:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((point - x2) * y1) / (x1 - x2) + (((point - x1) * y2) / (x2 - x1)))
            print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
            flag = 0
    if flag:
        if point < table_points[0][0]:
            x1 = table_points[0][0]
            x2 = table_points[1][0]
            y1 = table_points[0][1]
            y2 = table_points[1][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + (m * (point - x1))
            print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
        elif point > table_points[-1][0]:
            x1 = table_points[-1][0]
            x2 = table_points[-2][0]
            y1 = table_points[-1][1]
            y2 = table_points[-2][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + (m * (point - x1))
            print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ", bcolors.ENDC,
                  round(result, 4))
        else:
            print(bcolors.FAIL, "Point not found in the table range. Unable to interpolate or extrapolate.", bcolors.ENDC)



if __name__ == '__main__':

    table_points = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
    x =  1.47
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)


