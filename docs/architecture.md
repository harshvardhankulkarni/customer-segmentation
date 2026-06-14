<!-- GSD -->

# Customer Segmentation (RFM Analysis) — Architecture

## Context and Goals

This project segments synthetic customer profiles using RFM (Recency, Frequency, Monetary) analysis. It is a portfolio demo demonstrating customer segmentation techniques with Python data analysis libraries.

## Data Flow

```
Synthetic Data Generation (200 profiles)
  → Recency: exponential distribution
  → Frequency: Poisson distribution  
  → Monetary: exponential distribution
  → Quintile-based RFM scoring (1-5 per dimension)
  → Composite score (3-15) mapped to 5 segments
  → 4-panel static matplotlib visualization
  → Interactive Plotly HTML chart
  → CSV export with segment labels
```

## Components

| File | Role |
|------|------|
| `1_customer_segmentation.py` | Main RFM analysis: data generation, scoring, segmentation, static chart, CSV export |
| `generate_interactive.py` | Generates interactive Plotly HTML version |
| `1_customer_segmentation.ipynb` | Jupyter notebook for exploratory development |
| `customer_segments_output.csv` | Generated output with 200 customer records |
| `1_customer_segments.png` | Static 4-panel visualization |
| `1_customer_segments_interactive.html` | Interactive Plotly chart |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| Quintile-based scoring | Simple, interpretable approach. Each dimension gets equal weight (1-5). |
| 200 synthetic customers | Sufficient for demonstrating segmentation patterns without overwhelming data volume |
| 5 segments | Matches common RFM convention (Champions, Loyal, Potential, At Risk, Lost) |
| Synthetic data | Focus on the analysis technique rather than data collection |
| Static + interactive charts | Static for reports, interactive for exploration |

## Trade-offs

- Synthetic data lacks real-world anomalies and unpredictable patterns
- Quintile scoring assumes equal weight for R, F, and M dimensions
- 5 segments may oversimplify complex customer bases
- No time-based cohort tracking (static snapshot, not longitudinal)

## File Organization

```
customer-segmentation/
├── 1_customer_segmentation.py
├── generate_interactive.py
├── 1_customer_segmentation.ipynb
├── 1_customer_segments.png
├── 1_customer_segments_interactive.html
├── customer_segments_output.csv
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
