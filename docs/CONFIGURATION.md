<!-- GSD -->

# Configuration

## Configuration Files

This project has no configuration files, environment variables, or `.env` files. All configuration is inline in the Python scripts.

## Configurable Parameters

All tunable parameters are at the top of `1_customer_segmentation.py`:

### Data Generation

| Parameter | File | Line | Default | Description |
|-----------|------|------|---------|-------------|
| `np.random.seed(42)` | `1_customer_segmentation.py` | 14 | `42` | Random seed for reproducible data |
| `n_customers` | `1_customer_segmentation.py` | 15 | `200` | Number of customer profiles to generate |

### Data Distributions (`1_customer_segmentation.py`, lines 21-24)

| Field | Distribution | Parameters | Clipped To |
|-------|-------------|------------|------------|
| `recency_days` | `np.random.exponential` | scale=30 | [1, 180] |
| `frequency` | `np.random.poisson` | lambda=5 | [1, 30] |
| `monetary_value` | `np.random.exponential` | scale=2000 | [100, 20000] |
| `tenure_days` | `np.random.randint` | low=30, high=730 | None |

### Segment Thresholds (`1_customer_segmentation.py`, lines 45-56)

The `assign_segment()` function defines score-to-segment mapping. Change the thresholds to customize segmentation.

### Visualization

| Parameter | File | Line | Default | Description |
|-----------|------|------|---------|-------------|
| `figsize` | `1_customer_segmentation.py` | 60 | `(14, 10)` | Chart dimensions in inches |
| `dpi` | `1_customer_segmentation.py` | 95 | `150` | PNG output resolution |
| `colors` | `1_customer_segmentation.py` | 63 | 5 hex colors | Segment color palette |
| `nbinsx` | `generate_interactive.py` | 69 | `20` | Histogram bin count |

### Output Filenames

| Current Name | File | Line |
|-------------|------|------|
| `1_customer_segments.png` | `1_customer_segmentation.py` | 95 |
| `customer_segments_output.csv` | `1_customer_segmentation.py` | 113 |
| `1_customer_segments_interactive.html` | `generate_interactive.py` | 73 |

Change the string in the `savefig()` / `to_csv()` / `write_html()` call to rename outputs.

## Interactive Version Parameters

In `generate_interactive.py`, the same generation and scoring parameters exist with minor differences:

- `n` (line 9) instead of `n_customers` — number of customers
- No `tenure_days` field (only used in the main script, not in interactive)
- Marker size multiplier: `sd['frequency']*1.5` (line 64) vs `sd['frequency']*10` in static
- Chart height: `700` (line 72)

## No Environment Variables

This project does not use any environment variables. No `.env` file is needed.
