data={"bangalore":[("15-12-2025",35.961),("16-12-2025",36.075),("17-12-2025",31.390),("18-12-2025",27.773),("19-12-2025",29.384),("20-12-2025",32.807),("21-12-2025",34.218),("22-12-2025",34.655),("23-12-2025",33.319),("24-12-2025",32.941),("25-12-2025",33.123),("26-12-2025",32.108)],
"bhubaneswar":[("15-12-2025",97.763),("16-12-2025",100.821),("17-12-2025",100.723),("18-12-2025",110.232),("19-12-2025",116.319),("20-12-2025",113.983),("21-12-2025",113.294),("22-12-2025",117.522),("23-12-2025",121.386),("24-12-2025",114.766),("25-12-2025",111.802),("26-12-2025",111.694)],
"chennai":[("15-12-2025",77.792),("16-12-2025",77.792),("17-12-2025",57.929),("18-12-2025",51.753),("19-12-2025",60.974),("20-12-2025",69.207),("21-12-2025",81.232),("22-12-2025",81.496),("23-12-2025",86.484),("24-12-2025",86.232),("25-12-2025",101.021),("26-12-2025",65.438)],
"delhi":[("15-12-2025",243.541),("16-12-2025",180.833),("17-12-2025",213.181),("18-12-2025",290.833),("19-12-2025",224.333),("20-12-2025",272.000),("21-12-2025",239.333),("22-12-2025",321.958),("23-12-2025",235.125),("24-12-2025",99.875),("25-12-2025",127.333),("26-12-2025",199.5)],
"jodhpur":[("15-12-2025",35.898),("16-12-2025",33.388),("17-12-2025",51.457),("18-12-2025",39.023),("19-12-2025",48.423),("20-12-2025",62.317),("21-12-2025",48.527),("22-12-2025",67.011),("23-12-2025",81.833),("24-12-2025",55.171),("25-12-2025",28.388),("26-12-2025",40.604)],
"kolkata":[("15-12-2025",51.183),("16-12-2025",62.971),("17-12-2025",62.273),("18-12-2025",56.042),("19-12-2025",48.320),("20-12-2025",66.151),("21-12-2025",64.722),("22-12-2025",65.080),("23-12-2025",67.409),("24-12-2025",74.062),("25-12-2025",68.907),("26-12-2025",76.936)],
"lucknow":[("15-12-2025",95.543),("16-12-2025",88.524),("17-12-2025",98.087),("18-12-2025",110.476),("19-12-2025",50.513),("20-12-2025",73.476),("21-12-2025",90.765),("22-12-2025",108.278),("23-12-2025",93.951),("24-12-2025",77.353),("25-12-2025",61.928),("26-12-2025",99.887)],
"mumbai":[("15-12-2025",51.496),("16-12-2025",54.370),("17-12-2025",53.078),("18-12-2025",54.725),("19-12-2025",50.835),("24-12-2025",61.002),("25-12-2025",53.690),("26-12-2025",56.841)],
"raipur":[("15-12-2025",36.266),("16-12-2025",33.659),("17-12-2025",29.012),("18-12-2025",20.061),("19-12-2025",16.893),("20-12-2025",17.118),("21-12-2025",26.953),("22-12-2025",23.699),("23-12-2025",26.642),("24-12-2025",32.228),("25-12-2025",23.857),("26-12-2025",27.778)]}

#every city's average 
city_average={}
for city, records in data.items():
    values = [v for _,v in records]
    city_average[city] = sum(values) / len(values)
print(city_average)

#Line graph of daily averages of cities
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(12,6))
for city, records in data.items():
    dates=[d for d, _ in records]
    values=[v for _,v in records]
    ax.plot(dates, values,marker='o',label= city)
ax.set_xlabel('Date')
ax.set_ylabel('PM 2.5 Level(µg/m³)')
ax.set_title("PM2.5 variation over time(city-wise)")
plt.axhline(y=15, linestyle='--', color='red', linewidth=2, label='WHO daily limit(15 µg/m³)')
ax.legend()
plt.tight_layout()
plt.xticks(rotation=30)
plt.show()

#Bar Graph of averages of cities for all days
cities=list(city_average.keys())
avg_values=list(city_average.values())
plt.bar(cities,avg_values)
plt.xlabel("City")
plt.ylabel("Average PM2.5")
plt.title("Average PM2.5 across cities")
plt.axhline(y=15, linestyle='--', color='red', linewidth=2, label='WHO daily limit(15 µg/m³)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Coefficient of variation=standard deviation/mean
city_stats={}
for city, records in data.items():
    airpol=[pm for _,pm in records]
    n=len(airpol)
    
    mean=city_average[city]
    #variance
    squared_difference=[(x-mean)**2 for x in airpol]
    variance=sum(squared_difference)/(n-1)
    standard_deviation=variance**0.5
    coefficient_of_variation= standard_deviation/mean
    city_stats[city]={"mean":mean,"coefficient of variation":coefficient_of_variation}
print(city_stats)

#scatter plot
cities = list(city_stats.keys())
means  = [city_stats[city]["mean"] for city in cities]
cvs    = [city_stats[city]["coefficient of variation"]   for city in cities]
fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(means, cvs)
ax.set_xlabel("Mean PM2.5 (µg/m³)")
ax.set_ylabel("Coefficient of Variation (CV)")
ax.set_title("Mean vs Variability of PM2.5 Across Cities")
for city, x, y in zip(cities, means, cvs):
    ax.text(x, y, city, fontsize=9, ha='right', va='bottom')
plt.tight_layout()
plt.show()