# Cardio Catch Diseases

## Predicting cardiovascular diseases

![](img_banner_title.png)

# 1. Business Problem.
**Company name:** Cardio Catch Disease.

**Product/Service:** The company offers a service that detects cardiovascular disease at early stages.

**Business Model:**

- The cost per diagnosis, is around BRL 1.000,00;
- The price that the customer pays, vary depending on the precision;
- For every 5% above 50% the customer pays aditional BRL 500,00;
  - If the precision is 50% or below: Customer does not pay;
  - If the precision is 55%: Customer pays BRL 500,00;
  - If the precision is 60%: Customer pays BRL 1.000,00, and so on.

**Current Situation:**

- The diagnosis are made manually by a team of specialists;
- The current precision vary between 55% and 65%.

**Problem:**

- The current precision is low to be profitable (sometimes the cost is higher than what is charged);
- The diagnosis takes some time to be ready due to be made manually.

**Proposed Solution:**

- Create a classification model that returns a better precision of the diagnosis and help the specialists on the diagnosis.

**Main questions to be answered:**

- How much is the precision and accuracy?
- How much more profit Cardio Catch Diseases will make with the classification model?
- How trustworthy is the result of the classification model?

# 2. Business Assumptions.

In this project we are going to assume the following:

- Information about blood pressure levels according to these sources:
  -  https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings
  -  https://www.healthline.com/health/high-blood-pressure-hypertension/blood-pressure-reading-explained#hypotension

- Information about Cholesterol levels according to this source:
  - https://www.insider.com/cholesterol-levels-by-age

- Information about glucose levels according to this source:
  - https://www.emedihealth.com/glands-hormones/diabetes/manage-diabetes

- We are going to assume that a person is active if he/she does exercises at least 3 times a week.
  - Is active: => 3
  - Not active: < 3

# 3. Solution Strategy

**Step 01. Data Description:** Use basic statistics metrics to identify data outside the scope of business.

**Step 02. Check Outliers:** Check if there are outliers on the dataset based on the assumptions cited previously.

**Step 03. Feature Engineering:** Derive new features from the original dataset that could help better explain causes of cardiovascular diseases.

**Step 04. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

**Step 05. Data Preparation:** Prepare the data to be used on the model. (Exe: Scaling, encoding)

**Step 06. Feature Selection:** Select features that are most significant that better explain the phenomenon (Cardiovascular Disease).

**Step 07. Machine Learning:** Train and test models and analysis of the models performance.

**Step 08. Cross Validation Scoring:** Compare the performance of the models through cross validation and selection of the best model.

**Step 09. Hyperparameter Fine Tuning:** Choose the best parameters of the model that maximize performance.

**Step 10. Translation and Interpretation of the Error:** Convert the performance of the machine learning model into business results.

**Step 11. Deploy Model to Production:** Publish the model in a cloud environment so that other people or services can use the results to improve the business decision.

# 4. Top 3 Data Insights
**Hypothesis:** There are more cases of cardiovascular disease in patients that smokes.
  - FALSE: There are more cases of cardiovascular diseases in patientes that don't smoke.

**Hypothesis:** There are more cases of cardiovascular disease in patients that drinks alcohol.
  - FALSE: There are more cases in patients that drinks alcohol.

**Hypothesis:** There are more cases of cardiovascular disease in patients that are taller.
  - TRUE: But also, there are more cardiovascular diseases in very short patients (shorter than 155 cm).

# 5. Machine Learning Model Performance
- The model select in this project was Logistic Regression.
- The model have the following performance:

Metric | Accuracy | Precision | Recall | F1-Score | ROC-AUC
--- | --- | --- | --- | --- |---
Mean | 72.498 | 75.262 | 66.129 | 70.4 | 78.908
STD | 0.740645 | 0.968386 | 0.649506 | 0.751531 | 0.926499

The Logistic Regression was chosen because it has a better balance of Precision and Recall, where precision is what the business is based on for charging and recall minimizes the false negative rate, which is important in this case where we are diagnosing a disease.

# 6. Business Results
- Current Situation:
  - The cost per diagnosis, is BRL 1.000,00
  - For every 5% above 50% the customer pays aditional BRL 500,00
  - Currently the precision of the diagnoses vary between 55% and 65%
  - So the price vary between BRL 500,00 and BRL 1.500,00
  
- Implementing the model:
  - The model have precision of 75.19% with a standard deviation of 0.94%
  - This means that in average the precision of the model vary from 74.25% to 76.13%
  - So the price vary between BRL 2.000,00 and BRL 2.500,00
  - This makes the diagnosis more profitable where in the worst case, the company would profit at least BRL 1.000,00 (precision of < 75%)

Scenarios | Current Precision | Profit | Model Precision | Profit
--- | --- | --- | --- | ---
Average | 60.0 | 0.0 | 75.19 | 1.500,0
Worst Case | 55.0 | -500,0 | 74.25 | 1.000,0
Best Case | 65.0 | 500.0 | 76.13 | 1.500,0

# 7. Conclusions


# 8. Lessons Learned

# 9. Next Steps to Improve
