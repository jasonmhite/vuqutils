import seaborn as sb
import pandas as pd

__all__ = ["uncertainty_plot"]

def uncertainty_plot(data, center=True, relative=False, filternull=True):
    """
    Take a Series object and make a relative uncertainty plot. This
    centers the plot and annotates with mean and standard deviation.

    Parameters
    ----------

    data:  a Pandas Series object that contains the data.
    center: If true, center on mean. If false, do no centering.
            Else, treat center as an explicit value to center on.
            Default true.
    filternull: If true (default), filter out null values in the data.
    relative: If true, normalize width to the standard deviation
              (default false)
    """

    if filternull is True:
        plotdata = data[data.notnull()]
    else:
        plotdata = data

    if relative is True:
        plotdata /= plotdata.std()

    if center is True:
        center = 0.
        plotdata -= data.mean()
    elif center is False:
        center = plotdata.mean()
    elif center is not False:
        plotdata -= center


    bbox_style = {'boxstyle': 'round', 'fc': 'white', 'lw': 2,
            'alpha': .7, 'ec': 'grey',}
    anntext = """$\mu={}$
    $\sigma={}$""".format(data.mean(), data.std())
    ax = sb.distplot(plotdata) 
    ax.text(.02, .88, anntext,
        transform=ax.transAxes,
        bbox=bbox_style,
        )
    ax.axvline(center, color='black')
    return(ax)
