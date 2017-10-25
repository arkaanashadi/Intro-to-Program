import matplotlib.pyplot as plt
import random


# The math function
def func(x):
    return x**2-3*x+4


def main():

    # x, y ranges and amount of random points
    x_range = 25
    y_range = 600
    random_points = 4000

    # Builds lists for the curve
    x_coord = [x for x in range(0, x_range + 1)]
    y_coord = [func(y) for y in x_coord]

    # Builds list for the random points
    rand_x = [random.randint(0, x_range) for i in range(0, random_points)]
    rand_y = [random.randint(0, y_range) for j in range(0, random_points)]

    # Builds list for the points under the curve
    plot_x = []
    plot_y = []

    for index in range(0, len(rand_x)):
        for enu in enumerate(x_coord):
            if rand_x[index] == enu[1]:
                if rand_y[index] < y_coord[enu[0]]:
                    plot_x.append(rand_x[index])
                    plot_y.append(rand_y[index])

    # Estimate of the area under the curve
    area_under_curve = ((25*600)*(len(plot_x)))/random_points
    print(area_under_curve)

    # Plots all three lists and displays the graph
    plt.scatter(rand_x, rand_y, c="yellow")
    plt.scatter(plot_x, plot_y, c="red")
    plt.plot(x_coord, y_coord, marker="p", c="blue")
    plt.xlabel("x coordinates")
    plt.ylabel("y coordinates")
    plt.title("Area Under Curve = {0}".format(str(area_under_curve)))
    plt.show()


main()
