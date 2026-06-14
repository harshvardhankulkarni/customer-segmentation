<!-- GSD -->

# Development Guide

## Project Structure Overview

This is a single-script Python analysis project with a companion interactive generator. There is no package structure, no build system, and no configuration files.

```
customer-segmentation/
├── 1_customer_segmentation.py     # Main entry point
├── generate_interactive.py        # Interactive chart generator
├── 1_customer_segmentation.ipynb  # Notebook (mirrors main script)
├── index.html                     # GitHub Pages portfolio
└── docs/                          # Project documentation
```

## How to Modify the Analysis

### Change the Number of Customers

In `1_customer_segmentation.py`, line 15:

```python
n_customers = 200  # Change this value
```

### Change the Random Seed

In `1_customer_segmentation.py`, line 14:

```python
np.random.seed(42)  # Change for different random data
```

### Change Segment Thresholds

In `1_customer_segmentation.py`, lines 45-56 (the `assign_segment` function):

```python
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
```

Adjust the score thresholds to change segment boundaries. The score range is 3-15.

### Add a New Segment

1. Add a new score range to `assign_segment()`
2. Add the segment name to the print loop at line 102
3. Optionally add a color for the new segment in the `colors` list at line 63

### Add a New RFM Dimension

1. Generate the new metric in the data dictionary
2. Create a scoring column using `rfm_score()`
3. Add it to `RFM_total`
4. Add a new subplot visualization

### Modify Data Distributions

In `1_customer_segmentation.py`, lines 21-24, change the NumPy distribution parameters:

```python
'recency_days': np.random.exponential(30, n_customers).astype(int),
'frequency': np.random.poisson(5, n_customers),
'monetary_value': np.random.exponential(2000, n_customers).round(2),
'tenure_days': np.random.randint(30, 730, n_customers),
```

Clip ranges at lines 28-30 ensure realistic bounds.

### Use Real Data Instead of Synthetic

Replace lines 13-30 with:

```python
df = pd.read_csv('your_customer_data.csv')
```

Ensure your CSV has columns for recency (days), frequency (count), and monetary value (currency).

## How to Add a New Visualization

The main script uses a 2x2 subplot grid (line 60):

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
```

To add a new chart:

1. **Replace an existing panel** — Use one of the four `axes[row, col]` slots
2. **Expand to more panels** — Change the subplot grid, e.g., `plt.subplots(3, 2, ...)` for 6 panels
3. **In `generate_interactive.py`** — Use `make_subplots()` rows/cols and add traces with `row`/`col` parameters

For the interactive version, mirror changes in `generate_interactive.py` to keep both outputs consistent.

## Code Style Guidelines

- Use descriptive variable names (`segment_counts`, not `sc`)
- Keep functions short and single-purpose
- Use f-strings for string formatting
- Use NumPy random seed for reproducibility
- Color palette: use the existing 5-color scheme (`#2ecc71`, `#3498db`, `#f39c12`, `#e74c3c`, `#95a5a6`)
- Inline comments for non-obvious logic (e.g., recency reverse scoring)
- No class structures needed — module-level functions are sufficient

## Commit Conventions

Use conventional commit prefixes:

| Prefix | Use Case |
|--------|----------|
| `feat:` | New feature or visualization |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code restructure without behavior change |
| `chore:` | Build, config, or dependency updates |

Example:

```
feat: add customer lifetime value dimension
fix: correct recency scoring inversion logic
docs: update architecture diagram
```
