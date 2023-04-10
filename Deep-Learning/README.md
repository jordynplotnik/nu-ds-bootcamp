## Overview:

The nonprofit, Alphabet Soup wants a machine learning tool to predict the success of future funding applicants. They have provided a dataset containing over 34,000 organizations that have previously received funding. This analysis will evaluate the model with the goal of achieveing high accuracy

## Results: 

# Data Preprocessing

* Target: Determine whether or not a loan was successful using the "IS_SUCCESSFUL" value
* Feature Variables: Application Type, Affiliation, Classification, Use Case, Status, Income Amount, Special Considerations, and Ask Amount 
* Variables that are neither targets nor features: EIN, and Name

# Compiling, Training, and Evaluating the Model
* Neurons, layers, and activation functions: 2 layers were used: 24 neurons in the first layer, and 16 in the second. Also, the relu activation function was used.
* Target model performance: No
* Steps to increase model performance: Dropped more columns (Status, Special Considerations), increased "Other" threshold, etc. 


# Summary: 
The model did not achieve the desired accuracy of 75%. However, after attempting to update the model by cleaning up the columns and data, there was a slight increase in the final accuracy, resulting in an accuracy of ___

