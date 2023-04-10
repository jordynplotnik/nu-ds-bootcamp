## Analysis

In this repository, machine learning was used to predict whether a loan would be a healthy or a high-risk investment. A linear model was created using sklearn to determine the accuracy score, generate a confusion matrix, and produce a final classification report.

## Results from Training Model

<img width="419" alt="Screen Shot 2023-04-10 at 11 51 17 AM" src="https://user-images.githubusercontent.com/116044037/230950322-d25d92b9-4c57-46b6-b498-4f5f34286755.png">

Note: Label 0 represents a healthy investment, and label 1 indicates a high-risk investment.

The results showed that the model had a high level of precision and recall for both healthy and high-risk loans. The precision for label 0 (healthy investments) was 1.00, and recall was 0.99. For label 1 (high-risk investments), the precision was 0.85, and recall was 0.89. Overall, the model achieved 99% accuracy, with 18,765 loans predicted as healthy and 619 loans predicted as high-risk.

## Summary

Overall, this model was a good predictor of credit risk for both healthy loans and high-risk loans, even though it had slightly lower accuracy for predicting high-risk loans compared to healthy ones. The model was 99% accurate in reporting that 18,765 loans were healthy, and 619 were high-risk. To improve the model's performance, adjustments could be made to more accurately identify high-risk loans.
