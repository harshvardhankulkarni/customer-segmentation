<!-- GSD -->

# Testing

## Automated Tests

This project does not have automated tests. It is a demo / portfolio project — the analysis uses deterministic synthetic data (fixed random seed), so results are reproducible by design.

## Manual Validation Steps

After running `python 1_customer_segmentation.py`:

### 1. Verify Script Completes

Check the exit code is 0 (no errors). The last line should print `Done.`

### 2. Verify CSV Output Exists

```bash
# Check the output file exists with expected columns
Get-ChildItem customer_segments_output.csv
Get-Content customer_segments_output.csv | Select-Object -First 1
```

Expected columns: `customer_id,recency_days,frequency,monetary_value,tenure_days,R_score,F_score,M_score,RFM_total,segment`

### 3. Verify Row Count

```python
import pandas as pd
df = pd.read_csv('customer_segments_output.csv')
len(df)  # Should be 200
```

### 4. Verify Segment Counts

```python
df['segment'].value_counts()
```

Expected distribution (seed 42): 5 segments present, Champions 5-15%, Loyal Customers 30-45%, At Risk 5-15%, Lost 2-8%.

### 5. Verify Score Ranges

```python
# Each score column should be 1-5
df[['R_score', 'F_score', 'M_score']].describe()

# RFM_total should be 3-15
df['RFM_total'].min() >= 3
df['RFM_total'].max() <= 15
```

### 6. Verify Segmentation Logic

```python
# Champions should have RFM_total >= 13
assert all(df[df['segment'] == 'Champions']['RFM_total'] >= 13)

# Lost should have RFM_total <= 4
assert all(df[df['segment'] == 'Lost']['RFM_total'] <= 4)
```

### 7. Verify PNG Output

Open `1_customer_segments.png` — it should display a 2x2 grid of charts:
- Top-left: Bar chart of customer counts per segment
- Top-right: Bar chart of average spend per segment (INR)
- Bottom-left: Scatter plot of recency vs spend, colored by segment
- Bottom-right: Histogram of purchase frequency

### 8. Verify Interactive HTML Output

Open `1_customer_segments_interactive.html` in a browser. Hover over data points — tooltips should show customer ID, recency, and spend. Zoom and pan should work.

## Data Quality Checks

- **Negative values**: Recency, frequency, and monetary should all be positive (clipped at minimums of 1, 1, 100)
- **Duplicate customer IDs**: Each `customer_id` should be unique (C0001-C0200)
- **Null values**: No nulls should exist in any column (all generated, no missing data)
- **Segment balance**: No single segment should contain >50% or <2% of customers

## Validate Segmentation Logic

The segmentation logic maps RFM_total (3-15) to 5 labels:

| RFM Total | Expected Segment |
|-----------|-----------------|
| 13-15 | Champions |
| 10-12 | Loyal Customers |
| 7-9 | Potential Loyalists |
| 5-6 | At Risk |
| 3-4 | Lost |

To verify every row follows this mapping:

```python
def expected_segment(score):
    if score >= 13: return 'Champions'
    if score >= 10: return 'Loyal Customers'
    if score >= 7: return 'Potential Loyalists'
    if score >= 5: return 'At Risk'
    return 'Lost'

df['expected'] = df['RFM_total'].apply(expected_segment)
assert (df['segment'] == df['expected']).all()
print('All segments match expected mapping.')
```
