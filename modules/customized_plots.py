import seaborn as sns
import matplotlib.pyplot as plt

def Hist(dataset, xlabel, filename):
    sns.set_style("darkgrid")
    sns.distplot(dataset, kde=True, rug=False)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('./fig/'+filename+'.png',dpi=100)  

def CountPlot(dataset, column, label, s, a):
    sns.set_style("darkgrid")
    sns_plot = sns.factorplot(x=column,data=dataset,kind='count', palette="muted",size = s, aspect = a)
    plt.xlabel(label)
    plt.ylabel('Frequency')
    plt.tight_layout()
    sns_plot.savefig('./fig/'+ label + '_Count_Plot.png',dpi=100)

def MapPlot(dataset, color = None, legend_plot = True):
    sns.set_style("darkgrid")
    city_long_border = (-74.03, -73.75)
    city_lat_border = (40.63, 40.85)
    if color is None:
        sns_plot = sns.lmplot('pickup_longitude', 'pickup_latitude', data=dataset,fit_reg=False, scatter_kws={"s": 2.5}, legend =legend_plot)
    else:
        sns_plot = sns.lmplot('pickup_longitude', 'pickup_latitude', data=dataset,hue = color, fit_reg=False, scatter_kws={"s": 2.5}, legend =legend_plot)
    sns.plt.xlim(city_long_border)
    sns.plt.ylim(city_lat_border)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    sns_plot.savefig('./fig/Map_Plot_PickUp.png',dpi=100)

def SpeedPlot(dataset,column,speed,label):
    sns.set_style("darkgrid")
    sns.pointplot(x=column, y=speed, data=dataset)
    plt.xlabel(label)
    plt.ylabel('Speed (km/hr)')
    plt.savefig('./fig/Speed_By_'+label+'.png',dpi=100)
 
def PlotFeatureImp(feature_importance_table):
    sns.set_style("darkgrid")
    sns.factorplot(x="importance", y="feature_name",data=feature_importance_table, kind="bar")
    plt.savefig('./fig/Feature_Imp_XGB.png',dpi=100)