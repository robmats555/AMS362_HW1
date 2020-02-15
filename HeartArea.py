import numpy as np


def upper(x):
    output = np.sqrt(2-(x*x)) + np.sqrt(abs(x)) - np.sqrt(np.sqrt(2))
    if np.isnan(output):
        return 0
    else:
        return output


def lower(x):
    output = np.sqrt(2-(x*x)) - np.sqrt(abs(x)) + np.sqrt(np.sqrt(2))
    if np.isnan(output):
        return 0
    else:
        return output


# I was forced to start the upper area off outside of the
# for loop. If I didn't, due to truncation error, inserting
# sqrt(2) into the function would put a negative number
# under the square root, causing the whole method to blow up.
t = np.arange(-1 * np.sqrt(2), np.sqrt(2), 0.0001)
upper_area = upper(t[1]) / 2 * 0.0001
lower_area = lower(t[1]) / 2 * 0.0001

for i, val in enumerate(t):
    if i < len(t)-1:
        upper_area += 0.0001 * ((upper(t[i]) + upper(t[i+1]))/2)
        lower_area += 0.0001 * ((lower(t[i]) + lower(t[i+1]))/2)
    else:
        break

# This value was calculated in CircleArea.py
circle_area = 3.3506
print(upper_area+lower_area-circle_area)
