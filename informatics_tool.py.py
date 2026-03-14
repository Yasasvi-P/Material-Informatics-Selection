import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA INGESTION
df = pd.read_csv('material_data.csv')

# 2. FEATURE ENGINEERING
df['Performance_Index'] = (df['Yield_Strength_MPa'] / df['Elongation_pct']).round(2)

# 3. STATISTICAL CORRELATION (The New "Selection-Worthy" Part)
# We select only numeric columns to find how they relate to each other
numeric_df = df[['Yield_Strength_MPa', 'Tensile_Strength_MPa', 'Elongation_pct', 'Hardness_HB', 'Performance_Index']]
correlation_matrix = numeric_df.corr()

# 4. DUAL-PANEL VISUALIZATION
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Panel A: The Pareto Frontier (Scatter Plot)
sns.scatterplot(data=df, x='Elongation_pct', y='Yield_Strength_MPa', 
                hue='Material_ID', size='Hardness_HB', sizes=(50, 400), ax=ax1)
ax1.set_title('Strength-Ductility Pareto Frontier')

# Panel B: The Correlation Heatmap (EDA Tool Feature)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax2)
ax2.set_title('Property Correlation Matrix (Pearson)')

# 5. EXPORT
plt.tight_layout()
plt.savefig('advanced_informatics_report.png')
plt.show()

print("Enhanced Report generated: correlation patterns identified.")