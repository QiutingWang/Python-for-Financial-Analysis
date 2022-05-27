####Seaborn####

import seaborn as sns #samuel norman seaborn
import matplotlib.pyplot as plt
height = [62, 64, 69, 75, 66,
          68, 65, 71, 76, 73]
weight = [120, 136, 148, 175, 137,
          165, 154, 172, 200, 187]
sns.scatterplot(x=height, y=weight) #call the scatterplot function from the seaborn library,the input of x and y axis
plt.show()

#create a count plot#
import seaborn as sns
import matplotlib.pyplot as plt
gender = ["Female", "Female",
          "Female", "Female",
          "Male", "Male", "Male",
          "Male", "Male", "Male"]
sns.countplot(x=gender)
plt.show()

##using pandas with seaborn##
#working with dataframe and countplot()#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("masculinity.csv")  #create the dataframe
sns.countplot(x="how_masculine",data=df)  #we use the how_masculine column,set the data parameter=dataframe
plt.show()  #get the tidy or untidy dataframe

#Adding a third variable with hue色彩度#
#load the dataset,and a scatterplot with hue
import pandas as pd
import seaborn as sns
tips = sns.load_dataset("tips")
tips.head()
import matplotlib.pyplot as plt
sns.scatterplot(x="total_bill",
                y="tip",   #add a legend to a plot automatically
                data=tips,
                hue="smoker",#用于区分色彩的变量
                hue_order=["Yes",
                           "No"]) #hue_order parameter:改变ticker上面的顺序takes a list of values and will set the order of the values in the plot accordingly
plt.show()
#set the hue color
import matplotlib.pyplot as plt
import seaborn as sns
hue_colors = {"Yes": "black",
              "No": "red"}   #create the color reference dictionaries
sns.scatterplot(x="total_bill",
                y="tip",
                data=tips,
                hue="smoker",
                palette=hue_colors) #refer to the dictionary by palette parameter
plt.show()
#using hue with count plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x="smoker",
              data=tips,
              hue="sex")
plt.show()

###Introduction to relational plots and subplots###
##replot()-->figure create subplots in a single figure,create 'relational plot' using scatter plot and line plots
#use scatterplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x="total_bill",
                y="tip,
                data=tips)
plt.show()
#use replot()
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind='scatter' #specify what kind of plot we want to use--scatter plot or line plots
            col="smoker") #separate the graphs by smoker and non-smokers,horizontally in column; On the other hand,if we want to separate them in row,the code:row='smoker';Finally,we can use row() and col() at the same time,the code:row='smoker',col='time
plt.show()

#subgroups for days of the week
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            col="day",
            col_wrap=2, #we specify # of plots position per col;row_wrap:#of plot per row
            col_order=["Thur",  #ordering the column
                       "Fri",
                       "Sat",
                       "Sun"])
plt.show()


###Customerizing scatter plot###
#subplots and point size#
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            size="size",
            hue='size') #通过点的大小和颜色深浅来判断大小
plt.show()
#subgroups with point style and transparency
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            hue="smoker",
            style="smoker",
            alpha=0.4)
plt.show()

##introduction to line plots##
import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(x="hour", y="NO_2_mean",
            data=air_df_mean,
            kind="line",
            style="location", #subgroup by location
            hue="location",
            markers=True, #add the marker
            dashes=False)  #turning off line style,从虚线换到实线
plt.show()

#multiple observations per x-value
import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(x="hour", y="NO_2",
            data=air_df,
            kind="line")
plt.show() #the return plots will have a shadow area up and down around the line,95% CI,indicates the uncertainty of our estimate
#replacing CI with std
import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(x="hour", y="NO_2",
            data=air_df,
            kind="line",
            ci="sd") # ci=None,we turn off the confidence interval
plt.show()

###Visualizing a categorical and quantitative Variable###
##Count plot and bar plots
#catplot() create different types of relational plots
#countplot:
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x="how_masculine",
              data=masculinity_data)
plt.show()
#catplot:
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="how_masculine",
            data=masculinity_data,
            kind="count")
plt.show()

#changing the order
import matplotlib.pyplot as plt
import seaborn as sns
category_order = ["No answer",
                  "Not at all",
                  "Not very",
                  "Somewhat",
                  "Very"] #we set the order eariler
sns.catplot(x="how_masculine",
            data=masculinity_data,
            kind="count",
            order=category_order)
plt.show()

#bar plot:displays mean of quantitative variable per category
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="day",
            y="total_bill",
            data=tips,
            kind="bar") 
plt.show() #it shows confidence intervals for the mean,show the uncertainty about our estimate;
           #if we want to turn of the Confidence interval:we state ci=None

#changing the orientation
import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot(x="total_bill", #compare to the original one, the conent of x and y is reversed
            y="day",
            data=tips,
            kind="bar")
