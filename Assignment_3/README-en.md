<div align="center">
  
# Naïve Bayes Algorithm Implementation
*Building a Machine Learning classification model using Python.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=jupyter&logoColor=white)
![Math](https://img.shields.io/badge/Mathematics-00599C?style=for-the-badge&logo=databricks&logoColor=white)

</div>

---

## Group Information
* **Group:** 3
* **Team Members:**

|    NRP     |      Name      |
| :--------: | :-------------: |
| 5025241044 | Ahmad Loka Arziki |
| 5025241129 | Mochamad Ramadhan Aditya Rachaman |
| 5025241147 | Lucky Himawan Prasetya |
| 5025241216 | Muhammad Daffa Ramadhan |  

---

## Applied Concept: Naïve Bayes Algorithm

> **Main Question:** *"Given the existing features, which class is the most probable?"*

**Bayes' Theorem** provides a principled way to reverse conditional probabilities. It is defined as:

$$P(y|X) = \frac{P(X|y) \cdot P(y)}{P(X)}$$

**Where:**
* $P(y|X)$ : *Posterior probability, probability of class y given features X*
* $P(X|y)$ : *Likelihood, probability of features X given class y*
* $P(y)$ : *Prior probability of class y*
* $P(X)$ : *Marginal likelihood or evidence*

### How the Algorithm Works
The Naive Bayes algorithm uses the principles of Bayes' Theorem above. The word **"Naive"** is used because it makes a strong assumption: **every feature in the data is strictly independent of each other**. 

With this assumption, we simply calculate the probability (*likelihood*) of each feature separately with respect to its target class, and then multiply them together. The class that yields the highest final (*posterior*) probability is selected as the prediction.

---

## Dataset: Play Football Decision

We use the **Play Football Decision Dataset**, a classic categorical classification dataset. The program utilizes 14 historical data records as its knowledge base.

<details>
<summary><b>Click to expand the Historical Data Table (14 Rows)</b></summary>
<br>

| No | Weather | Temp. | Humidity | Wind | Target |
|:--:|:---------|:------|:---------|:-------|:-----------------------|
| 1  | Sunny    | Hot   | High     | Weak   | **No** |
| 2  | Sunny    | Hot   | High     | Strong | **No** |
| 3  | Overcast | Hot   | High     | Weak   | **Yes** |
| 4  | Rainy    | Mild  | High     | Weak   | **Yes** |
| 5  | Rainy    | Cool  | Normal   | Weak   | **Yes** |
| 6  | Rainy    | Cool  | Normal   | Strong | **No** |
| 7  | Overcast | Cool  | Normal   | Strong | **Yes** |
| 8  | Sunny    | Mild  | High     | Weak   | **No** |
| 9  | Sunny    | Cool  | Normal   | Weak   | **Yes** |
| 10 | Rainy    | Mild  | Normal   | Weak   | **Yes** |
| 11 | Sunny    | Mild  | Normal   | Strong | **Yes** |
| 12 | Overcast | Mild  | High     | Strong | **Yes** |
| 13 | Overcast | Hot   | Normal   | Weak   | **Yes** |
| 14 | Rainy    | Mild  | High     | Strong | **No** |

*Statistics: 9 days resulted in "Yes", and 5 days resulted in "No".*
</details>

---

## Execution Results & Evaluation

This program does not utilize a percentage-based *train/test split*. Instead, it directly predicts a new test case based on the mathematical probability calculations from the table above.

**Evaluated Test Case:**
> *Weather: **Sunny** | Temperature: **Cool** | Humidity: **High** | Wind: **Strong***

### Algorithm Calculation Log:
1. **Prior Probability:**
   * $P(Yes) = \frac{9}{14} = 0.6429$
   * $P(No) = \frac{5}{14} = 0.3571$
2. **Likelihood Probability (Combined):**
   * *P(Case | Yes)* = P(Sunny|Yes) $\cdot$ P(Cool|Yes) $\cdot$ P(High|Yes) $\cdot$ P(Strong|Yes)
   * *P(Case | No)* = P(Sunny|No) $\cdot$ P(Cool|No) $\cdot$ P(High|No) $\cdot$ P(Strong|No)
3. **Posterior Probability (Unnormalized):**
   * Final Probability **(Yes)** = `0.005291`
   * Final Probability **(No)** = `0.020571`

### Conclusion
Based on the system's manual calculation, the posterior probability for the **No** class `(0.020571)` is greater than the **Yes** class `(0.005291)`. Therefore, the algorithm predicts that under these weather conditions, the decision is: 
**NO (Cancel Playing Football)**.
