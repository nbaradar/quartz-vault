---
title: Week 1 Quiz
tags:
  - study
  - coursera-sml
draft:
created: 2026-08-08
modified: 2026-08-08
published: 2026-08-08
---
> [!example] [[Training a Linear Regression Model|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Multiple Features|Next Lesson ->]]

---
# Question 1

Gradient descent is an algorithm for finding values of parameters w and b that minimize the cost function J: 
![[Pasted image 20260808195813.png]]

When  $\frac{\partial J(w,b)}{\partial w}$  is a negative number (less than zero), what happens to `w` after one update step?
- `w` increases.
- `w` decreases
- It is not possible to tell if `w` will increase or decrease.
- `w` stays the same

>[!SUCCESS]- Answer
>w increases
>
>The learning rate is always a positive number, so if you take W minus a negative number, you end up with a new value for W that is larger (more positive).

# Question 2

For linear regression, what is the update step for parameter b?

$b = b - \alpha \frac{1}{m} \sum_{i=1}^{m} \left(f_{w,b}(x^{(i)}) - y^{(i)}\right)x^{(i)}$

$b = b - \alpha \frac{1}{m} \sum_{i=1}^{m} \left(f_{w,b}(x^{(i)}) - y^{(i)}\right)$

>[!SUCCESS]- Answer
>$b = b - \alpha \frac{1}{m} \sum_{i=1}^{m} \left(f_{w,b}(x^{(i)}) - y^{(i)}\right)$ 
> 
> the first option is the update step for parameter w, and should be `w = w - alpha...' 

---
> [!example] [[Training a Linear Regression Model|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Multiple Features|Next Lesson ->]]