plt.show()

##using the distribution plot##
#create a histogram
sns.distplot(df['alcohol'], kde=False, bins=10)
#rug plot
sns.distplot(df['alcohol'], hist=False, rug=True)
#further customization 
sns.distplot(df['alcohol'], hist=False,
             rug=True, kde_kws={'shade':True}) #kde_kws:the shadow under the curve; kde:the curve of distribution

##Regression plots##
sns.regplot(x="alcohol", y="pH", data=df)
#regplot-high level
sns.regplot(x="alcohol",
            y="quality",
            data=df)
#lmplot-low level,much more powerful
sns.lmplot(x="alcohol",
           y="quality",
           data=df)
#organize data by colors,hue
sns.lmplot(x="quality",
           y="alcohol",
           data=df,
           hue="type")
#organize data by columns,col
sns.lmplot(x="quality",
           y="alcohol",
           data=df,
           col="type") #or row='type'

###Customerizing Seaborn Plots###
##using seaborn styles##
sns.set()
df['Tuition'].plot.hist()
#theme examples with .set_style
for style in ['white','dark','whitegrid','darkgrid',
              'ticks']:
    sns.set_style(style)
    sns.distplot(df['Tuition'])
    plt.show()
#removing axes with despine
sns.set_style('white') #也可以是top,right
sns.distplot(df['Tuition'])
sns.despine(left=True)

##colors in Seaborn##
#defining a color for a plot
sns.set(color_codes=True)
sns.distplot(df['Tuition'], color='g') #'g' code for green
#palettes调色板,6 default palettes
for p in sns.palettes.SEABORN_PALETTES:
    sns.set_palette(p)
    sns.distplot(df['Tuition'])
#displaying palettes
for p in sns.palettes.SEABORN_PALETTES:
    sns.set_palette(p)
    sns.palplot(sns.color_palette()) #display color swatches, 3 main types of color palettes
    plt.show()
#define customer palettes, 3 main types of color palettes
#circular:when data is not ordered for categorical data
sns.palplot(sns.color_palette("Paired", 12))
#sequential:when data has a consistent range from high to low values
sns.palplot(sns.color_palette("Blues", 12))
#Diverging:min and max values are interested
sns.palplot(sns.color_palette("BrBG", 12))

##Customerizing with Matplotlib##
#plt axes,axes can be pass into seaborn functions
fig, ax = plt.subplots() # create subplot
sns.distplot(df['Tuition'], ax=ax)
ax.set(xlabel="Tuition 2013-14") # add the xlabel notes
#further customerization
fig, ax = plt.subplots()
sns.distplot(df['Tuition'], ax=ax)
ax.set(xlabel="Tuition 2013-14",
       ylabel="Distribution", xlim=(0, 50000),
       title="2013-14 Tuition and Fees Distribution")
#combining plots
fig, (ax0, ax1) = plt.subplots(nrows=1,ncols=2, sharey=True, figsize=(7,4)) #sharey-->we share the y axis
sns.distplot(df['Tuition'], ax=ax0)
sns.distplot(df.query('State == "MN"')['Tuition'], ax=ax1) #query function to only plot data for the state Minnesota
ax1.set(xlabel="Tuition (MN)", xlim=(0, 70000)) #x轴的取值范围
ax1.axvline(x=20000, label='My Budget', linestyle='--') #.axvline to denote the maxmium amount we can budget for tuition，画出极值界限的分割线，有的时候会用mean and median
ax1.legend() #show the graph

###Additional Plot Type###
##categorical plot type##
#stripplot/swarmplot: show each observation
#boxplot/boxenplot/violinplot: abstract representations
#barplot/pointplot/countplot: statistical estimation

##Stripplot:
sns.stripplot(data=df, y="DRG Definition",
              x="Average Covered Charges",
              jitter=True) #jitter: how average charges vary by diagnosgtic reimbursement code
#Swarmplot: place the observations in a manner where they do not overlap; But it doesn't scale well to large dataset
sns.swarmplot(data=df, y="DRG Definition",
              x="Average Covered Charges")
#boxplot:
sns.boxplot(data=df, y="DRG Definition",
            x="Average Covered Charges")
#violinplot:(kernel density plot) distribution and outliers
sns.violinplot(data=df, y="DRG Definition",
               x="Average Covered Charges")
#Boxenplot:Create a boxenplot with the Paired palette and the Region column as the hue
sns.boxenplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue='Region')
plt.show()
plt.clf()
sns.barplot(data=df, y="DRG Definition",
            x="Average Covered Charges",
            hue="Region")
sns.pointplot(data=df, y="DRG Definition",
              x="Average Covered Charges",
              hue="Region")
#countplot:
sns.countplot(data=df, y="DRG_Code", hue="Region")
plt.show()
plt.clf()

