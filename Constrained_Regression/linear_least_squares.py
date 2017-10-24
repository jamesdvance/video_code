# Creating A Constrained 'Regression' 

from scipy.optimize import lsq_linear
import pandas as pd
import numpy as np

# Read in data
df = pd.read_csv()

# Convert independent variables to a matric
A = df_trial[['Var1','Var2']].as_matrix()
# Add an array of ones to act as bias coefficient
ones = np.ones(A.shape[0])
# Combine array of ones and indepedent variables
A = np.concatenate(( ones[:,np.newaxis],A),axis=1)
# Create matrix for target variable
b = df_trial['Target_Variable'].as_matrix()

# Make sure all over the above are set as float variables

# Set_ bounds
fixed_lb = 
var1_lb = 
var2_lb =
fixed_ub = 
var1_ub = 
var2_ub = 
# Put bounds into arrays
lb = np.array([fixed_lb,var1_lb,var2_lb])
ub = np.array([fixed_ub, var1_ub,var2_ub])

# Run optimization
results = lsq_linear(A,b,bounds=(lb,ub),lsmr_tol='auto')

# Extract coefficients
fixed_coef = results['x'][0]
var1_coef = results['x'][1]
var2_coef = results['x'][2]

# Write Coefficients to Data Frame
coef_df = pd.DataFrame({'Fixed Coefficient':fixed_coef, 'Variable 1 Coef':var1_coef, 'Variable 2 Coef': var2_coef})

# Write DataFrame to CSV
ceof_df.to_csv("lsq_results.csv")