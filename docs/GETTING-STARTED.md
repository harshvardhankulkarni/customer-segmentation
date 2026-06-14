<!-- GSD -->

# Getting Started

## Prerequisites

- Python 3.8 or higher
- pip package manager

Verify your Python installation:

```bash
python --version
```

## Installation

```bash
# Clone the repository
git clone https://github.com/harshvardhankulkarni/customer-segmentation.git
cd customer-segmentation

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly
```

## First Run

Run the main analysis script:

```bash
python 1_customer_segmentation.py
```

You should see output similar to:

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
```

## Interactive Version

Generate the interactive Plotly HTML chart:

```bash
python generate_interactive.py
```

Output: `1_customer_segments_interactive.html` — open in any browser. Hover over data points for customer details. Zoom and pan for exploration.

## Jupyter Notebook

Open the notebook version for a step-by-step walkthrough:

```bash
jupyter notebook 1_customer_segmentation.ipynb
```

Each section is documented with markdown explanations.

## Expected Outputs

| File | When Created | How to View |
|------|-------------|-------------|
| `customer_segments_output.csv` | After running `1_customer_segmentation.py` | Open in any text editor or spreadsheet |
| `1_customer_segments.png` | After running `1_customer_segmentation.py` | Open in any image viewer |
| `1_customer_segments_interactive.html` | After running `generate_interactive.py` | Open in a web browser |

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError: No module named 'pandas'` | Dependencies not installed | `pip install pandas numpy matplotlib seaborn plotly` |
| `Python was not found` | Python not installed or not on PATH | Install Python 3.8+ from python.org, check PATH |
| File not saving | Write permission in current directory | Run from a writable directory |
| `ValueError: Bin edges must be unique` | Too few unique values for quintiles | Happens with very small datasets (<10 customers) |
| Plotly HTML is blank | Browser blocking local files | Open with a local server or use `--allow-file-access-from-files` flag |
