
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

np.random.seed(42)
n = 200
df = pd.DataFrame({
    'customer_id': [f'C{i:04d}' for i in range(1, n+1)],
    'recency_days': np.random.exponential(30, n).astype(int),
    'frequency': np.random.poisson(5, n),
    'monetary_value': np.random.exponential(2000, n).round(2),
})
df['recency_days'] = df['recency_days'].clip(1, 180)
df['frequency'] = df['frequency'].clip(1, 30)
df['monetary_value'] = df['monetary_value'].clip(100, 20000)

def rfm_score(s, rev=False):
    q = pd.qcut(s, 5, labels=[1,2,3,4,5], duplicates='drop').astype(int)
    return 6 - q if not rev else q

df['R'] = rfm_score(df['recency_days'], rev=True)
df['F'] = rfm_score(df['frequency'])
df['M'] = rfm_score(df['monetary_value'])
df['RFM'] = df['R'] + df['F'] + df['M']

def seg(s):
    if s >= 13: return 'Champions'
    if s >= 10: return 'Loyal Customers'
    if s >= 7: return 'Potential Loyalists'
    if s >= 5: return 'At Risk'
    return 'Lost'

df['segment'] = df['RFM'].apply(seg)

color_map = {'Champions': '#2ecc71', 'Loyal Customers': '#3498db',
             'Potential Loyalists': '#f39c12', 'At Risk': '#e74c3c', 'Lost': '#95a5a6'}

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Customer Segments', 'Avg Spend by Segment',
                    'Recency vs Spend by Segment', 'Frequency Distribution'),
    specs=[[{'type': 'bar'}, {'type': 'bar'}],
           [{'type': 'scatter'}, {'type': 'histogram'}]]
)

seg_counts = df['segment'].value_counts()
for i, (s, c) in enumerate(seg_counts.items()):
    fig.add_trace(go.Bar(x=[s], y=[c], name=s, marker_color=color_map[s],
                         text=c, textposition='outside'), row=1, col=1)

seg_money = df.groupby('segment')['monetary_value'].mean().sort_values(ascending=False)
fig.add_trace(go.Bar(x=seg_money.index, y=seg_money.values,
                     marker_color=[color_map[s] for s in seg_money.index],
                     text=[f'Rs.{v:.0f}' for v in seg_money.values],
                     textposition='outside', showlegend=False), row=1, col=2)

for seg_name in df['segment'].unique():
    sd = df[df['segment'] == seg_name]
    fig.add_trace(go.Scatter(x=sd['recency_days'], y=sd['monetary_value'],
                             mode='markers', name=seg_name,
                             marker=dict(size=sd['frequency']*1.5, color=color_map[seg_name], opacity=0.6),
                             text=[f'{c}: Rs.{m:.0f}, {f} purchases' for c, m, f in zip(sd['customer_id'], sd['monetary_value'], sd['frequency'])],
                             hovertemplate='%{text}<br>Recency: %{x}d<br>Spend: Rs.%{y:.0f}<extra></extra>'),
                row=2, col=1)

fig.add_trace(go.Histogram(x=df['frequency'], nbinsx=20,
                           marker_color='#3498db', showlegend=False), row=2, col=2)

fig.update_layout(height=700, title_text='Customer Segmentation (RFM) - Interactive', hovermode='closest')
fig.write_html('1_customer_segments_interactive.html')
print('Saved: 1_customer_segments_interactive.html')
