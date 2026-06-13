"""
Customer Segmentation Analysis
Uses RFM (Recency, Frequency, Monetary) analysis to segment customers.
Generates its own data. No external files needed.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic customer data
np.random.seed(42)
n_customers = 200

customer_ids = [f'C{i:04d}' for i in range(1, n_customers + 1)]

data = {
    'customer_id': customer_ids,
    'recency_days': np.random.exponential(30, n_customers).astype(int),
    'frequency': np.random.poisson(5, n_customers),
    'monetary_value': np.random.exponential(2000, n_customers).round(2),
    'tenure_days': np.random.randint(30, 730, n_customers),
}

df = pd.DataFrame(data)
df['recency_days'] = df['recency_days'].clip(1, 180)
df['frequency'] = df['frequency'].clip(1, 30)
df['monetary_value'] = df['monetary_value'].clip(100, 20000)

# Calculate RFM scores
def rfm_score(series, reverse=False):
    quintiles = pd.qcut(series, 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    if reverse:
        return quintiles.astype(int)
    return (6 - quintiles.astype(int))

df['R_score'] = rfm_score(df['recency_days'], reverse=True)
df['F_score'] = rfm_score(df['frequency'])
df['M_score'] = rfm_score(df['monetary_value'])
df['RFM_total'] = df['R_score'] + df['F_score'] + df['M_score']

# Assign segments
def assign_segment(score):
    if score >= 13:
        return 'Champions'
    elif score >= 10:
        return 'Loyal Customers'
    elif score >= 7:
        return 'Potential Loyalists'
    elif score >= 5:
        return 'At Risk'
    else:
        return 'Lost'

df['segment'] = df['RFM_total'].apply(assign_segment)

# Visualization 1: Segment distribution
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

segment_counts = df['segment'].value_counts()
colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c', '#95a5a6']
axes[0, 0].bar(segment_counts.index, segment_counts.values, color=colors[:len(segment_counts)])
axes[0, 0].set_title('Customer Segments')
axes[0, 0].set_ylabel('Number of Customers')
for i, v in enumerate(segment_counts.values):
    axes[0, 0].text(i, v + 1, str(v), ha='center')

# Visualization 2: Monetary value by segment
segment_money = df.groupby('segment')['monetary_value'].mean().sort_values(ascending=False)
axes[0, 1].bar(segment_money.index, segment_money.values, color=colors[:len(segment_money)])
axes[0, 1].set_title('Average Spend by Segment (INR)')
axes[0, 1].set_ylabel('Average Total Spend')
for i, v in enumerate(segment_money.values):
    axes[0, 1].text(i, v + 50, f'Rs.{v:.0f}', ha='center')

# Visualization 3: Recency vs Monetary scatter
for i, seg in enumerate(df['segment'].unique()):
    seg_data = df[df['segment'] == seg]
    axes[1, 0].scatter(seg_data['recency_days'], seg_data['monetary_value'],
                      label=seg, alpha=0.6, s=seg_data['frequency']*10)
axes[1, 0].set_xlabel('Recency (days since last purchase)')
axes[1, 0].set_ylabel('Total Spend (INR)')
axes[1, 0].set_title('Recency vs Spend by Segment')
axes[1, 0].legend()

# Visualization 4: Frequency distribution
axes[1, 1].hist(df['frequency'], bins=20, color='#3498db', edgecolor='white')
axes[1, 1].set_xlabel('Number of Purchases')
axes[1, 1].set_ylabel('Number of Customers')
axes[1, 1].set_title('Purchase Frequency Distribution')

plt.tight_layout()
plt.savefig('1_customer_segments.png', dpi=150, bbox_inches='tight')
print('Saved: 1_customer_segments.png')

# Key insights
print('\n--- CUSTOMER SEGMENTATION RESULTS ---')
print(f'Total customers analyzed: {len(df)}')
print(f'\nSegment breakdown:')
for seg in ['Champions', 'Loyal Customers', 'Potential Loyalists', 'At Risk', 'Lost']:
    if seg in segment_counts.index:
        pct = (segment_counts[seg] / len(df)) * 100
        avg_spend = df[df['segment'] == seg]['monetary_value'].mean()
        print(f'  {seg}: {segment_counts[seg]} customers ({pct:.1f}%) - Avg spend: Rs.{avg_spend:.0f}')

revenue_share = df.groupby('segment')['monetary_value'].sum()
top_segment = revenue_share.idxmax()
print(f'\nTop revenue driver: {top_segment} (Rs.{revenue_share[top_segment]:.0f})')
print(f'Action: Target {top_segment} with loyalty program to increase retention.')

df.to_csv('customer_segments_output.csv', index=False)
print('\nExported: customer_segments_output.csv')
print('Done.')
