import matplotlib.pyplot as plt


def error_values_plot(error_value):
    # error data
    error.append(round(error_value, 5))
    epoch.append(len(error))

    # clear axis
    ax.cla()

    # plot error
    ax.plot(error)
    ax.scatter(len(error)-1, error[-1])
    ax.set_ylim(0, 1)

    plt.xticks(range(len(epoch)), epoch)
    plt.title("Erro X Época")
    plt.ylabel("Erro")
    plt.xlabel("Época")

    print("ERROR: {}".format(error))


error = []
epoch = []

fig = plt.figure()
ax = plt.subplot(111)

error_values_plot(0.987654)
error_values_plot(0.753421)
error_values_plot(0.842103)
error_values_plot(0.054271)
plt.show()


