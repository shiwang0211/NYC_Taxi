Overview
========

This repository aims to analyze the NYC taxi trip duration dataset from a Kaggle competition:

[https://www.kaggle.com/c/nyc-taxi-trip-duration](https://www.kaggle.com/c/nyc-taxi-trip-duration)

<br>

The applied techniques include:
- Utilize Pandas, Numpy, Seaborn to manipulate dataframes and visualize results
- Utilize sklearn, xgboost for model development

<br>

My current progress:
- [x] Basic exploratory data analysis
- [x] Feature engineering
- [x] Build XGB model and generate predictions
- [ ] Explore the possibility of network analysis
- [ ] Further tune the XGB model parameters

<br>

Some visualizations are provide below:
------

Distribution of log(Trip Duration) | Heatmap of trip distribution
:-------------------------:|:-------------------------:
<img src="/fig/Log Trip Duration His.png" width="500">  |  <img src="/fig/pickup_hour_and_pickup_weekday_Pivot.png" width="500">


K-Means clusters of pick-up/drop-off locations | Relationship between time and distance
:-------------------------:|:-------------------------:
<img src="/fig/Map_Plot_PickUp.png" width="500"> | <img src="/fig/Time_Distance_Pivot.png" width="500">


Feature importance from XGB 

<img src="/fig/Feature_Imp_XGB.png" width="500"> 


Contact
=======

Shi Wang (<shiwang0211@gmail.com>)
