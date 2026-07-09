---
title: Cost Function
tags:
  - study
  - coursera-sml
draft:
created: 2025-08-29

modified: 2025-12-15
published: 2025-08-29

---
>[!example] [[Linear Regression Models|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[quartz/content/Study/Supervised Machine Learning/Week 1/Gradient Descent|Next Lesson ->]]

The **cost function** tells us **how well the model is doing** so we can try to improve it.

**Model**: $f_{w,b} (x) = wx + b$

This is our training set for the model ($f_{w,b} (x) = wx + b$) :
![[Pasted image 20251205171444.png|400]]

$w, b$ : **parameters** (also referred to as **coefficients** / **weights**)

Parameters are the variables you can adjust during training to improve the model. Depending on the values you chose for $w, b$, you'll get a different function $f(x)$ 

Let's graph different values for $f(x)$ based on $w, b$
![[Pasted image 20251205172213.png|700]]
You can intuit that w dictates the slope of f(x)

You want to find correct values for $w, b$ so that $f_{w,b}$ matches your training set. 
![[Pasted image 20251205172436.png|300]]

$x^{(i)}, y^{(i)}$ is a training example. y is the target

![[Pasted image 20251211172620.png|500]]
The **Squared Error Cost Function** is one type of many cost functions that machine learning engineers could use depending on the model they are building. It is also the most commonly used Cost Function, especially for [[Linear Regression Models]]. 

To build a cost function that doesn't get too large based on the number of training examples $(m)$ we compute the **average** squared error instead of **total** squared error by dividing by $1/2m$ 

You can also write the cost function like this:
![[Pasted image 20251211174124.png|400]]

We can replace the prediction $\hat{y}^{(i)}$ with $f_{w,b} (x^{(i)})$ 

>[!question]- This is the cost function: $J(w, b) = \frac1{2m} \sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^2$. Which of these are the parameters of the model that can be adjusted? 
> **Answer**: $w$ and $b$ are parameters of the model, adjusted as the model learns from the data. They’re also referred to as “coefficients” or “weights”


When using the model $f_{w,b} (x) = wx + b$ we want to find the parameters $w, b$ that best fit our training set.

We use the cost function for this. 
$J(w, b) = \frac1{2m} \sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^2$

The goal is to minimize $J(w, b)$ which will give us our desired params

If we were to graph the squared cost function for a linear regression model with $w, b$ params it would look something like this, but slightly different based on training set. Both w and b are on the x axis below.
![[Pasted image 20251212222949.png|700]]

This is known as a contour plot, which is similar to topographical maps 
![[Pasted image 20251212223338.png|300]]

![[Pasted image 20251212223658.png|900]]

The plot on the top right is the horizontal slices of the contour plot below. This is why the same J error rate is on the same colored slice. 

>[!question]- For $f_{w,b} (x) = wx + b$, which of the following are the **inputs** that are fed to the model? A: $m$ | B: $(x, y)$ | C: $w$ and $b$ | D: $x$
> **Answer:** D: $x$

>[!question]- For linear regression, if you find parameters $w$ and $b$ so that $J(w, b)$ is very close to zero, what can you conclude? 
> **Answer:** The selected values of the parameters $w$ and $b$ cause the algorithm to fit the training set well

>[!example] [[Linear Regression Models|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[quartz/content/Study/Supervised Machine Learning/Week 1/Gradient Descent|Next Lesson ->]]

