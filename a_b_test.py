# -*- coding: utf-8 -*-
"""A/B Test"""

import pandas as pd
import numpy as np
import seaborn as sns

# Data loading and configuration
df = pd.read_csv('/content/cookie_cats.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Data inspection
df.info()
df.shape
df.describe().T

# Outlier suppression
Up_limit = (51 - 5) * 3 + 51
df.loc[df['sum_gamerounds'] > Up_limit, 'sum_gamerounds'] = Up_limit

# Missing value check
df.isnull().sum()

# Creating new columns
df.loc[df['retention_1'] == True, 'Numretention_1'] = 1
df.loc[df['retention_1'] == False, 'Numretention_1'] = 0
df.loc[df['retention_7'] == True, 'Numretention_7'] = 1
df.loc[df['retention_7'] == False, 'Numretention_7'] = 1

# Z-Test
proportions_ztest(count, nobs):
 

# Shapiro-Wilk Test (Normality Test)
shapiro(x):


# Mann-Whitney U Test
mannwhitneyu(x, y):


# Exporting results
export_results_to_excel(data, filename):
    """
    Exports the given data to an Excel file.
    """
    data.to_excel(filename, index=False)