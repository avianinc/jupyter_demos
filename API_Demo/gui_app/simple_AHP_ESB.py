#Import libraries
import numpy as np

#AHP Analysis of ESB, API, SOA and MOM technologies to support the implementation of an MBSE and DE environment for an aerospace program

#Define criteria
criteria = ["Functionality", "Scalability", "Reliability", "Security", "Ease of Integration"]

#Define alternatives
alternatives = ["APIs", "SOA", "ESB", "MOM"]

#Define decision matrix
decision_matrix = np.array([[3,4,4,4,3],
[4,3,4,3,4],
[3,3,3,3,4],
[2,2,2,2,2]])

#Normalize decision matrix
decision_matrix_normalized = np.round(decision_matrix / decision_matrix.max(axis=0), 3)

#Calculate weights for criteria
criteria_weights = np.round(np.sum(decision_matrix_normalized, axis=0) / len(alternatives), 3)

#Define weights for alternatives
alternative_weights = np.array([0.4, 0.3, 0.2, 0.1])

#Calculate weighted sum for each alternative
alternatives_weights = np.round(np.dot(decision_matrix_normalized, criteria_weights)*alternative_weights, 2)

#Print results
print("Criteria:", criteria)
print("Alternatives:", alternatives)
print("Decision matrix:")
print(decision_matrix)
print("Normalized decision matrix:")
print(decision_matrix_normalized)
print("Weights for criteria:", criteria_weights)
print("Weighted sum for alternatives:", alternatives_weights)

print("\nSummary:")
print("The most important criteria are:")
for i in range(len(criteria_weights)):
    print(f"{criteria[i]}: {criteria_weights[i]}")

#Table of normalized decision matrix
print("\nNormalized Decision Matrix:")
print("Criteria/Alternatives\tFunctionality\tScalability\tReliability\tSecurity\tEase of Integration")
for i in range(len(alternatives)):
    print(f"{alternatives[i]}\t{decision_matrix_normalized[i][0]}\t{decision_matrix_normalized[i][1]}\t{decision_matrix_normalized[i][2]}\t{decision_matrix_normalized[i][3]}\t{decision_matrix_normalized[i][4]}")

#Table of weighted sum for alternatives
print("\nThe weighted sum for each alternative is:")
print("Criteria/Alternatives\tWeighted Sum")
for i in range(len(alternatives)):
    print(f"{alternatives[i]}\t{alternatives_weights[i]}")