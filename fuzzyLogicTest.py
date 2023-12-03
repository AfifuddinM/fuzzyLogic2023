import skfuzzy                      # Fuzzy Logic
import numpy as np                  # Numerical Python
import matplotlib.pyplot as plt     # Plotting Library
from skfuzzy import membership as mf 
# Generate universe variables
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)

# Generate fuzzy membership functions
qual_lo = skfuzzy.trimf(x_qual, [0, 0, 5])
qual_md = skfuzzy.trimf(x_qual, [0, 5, 10])
qual_hi = skfuzzy.trimf(x_qual, [5, 10, 10])
serv_lo = skfuzzy.trimf(x_serv, [0, 0, 5])
serv_md = skfuzzy.trimf(x_serv, [0, 5, 10])
serv_hi = skfuzzy.trimf(x_serv, [5, 10, 10])
tip_lo = skfuzzy.trimf(x_tip, [0, 0, 13])
tip_md = skfuzzy.trimf(x_tip, [0, 13, 25])
tip_hi = skfuzzy.trimf(x_tip, [13, 25, 25])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_qual, qual_lo, 'b', linewidth=1.5, label='Low')
ax0.plot(x_qual, qual_md, 'g', linewidth=1.5, label='Medium')
ax0.plot(x_qual, qual_hi, 'r', linewidth=1.5, label='High')

ax0.set_title('Food Quality')
ax0.legend()

ax1.plot(x_serv, serv_lo, 'b', linewidth=1.5, label='Low')
ax1.plot(x_serv, serv_md, 'g', linewidth=1.5, label='Medium')
ax1.plot(x_serv, serv_hi, 'r', linewidth=1.5, label='High')

ax1.set_title('Service Quality')
ax1.legend()

ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='High')

ax2.set_title('Tip Amount')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()