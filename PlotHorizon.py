from open_file import fileread
from matplotlib import pyplot as plt


def plot_horizon(fname):

    data = fileread(fname)

    IH_r = [i['IH.r'] for i in data]
    OH_r = [i['OH.r'] for i in data]
    A    = [i['A']    for i in data]

    plt.plot(A,IH_r,label="Inner Horizon Radius")
    plt.plot(A,OH_r,label="Outer Horizon Radius")

    plt.legend(loc='1')

    plt.show()

def ani_plot_horizon(fname):


    data = fileread(fname)

    IH_r = [i['IH.r'] for i in data]
    OH_r = [i['OH.r'] for i in data]
    A    = [i['A']    for i in data]

    xlim = max(IH_r + OH_r)

    fnum = 0
    for o,i,a in zip(IH_r,OH_r,A):

        plt.xlim(-xlim,xlim)
        plt.ylim(-xlim,xlim)

        c1 = plt.Circle((0,0), o,color='r')
        c2 = plt.Circle((0,0), i,color='b')
        fig = plt.gcf()
        fig.gca().add_artist(c2)
        fig.gca().add_artist(c1)
        plt.savefig('img%s' % fnum)
        plt.title("A" + str(a))
        fnum += 1
        print fnum,'/',len(IH_r)



plot_horizon('attempt1mass3.log')
#ani_plot_horizon('attempt1mass3.log')