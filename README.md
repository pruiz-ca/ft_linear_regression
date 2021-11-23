# 🔮 ft_linear_regression

This program is an introduction to machine learning. It predicts the price of a car by using a linear function training with a gradient descent algorithm

<p align=center><img src=https://user-images.githubusercontent.com/74905890/142940340-025ab667-17b5-42db-afae-a2d60e3cc5b4.gif></img></p>

## Basic concepts
Linear regression: way to explain the relationship between a dependent variable and one (or more) explanatory variables using a straight line (y = mx + b)

Gradient descent: optimization algorithm to find a local minimum of a function. In this case we are using a squared error cost function.
<p align=center><img width=300px src=https://user-images.githubusercontent.com/74905890/142947946-2e93dae2-6c78-492c-854a-8d8e300a7fbf.png></img></p>

## What we are doing
A linear equation has the form: y = mx + b
We want to guess m and b for the line closest to all points in our dataset to predict y with x.
We are using the squared error cost function, it has a convex shape and is calculated substracting the Y value between predicted values and real values. Why squared? to avoid sign differences between values that are above and below the predited line.
<p align=center><img width=300px src=https://user-images.githubusercontent.com/74905890/142948862-d130cbd3-7d24-416f-b8fc-c30ff21c26a2.png></img></p>

By taking the derivative at a definite point of the cost function we get the slope at that particular point. At the minimum of the curve that slope is 0, so that's where we want to get m and b. These ecuations to calculate m and b are given to us in the subject.

With the number of iterations and learning rate we are setting the speed at which we are going down the cost function until we reach the minimum.
<p align=center><img width=300px src=https://user-images.githubusercontent.com/74905890/142949226-ddf08fa2-15c3-4c50-9122-d207a9a18ef1.png></img></p>

## Using the model
- train.py: generate the prediction model and save it in thetas.csv
- predict.py: make a prediction based on user input
- accuracy.py: calculates R squared.
```
train.py <dataset> <"auto">
    - dataset: if empty uses "dataset.csv"
    - auto: with this keyword the model will stop automatically when the prediction is good enough
```

## Good learning material
https://github.com/42-AI/bootcamp_python

https://github.com/42-AI/bootcamp_machine-learning

https://www.coursera.org/learn/machine-learning/

## Other links
https://zhuanlan.zhihu.com/p/64201647

https://mashkarharis.medium.com/linear-regression-in-python-scikit-learn-526b57a11a09

https://en.wikipedia.org/wiki/Gradient_descent

https://en.wikipedia.org/wiki/Linear_regression
