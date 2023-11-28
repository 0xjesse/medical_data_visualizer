import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
# Import data
df = pd.read_csv('medical_examination.csv')

# Calculate BMI
df['BMI'] = df['weight'] / (df['height'] / 100)**2
# Add 'overweight' column
df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# Normalize 'cholesterol' and 'gluc'
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   value_vars=[
                       'active', 'alco', 'cholesterol', 'gluc', 'overweight',
                       'smoke'
                   ])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  # df_cat = None taken out with line above
  g = sns.catplot(
      x='variable',
      hue='value',
      col='cardio',
      kind='count',
      data=df_cat,
      order=['active', 'alco', 'cholesterol', 'gluc', 'overweight',
             'smoke'])  # Adjust order here
  g.set_axis_labels("variable", "total")  # Set y-axis label to 'total'
  # Draw the catplot with 'sns.catplot()'

  g.set_axis_labels("Health Metrics", "Total Count")
  g.set_titles("Cardiovascular Disease: {col_name}")
  g.fig.suptitle('Distribution of Health Metrics by Cardiovascular Disease Status', y=1.05)

  for t, l in zip(g._legend.texts, ['Normal', 'Elevated']): 
    t.set_text(l)

  g._legend.set_title('Health Metric Status')
  g._legend.set_bbox_to_anchor((1.15, 0.5))

      # Modify the titles for each subplot for clarity
  g.set_titles(col_template="Cardiovascular Disease: {col_name}")
  for ax, title in zip(g.axes.flat, ['No', 'Yes']):
      ax.set_title(f"Cardiovascular Disease: {title}")

  # Get the figure for the output
  # Save the plot and return the figure
  fig = g.fig
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi'])
               & (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.drop(columns='BMI').corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(12, 12))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax)

  ax.set_title('Correlation Heatmap of Health Metrics')


  # Save the plot and return the figure
  fig.savefig('heatmap.png')
  return fig
