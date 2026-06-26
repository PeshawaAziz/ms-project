import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('data.xlsx')

print("Original Data:")
print(df)
print("\nColumn names:", df.columns.tolist())

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(df.iloc[:, 0], df['Alg.1'], 'o-', label='Alg.1')
axes[0].plot(df.iloc[:, 0], df['Alg.2'], 's-', label='Alg.2')
axes[0].plot(df.iloc[:, 0], df['Alg.3'], '^-', label='Alg.3')
axes[0].set_xlabel('Data Size')
axes[0].set_ylabel('Run Time')
axes[0].set_title('Linear Scale')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(df.iloc[:, 0], df['Alg.1'], 'o-', label='Alg.1')
axes[1].plot(df.iloc[:, 0], df['Alg.2'], 's-', label='Alg.2')
axes[1].plot(df.iloc[:, 0], df['Alg.3'], '^-', label='Alg.3')
axes[1].set_xlabel('Data Size')
axes[1].set_ylabel('Run Time (log scale)')
axes[1].set_yscale('log')
axes[1].set_title('Log Scale')
axes[1].legend()
axes[1].grid(True)

algorithms = ['Alg.1', 'Alg.2', 'Alg.3']
total_times = [df['Alg.1'].sum(), df['Alg.2'].sum(), df['Alg.3'].sum()]
axes[2].bar(algorithms, total_times, color=['blue', 'orange', 'green'])
axes[2].set_ylabel('Total Run Time')
axes[2].set_title('Total Run Time by Algorithm')
axes[2].grid(True, axis='y')

plt.tight_layout()
plt.show()

print("\nAnalysis Results:")
for alg in algorithms:
    print(f"{alg}: Total={df[alg].sum()}, Mean={df[alg].mean():.2f}, Min={df[alg].min()}, Max={df[alg].max()}")

new_row = pd.DataFrame({
    df.columns[0]: ['700KB'],
    'Alg.1': [80],
    'Alg.2': [320],
    'Alg.3': [700]
})

df_updated = pd.concat([df, new_row], ignore_index=True)
print("\n\nUpdated Data with 700KB:")
print(df_updated)

mask = df[df.columns[0]].isin(['100KB', '200KB', '300KB', '400KB', '500KB', '600KB'])
alg2_avg = df.loc[mask, 'Alg.2'].mean()

print(f"\n\nPart C: Average run time for Alg.2 (100KB-600KB): {alg2_avg:.2f}")
print(f"Column values for Alg.2: {df.loc[mask, 'Alg.2'].tolist()}")
