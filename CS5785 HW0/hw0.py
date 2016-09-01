from matplotlib import pylab as plt
import matplotlib.lines as mlines
import numpy
def main():
# parse in the first four columns into data_set matrix
    data_set = numpy.genfromtxt('iris.data.txt', delimiter=',', usecols=[0,1,2,3])
# parse in the 5th column as species vector
    data_labels = numpy.genfromtxt('iris.data.txt', dtype=numpy.str, delimiter=',', usecols=[4])
# parameters[0] = sepal length, [1] = sepal width, [2] = petal length, [3]=petal width
    parameters=[]
    para_descr=["sepal_length","sepal_width","petal_length","petal_width"]
    for i in range(0,4):
        parameters.append([])
        parameters[i] = data_set[:,i]
# create a list that assigns colors for each species
    colors = []
    for w in data_labels:
        if 'setosa' in w:
            colors.append('r')
        elif 'versicolor' in w:
            colors.append('g')
        elif 'virginica' in w:
            colors.append('b')

# plot the 6th graph and save it
    for i in range(0,4):
        for j in range(i+1, 4):
            plt.scatter(parameters[i],parameters[j],c=colors)
            plt.xlabel(para_descr[i] + '/cm')
            plt.ylabel(para_descr[j] + '/cm')
            plt.title(" Plot of " + para_descr[i]+" VS " +para_descr[j])
            plt.savefig(para_descr[i]+" vs "+para_descr[j]+".png")

if __name__ == '__main__':
    main()
