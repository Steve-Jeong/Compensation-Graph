import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe (same as before)
data = {
    'Section': [1, 2, 3, 4, 5, 6, 7],
    'Min. Allowable Settlement (cm)': [11, 11, 6, 6, 6, 0, 0],
    'Max. Allowable Settlement (cm)': [31, 31, 26, 26, 26, 20, 20],
    'Min. Settlement (cm)': [-0.9, 3.3, -1.5, 2.5, 2.8, -6.0, -1.3],
    'Max. Settlement (cm)': [5.7, 14.6, 7.8, 13.4, 12.8, 0.7, 3.1],
    'Calc. Settlement (cm)': [4.3, 6.9, 2.7, 2.7, 2.3, 2.7, 2.9]
}

df = pd.DataFrame(data)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Set the width of each bar
bar_width = 0.35

# Plot allowable settlement range
ax.bar(df['Section'], df['Max. Allowable Settlement (cm)'] - df['Min. Allowable Settlement (cm)'], 
  bottom=df['Min. Allowable Settlement (cm)'], width=bar_width, 
  label='Allowable Settlement Range', color='lightblue', edgecolor='blue', alpha=0.7)

# Plot actual settlement range
ax.bar(df['Section'], df['Max. Settlement (cm)'] - df['Min. Settlement (cm)'], 
  bottom=df['Min. Settlement (cm)'], width=bar_width, 
  label='Actual Settlement Range', color='lightgreen', edgecolor='green', alpha=0.7)

# Plot calculated settlement as bars
ax.bar(df['Section'], [0.5] * len(df), bottom=df['Calc. Settlement (cm)'] - 0.25, 
  width=bar_width, color='red', label='Calculated Settlement')

# Customize the plot
ax.set_xlabel('Section', fontsize=12)
ax.set_ylabel('Settlement (cm)', fontsize=12)
ax.set_title('Settlement Ranges and Calculated Values by Section', fontsize=16)  # Increase title size
ax.set_xticks(df['Section'])
ax.set_xticklabels(df['Section'])
ax.legend()

# Set y-axis major ticks to 5 cm intervals
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
# Set y-axis minor ticks to 1 cm intervals
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)
ax.grid(which='minor', linestyle=':', alpha=0.5)  # Add minor grid lines

# Add margins to top and bottom
y_min, y_max = ax.get_ylim()
margin = (y_max - y_min) * 0.1  # 10% margin
ax.set_ylim(y_min - margin, y_max + margin)

# Show the plot
plt.tight_layout()
plt.show()

print("Graph with updated minor tick intervals generated successfully.")