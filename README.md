# MMJ Analytics
<br />
<br />
<br />

# Transit Systems of the World
![](images/train-cover.jpg)

***
<br />

## Table of Contents
- [Introduction](#introduction)
- [Overall](#overall)
    - [Top 5 Countries](#top-5-countries)
    - [Transit Lines Opened per Year](#transit-lines-opened-per-year)
    - [Track Length vs Number of Track](#track-length--number-of-tracks-correlation)
- [United States](#united-states)
    - [US Transit Line Counts](#us-transit-line-counts)
    - [US Heatmap](#us-heatmap)
    - [New York Data](#new-york-data)
<br />
<br />

***
## **Introduction**
***
This dataset, which can be found [here](https://www.kaggle.com/datasets/citylines/city-lines), includes transportation line data from a number of cities from around the world including London, Berlin, Mexico City, Barcelona, Washington D.C., and others covering many thousands of kilometers of lines.
<br />
<br />

***
## **Overall**
***
The data mentioned above informs people of several different factors pertaining to transportation lines around the world. An initial glimpse of the data, allowed us to indentify how the data was spread amongst the countries in the [cities]("data/cities.csv) data. As you can see, the United States has an overwhelming amount of cities with stations compared to the rest of the countries within the data.<br />
This led us to indetify the [top five](#top-5-countries) countries to see how the United States compared.
![](images/iqr_plot.png)
<br />
<br />

### Top 5 Countries
The further comparison of the top five countries shows when each had station openings and how many in that particular year. It is interesting to note that the top country, United States, built a majority of its transportation lines between 1875 and and 1925. Which will be highlighted again in a [New York] analysis. 
![](images/top_5.png)
<br />

### Transit Lines Opened per Year
![](images/Transit_lines_opened_per_year.png)
<br />

### Average Track Length Comparison by Country
This bar plot shows variation between the average length of transit lines in each country.
![](images/track_length_number_correlation.png)

***
## United States
***

### US Transit Line Counts
After indentifying the United States held the most cities, further analysis was conducted on those cities within the United States. What can be immeditaely identified is that the cities withing the United States are large metropolitan cities. With [New York](#new-york-data) having the most stations.

It is important to note that there are other cities within the United States that host transportation stations, however the [station](data/stations.csv) data does not hold information for those cities not listed. This is important to note this is one limitation of this data set.

![](images/us_transit_lines.png)
<br />
<br />

### US Heatmap
Additinally cities within the United States that host a transportation station are represented below with the a provides a visual representation of the density of the stations within those cities.

![](images/us_heatmap.png) 

Click this [interactive map](http://127.0.0.1:5500/images/us_heatmap.html) to view and zoom to certain areas.
<br />
<br />

### New York Data
As previously identified, New York held the most stations in the United States. Additionaly, it was noted that the United States opened the majority of tracks were opened between the 1875 and 1925. This further highlights the stark buildup during that time period and followed by a tappering of openings.

![](images/new_york_track_length.png)