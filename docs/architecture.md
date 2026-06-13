# Architecture: Customer Segmentation

## Context

Businesses need to understand their customer base to allocate marketing spend effectively. Treating all customers the same wastes money. RFM analysis provides a data-driven way to segment customers based on actual purchase behavior.

## Goals

- Segment customers into actionable groups.
- Identify high-value customers for retention.
- Flag at-risk customers for re-engagement.
- Produce a visual report and a structured data export.

## Design

### Data Flow

```
Synthetic Data Generator
        |
        v
Raw Customer Profiles (200 records)
        |
        v
RFM Score Calculator
  - Recency: days since last purchase (inverted)
  - Frequency: total purchase count
  - Monetary: total spend
        |
        v
Segment Assignment (5 groups by score thresholds)
        |
        +---> Visualization (4-panel chart)
        +---> CSV Export (segmented data)
        +---> Console Output (key metrics)
```

### Scoring Logic

Each dimension uses quintile-based scoring:

```python
def rfm_score(series, reverse=False):
    quintiles = pd.qcut(series, 5, labels=[1,2,3,4,5], duplicates='drop')
    if reverse:
        return quintiles.astype(int)
    return (6 - quintiles.astype(int))
```

- Recency uses reverse scoring (lower days = higher score).
- Frequency and Monetary use standard scoring (higher = higher score).

### Segment Mapping

```
RFM Total 3-4   -> Lost
RFM Total 5-6   -> At Risk
RFM Total 7-9   -> Potential Loyalists
RFM Total 10-12 -> Loyal Customers
RFM Total 13-15 -> Champions
```

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Synthetic data instead of real data | Self-contained. No external dependencies. Reproducible. |
| Quintile-based scoring | Standard RFM practice. Handles skewed distributions well. |
| 5 segments | Matches industry convention. Actionable without being too granular. |
| PNG output | Universal format. Easy to share, embed, or present. |

## Trade-offs

- **Simplicity vs accuracy**: Quintile scoring is simple but may not capture nonlinear relationships. More sophisticated methods (k-means, hierarchical clustering) could find better segments but require more tuning.
- **Synthetic data**: The insights are illustrative, not actionable for real businesses. Real data would require privacy handling and data quality checks.
- **Static analysis**: This is a one-time batch process. A production system would need incremental updates as new orders come in.

## Integration Points

- **Input**: None (self-generates data). To use real data, replace the generation block with a CSV import using `pd.read_csv()`.
- **Output**: `customer_segments_output.csv` can feed into CRM systems, email marketing tools, or BI dashboards.
- **Extending**: Add more features (customer lifetime value, churn probability) by adding new scoring dimensions.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib, seaborn

No external APIs, databases, or network access required.
