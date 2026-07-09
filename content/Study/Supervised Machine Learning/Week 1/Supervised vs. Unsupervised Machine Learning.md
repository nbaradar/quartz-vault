---
title: Supervised vs. Unsupervised Machine Learning
tags:
  - study
  - coursera-sml
draft:
created: 2025-06-19

modified: 2025-09-19
published: 2025-06-19

---
> [!example] [[Overview of Machine Learning|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Linear Regression Models|Next Lesson ->]]
## Supervised Learning: Regression
**[[Supervised Learning|Supervised Machine Learning]]** refers to algorithms that learn `x` -> `y` or `input` -> `output` mappings. 

You give your learning algorithm examples to learn from, with the right answer (correct `y` for `x`), and the algorithm eventually learns to take just the `input` alone without the `output` label and gives a reasonably accurate prediction or guess of what the `output` should be.

#### Application Examples

![[Pasted image 20250619184359.png|600]]

#### Specific Example: Housing Prices
Say you want to predict housing prices based on house size. You've collected some data:

![[Pasted image 20250619185457.png|400]]

Now your friend wants to know the price of a 750sqft house. How can we help them with our data? Well first we could just use a linear trend line to estimate the value...

![[Pasted image 20250619185714.png|400]]

Which looks like it comes out to ~150k. BUT fitting a linear trend line isn't the only algorithm you can use. There are others that would work better for this application. 

For example, you may decide a curve fits better on this data than a linear trend line since it captures more complexity. Well if we decided to use a curve...

![[Pasted image 20250619190331.png|400]]

Now your friends same house is predicted to be worth ~200k. Part of being a good machine learning engineer is knowing the best algorithm/function to apply to a subset of data. You can also get an algorithm to systematically choose the most appropriate line or curve or other function to fit this data.

This is supervised learning because you are giving the algorithm a bunch of `inputs` (house size) and `outputs` (price), and are asking the learning algorithm to produce more of these right answers. 

This housing price prediction is the particular type of supervised learning called [[Regression]] (we're trying to predict a number from infinitely many possible numbers)

>[!abstract] Summary: 
>Supervised Learning = Learning `x` -> `y` or `input` -> `output` mappings

---
## Supervised Learning: Classification
There is a second major type of supervised learning algorithm called [[Classification]].

#### Example: Breast Cancer Detection
Say you are building a machine learning system to detect breast cancer. Using a patient's medical records your machine learning system tries to figure out if a tumor is **malignant** (cancerous or dangerous) or **benign** (non dangerous lump).

Your dataset has tumors of various **sizes**, labeled with `benign: 0` or `malignant: 1`. 
![[Pasted image 20250619194302.png|600]]

Classification is **only trying to predict a FINITE number of possible outputs**, in this case two (0 or 1). 

This is different from Regression, which tries to **predict any number from an INFINITE set of possible outputs**

Let's say you have a patient that comes in with a 7cm lump. Using your machine learning system, how could you predict whether it is cancerous? 

![[Pasted image 20250619195629.png|500]]

This is too simplistic. Thankfully, Classification problems allow you to have more than just two possible output categories. _(NOTE: The terms `Output Category` and `Output Class` are interchangeable)_

So instead, lets have multiple `malignant` categories that represent different types of cancer diagnoses:
- `malignant type 1`
- `malignant type 2`

![[Pasted image 20250619200143.png|500]]

Classification algorithms predict **Categories**. Categories **can be non-numeric**. Like 'cats' vs 'dogs'
Categories **_could_ be numbers**, but the set of possible output numbers are **SMALL** and **FINITE**

You can also use more than 1 input value to predict output categories. In our example, we were only using **tumor size**. Let's also use **patient age**. Now your dataset has 2 inputs.

![[Pasted image 20250619201416.png|400]]

If a patient of a certain age and tumor size was presented (in yellow), how would the Classification algorithm predict the presence of cancer? Given a dataset like this, it could find a **_boundary_** that seperates malignant tumors from benign ones. The learning algorithm would be responsible for figuring out this boundary line. 

![[Pasted image 20250619201715.png|400]]

In this case, the tumor is more likely to be benign. This could help the doctor with a diagnosis. In real-world examples, _many_ more input values are required. In this example we could also use the thickness of the tumor clump, uniformity of the cell size, uniformity of the cell shape and so on.

>[!question]- Supervised learning is when we give our learning algorithm the right answer _y_  for each example to learn from.  Which is an example of supervised learning: Spam Filtering OR Calculating the average age of a group of customers?
>>A: Spam Filtering
>
> For instance, emails labeled as "spam" or "not spam" are examples used for training a supervised learning algorithm. The trained algorithm will then be able to predict with some degree of accuracy whether an unseen email is spam or not.

---
## Unsupervised Learning: Part 1

Say you're given data on patients and their tumor size and the patient's age. But not whether the tumor was benign or malignant. We're not asked to diagnose whether the tumor is benign or malignant, because we're not given any labels (we don't know the outputs to these inputs). Instead we want to find some **structure** or a **pattern** in the data. 

![[Pasted image 20250619203559.png|400]]

This is known as [[Unsupervised Learning]]. We don't ask it to give us a "right" output for every input. We don't "supervise" the algorithm. 

### Clustering
A type of Unsupervised learning method. The algorithm may decide that data can be organized in clusters of data:

![[Pasted image 20250619204147.png|350]]

#### Example: Google News
For example, clustering is used in Google News. They use Unsupervised Learning to look at 1000s of articles every day to find related articles. Notice how in the below screenshot, the clustering algorithm is finding articles with the same keywords
![[Pasted image 20250619204456.png|600]]

There is no employee at Google telling the algorithm to find the words `panda` and `twin` and `zoo` and put them into the same cluster. Instead, the algorithm finds out without supervision what articles should be added to a cluster on any given day.

> [!example] [[Overview of Machine Learning|<- Previous Lesson]] | [[Supervised Machine Learning|Home]] | [[Linear Regression Models|Next Lesson ->]]