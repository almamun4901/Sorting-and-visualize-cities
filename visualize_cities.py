# Name : Md Al Mamun
# Date: 11/09/2022
#Purpose: Lab 3

# Visualize world map with top 50 populated cities

from cs1lib import *
from city import City

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 320


def myDraw():
    set_clear_color(1,1,1)
    clear()

    #setting the world image as the background
    img = load_image("world.png")
    draw_image(img, 0, 0)

    #comapre functions
    def compare_population_ints(a, b):
        return int(a.population) >= int(b.population)

    def compare_latitude(a, b):
        return a.latitude <= b.latitude

    def compare_strings(a, b):
        return a.city_name.lower() <= b.city_name.lower()

    #Partition function for the quicksort
    def partition(the_list, p, r, compare_func):

        pivot = the_list[r]

        i = p - 1

        for j in range(p, r):
            if compare_func(the_list[j], pivot):
                i = i + 1

                (the_list[i], the_list[j]) = (the_list[j], the_list[i])

        (the_list[i + 1], the_list[r]) = (the_list[r], the_list[i + 1])
        return i + 1

    #quicksort function
    def quicksort(the_list, compare_func, p=None, r=None):
        if p == None and r == None:
            p = 0
            r = len(the_list) - 1

        if p < r:
            pivot = partition(the_list, p, r, compare_func)

            quicksort(the_list, compare_func, p, pivot - 1)
            quicksort(the_list, compare_func, pivot + 1, r)

    #sort function to call quicksort
    def sort(the_list, compare_func):
        quicksort(the_list, compare_func)

    #reading the file
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

    #comapre population and visualize
    sort(city_list, compare_population_ints)

    i = 0
    while i < len(city_list):
        if i < 50:
            set_fill_color(1, 0, 0)
            draw_rectangle(int(360 + (2 * city_list[i].longitude)), int(180 - 2 * city_list[i].latitude), 5, 5)
        i = i + 1

    #sorting cities name and writing
    sort(city_list, compare_strings)

    fp_w = open('cities_alpha.txt', 'w')
    # writing in the text file with new line among each objects
    for i in city_list:
        fp_w.write(str(i) + '\n')

    #sorting cities population and writing
    sort(city_list, compare_population_ints)
    fp_w = open('cities_population.txt', 'w')
    # writing in the text file with new line among each objects
    for i in city_list:
        fp_w.write(str(i) + '\n')

    #sorting latitude and writing
    sort(city_list, compare_latitude)
    fp_w = open('cities_latitude.txt', 'w')
    # writing in the text file with new line among each objects
    for i in city_list:
        fp_w.write(str(i) + '\n')



start_graphics(myDraw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)



