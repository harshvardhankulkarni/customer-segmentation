# Customer Segmentation (RFM Analysis) - Demo Project

Segment customers into meaningful groups using Recency, Frequency, and Monetary scoring. This analysis helps businesses target the right customers with the right strategies.

This is a demo project using synthetic data to demonstrate RFM analysis techniques.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Data manipulation and RFM scoring
- NumPy 1.24+ - Numerical operations
- Matplotlib 3.7+ - Visualization
- Seaborn 0.12+ - Statistical plotting

## Quick Start

### Prerequisites

- Python 3.8 or higher installed
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/customer-segmentation.git
cd customer-segmentation
pip install pandas numpy matplotlib seaborn
```

### Running

```bash
python 1_customer_segmentation.py
```

Expected output:

```
Saved: 1_customer_segments.png
--- CUSTOMER SEGMENTATION RESULTS ---
Total customers analyzed: 200
Champions: 17 customers (8.5%)
Loyal Customers: 77 customers (38.5%)
...
Exported: customer_segments_output.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| 1_customer_segments.png | 4-panel visualization chart |
| customer_segments_output.csv | Segmented customer data with RFM scores |

## How It Works

The script generates 200 synthetic customer profiles with purchase history. Each customer gets scored on three dimensions:

1. **Recency** - Days since last purchase. Lower is better. Scored 1-5.
2. **Frequency** - Total number of purchases. Higher is better. Scored 1-5.
3. **Monetary** - Total amount spent. Higher is better. Scored 1-5.

The combined RFM score (range 3-15) maps customers to one of five segments:

| Score Range | Segment | Strategy |
|-------------|---------|----------|
| 13-15 | Champions | Loyalty programs, exclusive access |
| 10-12 | Loyal Customers | Upsell, cross-sell, membership perks |
| 7-9 | Potential Loyalists | Engagement campaigns, recommendations |
| 5-6 | At Risk | Re-engagement, special discounts |
| 3-4 | Lost | Last-resort offers, clean from lists |

## Project Structure

```
customer-segmentation/
  1_customer_segmentation.py   Main analysis script
  README.md                    This file
  docs/
    architecture.md             Design and methodology
    runbook.md                  Operations guide
```

## Configuration

All parameters are at the top of the script for easy modification:

- `n_customers` - Number of customers to generate (default: 200)
- `np.random.seed(42)` - Set to any integer for reproducible results
- Segment score thresholds in `assign_segment()` function

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the script to verify output.
5. Submit a pull request.

## License

MIT
