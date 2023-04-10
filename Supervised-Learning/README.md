## Analysis

This analysis was to use machine learning to predict whether a loan would be a healthy or a high-risk investment.  A liner model using sklearn was created to determine an accuracy score, generate a confusion matrix and a final classification report.

## Results

* Machine Learning Training Model:

<img width="419" alt="Screen Shot 2023-04-10 at 11 51 17 AM" src="https://user-images.githubusercontent.com/116044037/230950322-d25d92b9-4c57-46b6-b498-4f5f34286755.png">

Note: Label 0 represents a healthy investment and label 1 indicates a high-risk investment.

The results showed that the model had a high level of precision and recall for both healthy and high-risk loans. The precision for label 0 (healthy investments) was 1.00 and recall was 0.99, while for label 1 (high risk investments) the precision was 0.85 and recall was 0.89. Overall, the model achieved 99% accuracy with 18,765 loans predicted as healthy and 619 loans predicted as high-risk.

In general, the model performed well with high levels of precision and recall for both healthy and high-risk loans. , but it has slightly lower accuracy for predicting high-risk cases compared to healthy cases.

## Summary

Overall the model was 99% accurate reporting 18,765 loans as healthy and 619 as high-risk. To improve the model's performance, adjustments could be made to more accurately identify high-risk loans. Despite this, the model's overall accuracy was high, and it would be sufficient for use as only 56 loans were falsely classified as high-risk.
