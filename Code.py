import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Results.csv')

value_list1 = ["gap type 1"]
boolean_series1 = df.gap_type.isin(value_list1)
filtered_df1 = df[boolean_series1]

value_list2 = ["gap type 2"]
boolean_series2 = df.gap_type.isin(value_list2)
filtered_df2 = df[boolean_series2]

value_list3 = ["gap type 3"]
boolean_series3 = df.gap_type.isin(value_list3)
filtered_df3 = df[boolean_series3]

value_list4 = ["gap type 4"]
boolean_series4 = df.gap_type.isin(value_list4)
filtered_df4 = df[boolean_series4]

value_list5 = ["gap type 5"]
boolean_series5 = df.gap_type.isin(value_list5)
filtered_df5 = df[boolean_series5]

# print(filtered_df1)

# df1 = df.sort_values('Mean squared error', ascending=False)

fig = plt.figure(figsize=(15, 15))

ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# Ax1 for gap type 1
ax1.bar(filtered_df1['method'], filtered_df1['Mean squared error'])
ax1.set_xticklabels(filtered_df1['method'], rotation=60, horizontalalignment='right', fontsize='12')

ax1.set_title('MSE Gap type 1', fontsize=20)
ax1.set_ylabel('MSE')

# Ax1 for gap type 2
ax2.bar(filtered_df2['method'], filtered_df2['Mean squared error'])
ax2.set_xticklabels(filtered_df2['method'], rotation=45, horizontalalignment='right', fontsize='10')

ax2.set_title('MSE Gap type 2', fontsize=20)
ax2.set_ylabel('MSE')

# Ax1 for gap type 3
ax3.bar(filtered_df3['method'], filtered_df3['Mean squared error'])
ax3.set_xticklabels(filtered_df3['method'], rotation=60, horizontalalignment='right', fontsize='12')

ax3.set_title('MSE Gap type 3', fontsize=20)
ax3.set_ylabel('MSE')

# Ax1 for gap type 4
ax4.bar(filtered_df4['method'], filtered_df4['Mean squared error'])
ax4.set_xticklabels(filtered_df4['method'], rotation=60, horizontalalignment='right', fontsize='12')

ax4.set_title('MSE Gap type 4', fontsize=20)
ax4.set_ylabel('MSE')

# Ax1 for gap type 5
ax5.bar(filtered_df5['method'], filtered_df5['Mean squared error'])
ax5.set_xticklabels(filtered_df5['method'], rotation=60, horizontalalignment='right', fontsize='12')

ax5.set_title('MSE Gap type 5', fontsize=20)
ax5.set_ylabel('MSE')

plt.show()

