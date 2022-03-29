####Matplotlib####

###Introduction to data visualzation with matplotlib###
#pyplot plat#
from os import lseek
import matplotlib.pyplot as plt
fig, ax = plt.subplots() #figure object and axes object.Figure object is a container,hold everything you see in the page
plt.show() #we can see the empty plot
#add data to our axes
seattle_weather["MONTH"]
seattle_weather["MLY-TAVG-NORMAL"]
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"]) #plotting command is the method of the Axes object(X,y)
plt.show()
#Add more data to the plot
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show() #it will show two indenpendent lines
#put them together
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

##Customizing your plots##
#customizing data appearence#
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"])
plt.show()
#Adding markers
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"],
        marker="o") #o-->use circles as markers;v-->use trangle as markers
plt.show()
#setting the line style
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"],
        marker="v",linestyle="--",color='r') #the apparence of connecting lines,r is red
ax.set_xlabel("Time (months)")  #set the label name of x and y
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
ax.set_title("Weather in Seattle") # add a title
plt.show()

##Small multiples##
#adding data
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"],
        color='b')
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
plt.show()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"],
        linestyle='--', color='b')
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"],
        linestyle='--', color='b')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
        color='r')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"],
        linestyle='--', color='r')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"],
        linestyle='--', color='r')
plt.show()
#to avoid this mess,we use small multiples
fig, ax = plt.subplots(3, 2) #with 3 rows and 2 columns blank plots
plt.show()

##small multiples##
#Adding data
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"],
        color='b')
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
plt.show()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"],
        linestyle='--', color='b')
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"],
        linestyle='--', color=color)
plt.show()

ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
        color='r')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"],
        linestyle='--', color='r')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"],
        linestyle='--', color='r')
plt.show()
#use small multiples to put several plot into one graph
#Small multiples with plt.subplot
fig, ax = plt.subplots()  #we called this functions with no inputs
fig, ax = plt.subplots(3, 2)
plt.show()
#Adding data to subplots for the first subplot在左上角的图
ax[0, 0].plot(seattle_weather["MONTH"],  #index into this object
              seattle_weather["MLY-PRCP-NORMAL"],
              color='b')
plt.show()

#subplot with data
fig, ax = plt.subplots(2, 1)
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],
           color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"],
           linestyle='--', color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"],
           linestyle='--', color='b')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
           color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"],
           linestyle='--', color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"],
           linestyle='--', color='r')
ax[0].set_ylabel("Precipitation (inches)")
ax[1].set_ylabel("Precipitation (inches)")
ax[1].set_xlabel("Time (months)")
plt.show()

#sharing the y-axis range,make sure that all the subplots have the same range of y-axis,we initalize the figure and its subplots with sharey=True
fig, ax = plt.subplots(2, 1, sharey=True)


##Ploting time series data##
#Time series data plotting#using climate change time series,date,co2,relative_temp
#show the index of the dataframe
climate_change.index
#plotting time series data
import matplotlib.pyplot as plt
fig, ax = plt.subplots() #create figure and axes
ax.plot(climate_change.index, climate_change['co2']) #add the data into the plot
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()
#zooming in a decade
sixties = climate_change["1960-01-01":"1969-12-31"] #delimit the start date and the end date of the period,yearly
fig, ax = plt.subplots()
ax.plot(sixties.index, sixties['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show() #the result shows a missing value in the plot,represented as breaks
#Zooming in on one year
sixty_nine = climate_change["1969-01-01":"1969-12-31"] #the result will show the graph in that year,monthly separated
fig, ax = plt.subplots()
ax.plot(sixty_nine.index,sixty_nine['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()

##plotting time series with different variables##
#plotting two time-series together#
import pandas as pd
climate_change = pd.read_csv('climate_change.csv',
                             parse_dates=["date"],
                             index_col="date")
climate_change

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"])
ax.plot(climate_change.index, climate_change["relative_temp"])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm) / Relative temperature')
plt.show() #the results show one of the line is so flat like a horizontal line,one is have a big slope.The scales of the lines are different.

#using twin axes,plot them into the same subplot using two different y-axis scales
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change["relative_temp"])
ax2.set_ylabel('Relative temperature (Celsius)')
plt.show()

#Separating variables by color
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"], color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)', color='blue')
ax2 = ax.twinx()
ax2.plot(climate_change.index, climate_change["relative_temp"],
         color='red')
ax2.set_ylabel('Relative temperature (Celsius)', color='red')
plt.show()

#color the ticks
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"],
        color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)', color='blue')
ax.tick_params('y', colors='blue')
ax2 = ax.twinx()
ax2.plot(climate_change.index,
         climate_change["relative_temp"],
         color='red')
ax2.set_ylabel('Relative temperature (Celsius)',
color='red')
ax2.tick_params('y', colors='red')
plt.show()
#use a function to plot time-series,plot_underscore_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
  axes.plot(x, y, color=color) #Plot the inputs x,y in the provided color
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color=color)
  axes.tick_params('y', colors=color) #Set the colors tick params for y-axis