###Regression Plot###
#regplot
sns.regplot(data=df, x='temp',
            y='total_rentals', marker='+')
#evaluating regression with residplot:evaluate the fit of a model
sns.residplot(data=df, x='temp', y='total_rentals')
#polynomial regression:order=2
sns.regplot(data=df, x='temp',
            y='total_rentals', order=2)
sns.residplot(data=df, x='temp',
              y='total_rentals', order=2)
#categorical value
sns.regplot(data=df, x='mnth', y='total_rentals',
            x_jitter=.1, order=2) #x_jitter:see the individual distribution of each month
#Estimator:hignlighting trends
sns.regplot(data=df, x='mnth', y='total_rentals',
            x_estimator=np.mean, order=2)
#binning the data with continuous varibales
sns.regplot(data=df,x='temp',y='total_rentals',
            x_bins=4) #divide the independent varibale into four bins


###Matrix Plot###
#get data in the right format:
pd.crosstab(df["mnth"], df["weekday"],
            values=df["total_rentals"],aggfunc="mean").round(0)
#build a heatmap
sns.heatmap(pd.crosstab(df["mnth"], df["weekday"],
            values=df["total_rentals"], aggfunc="mean"))
#customize heatmap
sns.heatmap(df_crosstab, annot=True, fmt="d", #fmt:results are displaied as integars
            cmap="YlGnBu", cbar=False, linewidths=.5) #cmap:the color setting;cbar=False-->the color bar is not display
#centering the heatmap
sns.heatmap(df_crosstab, annot=True, fmt="d",
            cmap="YlGnBu", cbar=True,
            center=df_crosstab.loc[9, 6]) #centering the heatmap color on a specific value
#plotting the correlation matrix:
cols = ['total_rentals', 'temp', 'casual', 'hum', 'windspeed']
sns.heatmap(df[cols].corr(), cmap='YlGnBu')


###Create Plots and Data Aware Grids###
##use FacetGrid, catplot, and Implot##
#comparing multiple plots side by side using the same scales and axes as a trellis or lattice plot--faceting
#FaceGrid categorical example:facets and mapping the plots
g = sns.FacetGrid(df, col='HIGHDEG') #column name is 'HIGDEG'
g.map(sns.boxplot, 'Tuition',
      order=['1', '2', '3', '4'])
#Catplot():combine the facetting and mapping process into 1 function
sns.catplot(x="Tuition", data=df,
            col="HIGHDEG", kind="box")
#FaceGrid for Regression
g = sns.FacetGrid(df, col='HIGHDEG')
g.map(plt.scatter, 'Tuition', 'SAT_AVG_ALL') #(plotstyle,'x','y')
#implot:scatter and regression
sns.lmplot(data=df, x="Tuition", y="SAT_AVG_ALL",
           col="HIGHDEG", fit_reg=False)
sns.lmplot(data=df, x="Tuition", y="SAT_AVG_ALL",
           col="HIGHDEG", row="REGION") #with regression line and region

##Using PairGrid and pairplot##
##PairGrid show the Pairwise relationship:
g = sns.PairGrid(df, vars=["Fair_Mrkt_Rent","Median_Income"]) 
g = g.map(sns.scatterplot)
#customize
g = sns.PairGrid(df, vars=["Fair_Mrkt_Rent", "Median_Income"])
g = g.map_diag(sns.histplot) #diagnal graphs
g = g.map_offdiag(sns.scatterplot)

##pairplot
sns.pairplot(df, vars=["Fair_Mrkt_Rent","Median_Income"], kind="reg",
             diag_kind="hist")
#customize
sns.pairplot(df.query("BEDRMS < 3"),
             vars=["Fair_Mrkt_Rent",   #as for vars:we need to specify x_vars and y_vars sometime
             "Median_Income", "UTILITY"],
             hue="BEDRMS", palette="husl",
             plot_kws={"alpha": 0.5})

##Using JointGrid and jointplot##
##JointGrid
#basic:
g = sns.JointGrid(data=df, x="Tuition", y="ADM_RATE_ALL")
g.plot(sns.regplot, sns.histplot)
#advanced
g = sns.JointGrid(data=df, x="Tuition", y="ADM_RATE_ALL")
g = g.plot_joint(sns.kdeplot)
g = g.plot_marginals(sns.kdeplot, shade=True)

##Jointplot
sns.jointplot(data=df, x="Tuition", y="ADM_RATE_ALL", kind=
#customize:
sns.set_style("whitegrid")
g = (sns.jointplot(x="Tuition",
                   y="ADM_RATE_ALL",
                   kind="scatter",
                   xlim=(0, 25000),
                   data=df.query('UG < 2500 &
                   Ownership == "Public"')).plot_joint(sns.kdeplot))



