import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# Load the data
df = pd.read_csv('data.csv')
# Create a function to identify potential compromises
def identify_compromises(df):
    # Create a list of Indicators of Compromise (IoCs)
    iocs = ['unusual network traffic', 'unauthorized access attempts', 'changes to system files']
    # Create a list of potential compromises
    potential_compromises = []
    # Iterate over the IoCs
    for ioc in iocs:
        # Check if the IoC is present in the data
        if ioc in df['ioc'].values:
            # Add the IoC to the list of potential compromises
            potential_compromises.append(ioc)
    # Return the list of potential compromises
    return potential_compromises
# Identify potential compromises
potential_compromises = identify_compromises(df)
# Print the list of potential compromises
print(potential_compromises)