#use our function,we don't need to repeat these calls, and the code is simpler
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'],
               'blue', 'Time', 'CO2 (ppm)')
ax2 = ax.twinx()
plot_timeseries(ax, climate_change.index,
                climate_change['relative_temp'],
                'red', 'Time', 'Relative temperature (Celsius)')
plt.show()

##Annotating time-series data
# Add annotation加注释，explaining the feature,focusing our attention on some feature of the data and explain the feature
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'],
               'blue', 'Time', 'CO2 (ppm)')
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index,
                climate_change['relative_temp'],
               'red', 'Time', 'Relative temperature (Celsius)')
ax2.annotate(">1 degree",  xy=[pd.TimeStamp("2015-10-06"), 1]) # 1 degree celsius value at that date
plt.show()
#positioning the text
ax2.annotate(">1 degree",
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2)) 
# add an arrow to annotation
ax2.annotate(">1 degree",
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2),
             arrowprops={})
#customizing arrow properties
ax2.annotate(">1 degree",
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2),
             arrowprops={"arrowstyle":"->", "color":"gray"}) 


###Quantitative comparisons and statistical visualization###
##Quantitative comparisons:bar-charts##
#Read the csv file
medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"]) #use ax.bar() to create a bar chart
plt.show()
#Rotate the tick labels,show all the whole labels 
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90)  #the heights correspond to the number of models
ax.set_ylabel("Number of medals")  
plt.show()
#visualizing the other medals
fig, ax = plt.subplots
ax.bar(medals.index, medals["Gold"])
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90) #we create a stacked bar chart
ax.set_ylabel("Number of medals") #the bottom key-words argument to tell plt the bottom of this column's data should be at height of the previous column's data
plt.show()
#visualizing all the three，三个柱状图叠加stack bar chart
fig, ax = plt.subplots
ax.bar(medals.index, medals["Gold"])
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"])
ax.bar(medals.index, medals["Bronze"],
       bottom=medals["Gold"] + medals["Silver"])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
plt.show()
#Adding a legend,for use the figure easier to understand,label which color correspond to which model
fig, ax = plt.subplots
ax.bar(medals.index, medals["Gold"])
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"]) #Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Bronze"],
       bottom=medals["Gold"] + medals["Silver"]) #Stack bars for "Bronze" on top of that with label "Bronze"
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
ax.legend()
plt.show()

##Quantitive comparisons:histograms--compare the distribution of data##
#draw a bar chart#
fig, ax = plt.subplots()
ax.bar("Rowing", mens_rowing["Height"].mean()) #argument:the names of bar chart,the value.
#mens_rowing:includes information about the medalists in the men's rowing events
ax.bar("Gymnastics", mens_gymnastics["Height"].mean())
ax.set_ylabel("Height (cm)")
plt.show()
#introducing histogram,adding the label,setting the number of bins
fig, ax = plt.subplots()
ax.hist(mens_rowing["Height"],label="Rowing",bins=5)
ax.hist(mens_gymnastic["Height"],label="Gymnastics",bins=5)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
ax.legend() #add a label
plt.show()
#setting the bins boundaries#
ax.hist(mens_rowing["Height"], label="Rowing",
        bins=[150, 160, 170, 180, 190, 200, 210])
ax.hist(mens_gymnastic["Height"], label="Gymnastics",
        bins=[150, 160, 170, 180, 190, 200, 210])
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()
#transparency:'step'
ax.hist(mens_rowing["Height"], label="Rowing",
        bins=[150, 160, 170, 180, 190, 200, 210],
        histtype="step")
ax.hist(mens_gymnastic["Height"], label="Gymnastics",
        bins=[150, 160, 170, 180, 190, 200, 210],
        histtype="step") #'step' display the bar as thin lines, instead of bars
