"""
Constants of COVID-19 diasease and wealth distribution a ver ahora
"""

import numpy as np

"""
Probability of each infection serverity by age

Source: Imperial College Covid-19 research team


"""

age_hospitalization_probs = [0.001, 0.003, 0.012, 0.032, 0.049, 0.102, 0.166, 0.243, 0.273]
age_severe_probs = [0.05, 0.05, 0.05, 0.05, 0.063, 0.122, 0.274, 0.432, 0.709]
#age_death_probs = [0.002, 0.00006, 0.0003, 0.0008, 0.0015, 0.006, 0.022, 0.051, 0.093]
age_death_probs = [0.0034, .0004, 0.00023, 0.0092, 0.0260, 0.0596, 0.1378, 0.2420, 0.3220]


## Citar fontes

"""
Wealth distribution - Lorenz Curve

By quintile, source: https://www.worldbank.org/en/topic/poverty/lac-equity-lab1/income-inequality/composition-by-quintile

La curva de Lorenz ya tiene los datos de México pero faltan las series de arriba
"""

lorenz_curve = [.05, .09, .14, .21, .51]
share = np.min(lorenz_curve)
basic_income = np.array(lorenz_curve) / share
