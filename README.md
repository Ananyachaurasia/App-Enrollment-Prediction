# Directing Customers Through App Behavior Analysis

## Introduction

* In today's market, a lot of companies provide free services in their mobile applications in order, usually for a limited time, in order to attract customers/clients to subscribe in their permium service which includes all features for unlimited time.

* In order to attract the most possible number of these customers, they need to focus on targeting the customers who used the mobile application but didn't subscribe yet for the permium services in order to give them discounts and offers that may not that influential if offered to those who already have the intention to subscribe in all cases.

* We are going to build a model that predicts which users won't subscribe to the paid membership so that the greater marketing efforts can go into trying to convert them to paid users.

## Data

* The [dataset](https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P39-CS3-Data.zip) used is a fintech company that wants to provide its customers with a paid mobile app subscription that will allow them to track all of their finances in one place.

* To attract customers, the company releases a free version of their app with some of the main features unlocked. The company wants to identify which users will not likely to enroll in the paid product, so that additional offers can be given to them and not to everybody specially that there will be customers who are going to enroll anyway.

* The dataset contains 50 thousand records (row) each has 12 columns including our target the enrollement status as following:

|        Column        |                                     Description                                     |
|:--------------------:|:-----------------------------------------------------------------------------------:|
|         user         |                                       User ID                                       |
|      first_open      |              The time where the user opened the app for the first time              |
|       dayofweek      |         The index of the day on which the app was opened for the first time         |
|         hour         |               The hour at which the app was opened for the first time               |
|          age         |                                 The age of the user                                 |
|      screen_list     | A comma-separated string of all screens the user showed during the usage of the app |
|      numscreens      |               The number of screens showed during the usage of the app              |
|       minigame       |                   If the user played the mini game (1) or not (0)                   |
|         liked        |                If the user liked the app on the store (1) or not (0)                |
| used_premium_feature |                  If the user used a premium feature (1) or not (0)                  |
|       enrolled       |         If the user actually enrolled in the paid membership (1) or not (0)         |
|     enrolled_date    |              The data on which the user enrolled in the paid membership             |



## Feature Engineering

### Response Time

* In order to make a model that is valid in the future. We need to a set a time limit after which we can look if that customer enrolled or not. We will take that threshold by taking a reasonable time that involves the majority of the customers who enrolled in the membership.

* To calculate the time taken for each customer to response, we will subtract the enrollement time from the first open time.

We will take the time threshold at 48 hours (2 days). After that, the customer will be considered unrolled as we will check the model's performance after 2 days of operating it.


## Screens

* We want to divide the `screen_list` into separated columns each correspond to a specific type of the screens (saving, loans, credit, other)

* We have a separate .csv file ('top_screens.csv') that contains the top and most-viewed screens.

## Results

Using `LogisticRegression` class from, we achieved 77% accuracy.
