---
title: Training a Linear Regression Model
tags:
  - study
  - coursera-sml
  - gradient-descent
draft:
created: 2026-08-08
modified: 2026-08-08
published: 2026-08-08
---
> [!example] [[Gradient Descent|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Week 1 Quiz|Next Lesson ->]]

---
## Gradient Descent for Linear Regression
Let's use what we learned about... 

[[Linear Regression Models]]
![[Pasted image 20260808193120.png|300]]

[[Cost Function]],
![[Pasted image 20260808193154.png|300]]

[[Gradient Descent]] 
![[Pasted image 20260808193217.png|300]]

To train a linear regression model to fit a straight line through our training data. 
The derivatives in the gradient descent algo can also be written like this:
![[Pasted image 20260808194342.png|400]]

The first is the derivative in respect to `w`, the second is the derivative in respect to `b`. These formulas are derived using calculus. Understanding how this derivation works is completely optional, and can be found below
>[!Tip]- Optional Calculus Derivation 
> ![[Pasted image 20260808194605.png]]

One of the nice things about implementing gradient descent over a squared error cost function is that the function is a convex function, meaning it has a single global minimum
![[Pasted image 20260808194202.png|600]]

## Running Gradient Descent

---
> [!example] [[Gradient Descent|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Week 1 Quiz|Next Lesson ->]]