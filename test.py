import pandas as pd
import matplotlib.pyplot as plt
# Create the dataframe
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
  label='Allowable Settlement Range', color='lightblue', edgecolor='blue')
# Plot actual settlement range
ax.bar(df['Section'] + bar_width, df['Max. Settlement (cm)'] - df['Min. Settlement (cm)'], 
  bottom=df['Min. Settlement (cm)'], width=bar_width, 
  label='Actual Settlement Range', color='lightgreen', edgecolor='green')
# Plot calculated settlement as points
ax.scatter(df['Section'] + bar_width/2, df['Calc. Settlement (cm)'], 
  color='red', s=50, label='Calculated Settlement')
# Customize the plot
ax.set_xlabel('Section')
ax.set_ylabel('Settlement (cm)')
ax.set_title('Settlement Ranges and Calculated Values by Section')
ax.set_xticks(df['Section'] + bar_width / 2)
ax.set_xticklabels(df['Section'])
ax.legend()
# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)
# Show the plot
plt.tight_layout()
plt.show()
print("Graph generated successfully.")