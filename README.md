<!-- GSD -->

# Customer Segmentation (RFM Analysis)

Segment customers into actionable groups using Recency, Frequency, and Monetary scoring. Generates 200 synthetic customer profiles, assigns them to 5 segments (Champions, Loyal Customers, Potential Loyalists, At Risk, Lost), and outputs a static 4-panel visualization, an interactive Plotly HTML chart, and a CSV export.

This is a demo / portfolio project.

## Features

- Generates 200 synthetic customer profiles with realistic distributions (exponential recency, Poisson frequency, exponential monetary value)
- Quintile-based RFM scoring (1-5 per dimension, 3-15 total)
- 5 customer segments with business-actionable labels
- 4-panel static visualization (segment distribution, avg spend by segment, recency vs spend scatter, frequency histogram)
- Interactive Plotly HTML chart with hover details, zoom, and pan
- CSV export of all customer data with RFM scores and segment assignments
- Console output with key metrics and revenue breakdown

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Runtime |
| Pandas | Data manipulation and RFM scoring |
| NumPy | Random data generation and numerical ops |
| Matplotlib + Seaborn | Static visualization |
| Plotly | Interactive HTML chart |

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/customer-segmentation.git
cd customer-segmentation
pip install pandas numpy matplotlib seaborn plotly
```

### Run the Analysis

```bash
python 1_customer_segmentation.py
```

### Run the Interactive Version

```bash
python generate_interactive.py
```

### Expected Output

```
Saved: 1_customer_segments.png

--- CUSTOMER SEGMENTATION RESULTS ---
Total customers analyzed: 200

Segment breakdown:
  Champions: 17 customers (8.5%) - Avg spend: Rs.2074
  Loyal Customers: 77 customers (38.5%) - Avg spend: Rs.2145
  Potential Loyalists: 80 customers (40.0%) - Avg spend: Rs.1936
  At Risk: 18 customers (9.0%) - Avg spend: Rs.2530
  Lost: 8 customers (4.0%) - Avg spend: Rs.2313

Top revenue driver: Loyal Customers (Rs.165125)
Action: Target Loyal Customers with loyalty program to increase retention.

Exported: customer_segments_output.csv
Done.
Saved: 1_customer_segments_interactive.html
```

## Output Files

| File | Description |
|------|-------------|
| `1_customer_segments.png` | 4-panel static visualization (150 DPI) |
| `1_customer_segments_interactive.html` | Interactive Plotly chart with hover, zoom, pan |
| `customer_segments_output.csv` | 200 customer records with RFM scores and segment |

## GitHub Pages

Portfolio page: https://harshvardhankulkarni.github.io/customer-segmentation/

## Project Structure

```
customer-segmentation/
├── 1_customer_segmentation.py        Main analysis script
├── 1_customer_segmentation.ipynb     Jupyter notebook version
├── generate_interactive.py           Plotly interactive HTML generator
├── index.html                        GitHub Pages portfolio page
├── customer_segments_output.csv      Generated output data
├── 1_customer_segments.png           Static visualization output
├── 1_customer_segments_interactive.html  Interactive chart output
├── README.md
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```

## License

Demo project. No license specified.