ax.set_xlabel("Height (cm)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()

##Statistical plotting##
#adding error bars to bar chart#summarize the distribution of data in one number:for example,the std of the values
fig, ax=plt.subplots()
ax.bar("Rowing",
       mens_rowing["Height"].mean(),  #y is the mean of the height column
       yerr=mens_rowing["Height"].std())
ax.bar("Gymnastics",
       mens_gymnastics["Height"].mean(),
       yerr=mens_gymnastics["Height"].std())
ax.set_ylabel("Height (cm)")
plt.show()
#adding error bars to bar chart.Take the sequence of x values
fig, ax = plt.subplots()
ax.errorbar(seattle_weather["MONTH"],
            seattle_weather["MLY-TAVG-NORMAL"],
            yerr=seattle_weather["MLY-TAVG-STDDEV"])
ax.errorbar(austin_weather["MONTH"],
            austin_weather["MLY-TAVG-NORMAL"],
            yerr=austin_weather["MLY-TAVG-STDDEV"])
ax.set_ylabel("Temperature (Fahrenheit)")
plt.show()

#adding boxplots.the sequence of sequences
fig, ax = plt.subplots()
ax.boxplot([mens_rowing["Height"],
            mens_gymnastics["Height"]]) #we create two columns
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
plt.show()

##Quantitative comparisons:Scatter plot##
#introducing scatter plot:use scatter method
fig, ax = plt.subplots()
ax.scatter(climate_change["co2"], climate_change["relative_temp"])
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()

#customizing scatter plot
eighties = climate_change["1980-01-01":"1989-12-31"] #use time series indexing
nineties = climate_change["1990-01-01":"1999-12-31"]
fig, ax = plt.subplots()
ax.scatter(eighties["co2"], eighties["relative_temp"],
           color="red", label="eighties")
ax.scatter(nineties["co2"], nineties["relative_temp"],
           color="blue", label="nineties")
ax.legend()
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()
#encoding third variable by color
fig, ax = plt.subplots()
ax.scatter(climate_change["co2"], climate_change["relative_temp"],
           c=climate_change.index)
ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")
plt.show()


###Preparing your figures to share with others###
##Changing plot style##the line color and the marker shape
#The previous one
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()
#choosing style
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()
#back to the default
plt.style.use("default") #the availabe styles: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#For example,using the 'bmh' style
plt.style.use("bmh")
#the remaining are the same as above
#For example,using the 'seaborn' style
plt.style.use("seaborn-colorblind")
#the remaining are the same as above
#color friendly options:'seaborn-colorblind'or 'tableau-colorblind10',to reduce the dark background
#if print 'black and white',using the 'grayscale' style

##Saving your viz##
#For example:a figure to share
fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
plt.show()
#using the unix ls function,which give a listing of the files in the present working directory
ls #only the file we created is present
#different file format
fig.savefig("gold_medals.jpg") #provide lossless compression of your image
fig.savefig("gold_medals.jpg",quality=50)
fig.savefig("gold_medals.svg") #produce a vector graphics file where elements can be edited by advanced graphics software
#Resolution
fig.savefig("gold_medals.png", dpi=300) #control the quality of graph,this stands for dots per inch.The higher the number,the more densely the image will be rendered.
#size
fig.set_size_inches([5, 3])

##Automating figures from data##
#Automate:ease and speed,flexibilty,robustness,reproducibilty
#how many different kinds of data?
summer_2016_medals["Sport"]
#getting unique values of a column
sports = summer_2016_medals["Sport"].unique()
print(sports)
['Rowing' 'Taekwondo' 'Handball' 'Wrestling'
'Gymnastics' 'Swimming' 'Basketball' 'Boxing'
'Volleyball' 'Athletics'] #tell me that there are 10 brunches of sport over here
#bar-chart of heights for all sports
fig, ax = plt.subplots()
for sport in sports:  #write a loop over them
  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport] #we set a loop variable called sport to be equal to one of these unique values
  ax.bar(sport, sport_df["Height"].mean(),
         yerr=sport_df["Height"].std()) #for athletes in each one of the sports,with a std error bar
ax.set_ylabel("Height (cm)")
ax.set_xticklabels(sports, rotation=90)
plt.show()

#plotting data 3D
https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html
#visualzing images 
https://matplotlib.org/2.0.2/users/image_tutorial.html
#geographical data
https://scitools.org.uk/cartopy/docs/latest/
#pandas+Matplotlib=Seaborn
seaborn.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
                sizes=(40, 400), alpha=.5, palette="muted",
                height=6, data=mpg)
https://seaborn.pydata.org/examples/index.html
