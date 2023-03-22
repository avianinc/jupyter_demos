# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:00:11 2023

AHP Analysis of ESB, API, SOA and MOM technologies:
to support the implementation of an MBSE and DE environment.

Steps to perform this analysis
1. Define the criteria and alternatives for the decision-making problem.
2. Create a decision matrix with the criteria as rows and the alternatives as columns. Populate the matrix with scores that reflect the relative importance of each criterion for each alternative.
3. Populate the matrix with scores that reflect the relative importance of each criterion for each alternative.
4. Define the weights for each alternative, reflecting the importance of each alternative to the decision.
5. Multiply the decision matrix by the alternative weights to obtain a weighted decision matrix.
6. Calculate the weighted score for each criterion by summing the weighted scores across all alternatives for that criterion.
7. Normalize the criteria weights by dividing each weighted score by the sum of all weighted scores.
8. Multiply the decision matrix by the normalized criteria weights to obtain a criteria-weighted matrix.
9. Calculate the weighted score for each alternative by summing the scores across all criteria for that alternative.
10. Present the results 

# Saaty, T.L. (1980), The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation. McGraw-Hill, New York.

@author: John DeHart (jdehart@avian.com)
"""

# Import libraries 
import numpy as np 
from tabulate import tabulate
from PIL import Image, ImageDraw

# Define the criteria 
criteria = ["Functionality", "Scalability", "Reliability", "Security", "Ease of Integration"] 

# Define the alternatives 
alternatives = ["APIs", "SOA", "ESB", "MOM"] 

# Define the decision matrix 
decision_matrix = np.array([[3,4,4,4,3],
                            [4,3,4,3,4],
                            [3,3,3,3,4],
                            [2,2,2,2,2]]) 

# Define the weights for the alternatives
alternative_weights = np.array([0.4, 0.3, 0.2, 0.1])

# Multiply the decision matrix by the alternative weights
weighted_matrix = np.round(decision_matrix * alternative_weights.reshape(-1, 1), 2)

# Calculate the weighted score for each criterion
criteria_weighted_scores = np.sum(weighted_matrix, axis=0)

# Normalize the criteria weights
criteria_normalized_weights = np.round(criteria_weighted_scores / np.sum(criteria_weighted_scores), 2)

# Multiply the decision matrix by the criteria weights
criteria_weighted_matrix = np.round(decision_matrix * criteria_normalized_weights, 2)

# Calculate the weighted score for each alternative
alternative_weighted_scores = np.sum(criteria_weighted_matrix, axis=1)

# this was a pia :)

output_table = "\n".join([
    "Alternative weights: (Input by users)",
    tabulate([alternative_weights], headers=alternatives, floatfmt=".1f"),
    "Decision matrix (criteria importance): (Input by users)",
    tabulate(decision_matrix, headers=criteria, showindex=alternatives),
    "Criteria weights:",
    tabulate([criteria_normalized_weights], headers=criteria, floatfmt=".2f"),
    "Normalized decision matrix (weighted by alternatives):",
    tabulate(weighted_matrix, headers=criteria, showindex=alternatives, floatfmt=".2f"),
    "Criteria weighted matrix (weighted by criteria importance):",
    tabulate(criteria_weighted_matrix, headers=criteria, showindex=alternatives, floatfmt=".2f"),
    "Alternative scores (weighted by criteria):",
    tabulate([[score] for score in alternative_weighted_scores], headers=["Weighted Score"], showindex=alternatives, floatfmt=".2f")
])

print(output_table)

img = Image.new('RGB', (600, 600), color = 'white')

d = ImageDraw.Draw(img)
d.text((10,10), output_table, fill=(0,0,0))

img.save('soa_ahp_analysis.png')