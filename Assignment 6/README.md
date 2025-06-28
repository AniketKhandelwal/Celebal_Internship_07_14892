
# Machine Learning Model Comparison and Selection using the Iris Dataset

## Overview

This project demonstrates how to build and compare multiple machine learning models using the Iris dataset. It covers the entire workflow including data preprocessing, model training, hyperparameter tuning with both GridSearchCV and RandomizedSearchCV, model evaluation using multiple metrics, and selecting the best-performing model.

---

## 1. Library Imports

We start by importing essential libraries for data manipulation, visualization, machine learning, and evaluation.

- pandas, numpy: For data handling and numerical operations
- matplotlib, seaborn: For plotting and visualizing data
- sklearn: For model training, preprocessing, and evaluation
  - sklearn.datasets.load_iris: To load the Iris dataset
  - sklearn.preprocessing.StandardScaler: To standardize feature scales
  - sklearn.model_selection: For train-test split and cross-validation
  - sklearn.pipeline.Pipeline: For chaining preprocessing and modeling steps
  - sklearn.metrics: For calculating performance metrics
  - sklearn.classifiers: For KNN, SVM, and Random Forest models

---

## 2. Data Loading and Preparation

The Iris dataset is loaded using sklearn's built-in function. It contains 150 rows and 4 features representing flower measurements.

- The feature matrix `X` is stored as a pandas DataFrame using the provided feature names.
- The target labels `y` represent three classes of iris species.

---

## 3. Train-Test Split

The dataset is split into training and testing subsets:

- 80 percent of the data is used for training
- 20 percent is used for testing
- A fixed random state is used to ensure reproducibility

---

## 4. Model Definitions and Hyperparameter Grids

We define three classification models:

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Random Forest Classifier

For each model, a set of hyperparameters is defined to be tuned using GridSearchCV. These hyperparameters include the number of neighbors for KNN, kernel type and regularization for SVM, and number of trees and depth for Random Forest.

The parameters are defined using the 'clf__' prefix because the models are part of a scikit-learn Pipeline.

---

## 5. Model Training, Hyperparameter Tuning, and Evaluation

Each model is trained and optimized through the following steps:

1. Create a Pipeline that standardizes features using StandardScaler and fits the classifier.
2. Use GridSearchCV to perform an exhaustive search over the hyperparameter space using 5-fold cross-validation.
   - Optionally, RandomizedSearchCV can be used for faster tuning.
3. Train the model and identify the best estimator.
4. Predict on the test set and evaluate using:
   - Accuracy
   - Precision (weighted)
   - Recall (weighted)
   - F1-Score (weighted)
5. Generate a classification report and store all metrics in a results list for comparison.

---

## 6. Cross-Validation Evaluation

To ensure stability and generalizability, the best models are also evaluated using cross-validation across the entire dataset.

- Mean accuracy is computed to assess overall performance
- Standard deviation is reported to evaluate consistency across folds

Example output:

```
KNN CV Accuracy: 0.9667 ± 0.0211
SVM CV Accuracy: 0.9667 ± 0.0211
RandomForest CV Accuracy: 0.9667 ± 0.0211
```

---

## 7. Model Selection Justification

Based on performance metrics, all three models performed equally well. However, the Random Forest Classifier was selected as the final model due to the following reasons:

- Consistently high accuracy and F1-score
- Robust performance across different random states
- Ability to output feature importance for interpretability
- Faster prediction times compared to KNN
- Better scalability than SVM on larger datasets
- Built-in resistance to overfitting due to ensemble nature

---

## 8. Conclusion

This project demonstrates a complete machine learning pipeline using the Iris dataset. It includes:

- Preprocessing and scaling
- Model comparison and tuning using GridSearchCV
- Evaluation with multiple performance metrics
- Cross-validation to assess generalization
- Justified selection of the best model for deployment

The final selected model, Random Forest Classifier, balances accuracy, interpretability, and robustness, making it well-suited for further use or deployment.
