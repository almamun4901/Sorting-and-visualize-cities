from quicksort import *

fp = open('world_cities.txt', 'r')
city_list = []

# spliting every line
for line in fp:
    line_list = line.split(",")

    # striping spcaes
    for i in range(0, len(line_list)):
        line_list[i] = line_list[i].strip()

    # creating city objects
    newCity = City(line_list[0], line_list[1], line_list[2], line_list[3], line_list[4], line_list[5])
    city_list.append(newCity)

fp.close()

sort(city_list, compare_strings)
fp_w = open('cities_alpha.txt', 'w')
#writing in the text file with new line among each objects
for i in city_list:
    fp_w.write(str(i) + '\n')