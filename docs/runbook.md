# Runbook: Customer Segmentation Analysis

## When to Use This Runbook

- Running the segmentation analysis for the first time.
- Re-running with new data.
- Troubleshooting failed executions.

## Prerequisites

- Python 3.8 or higher installed.
- pip package manager available.
- Internet access (only for initial package install).

## Procedure

### Step 1: Verify Python Installation

```bash
python --version
```

Expected output: `Python 3.8.x` or higher.

### Step 2: Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3: Run the Analysis

```bash
cd path/to/customer-segmentation
python 1_customer_segmentation.py
```

### Step 4: Verify Output

Check for these files in the project directory:

- `1_customer_segments.png` - Should open as a 4-panel chart.
- `customer_segments_output.csv` - Should contain 200 rows with columns: customer_id, recency_days, frequency, monetary_value, R_score, F_score, M_score, RFM_total, segment.

### Step 5: Interpret Results

Review the console output. Key numbers to check:

- Total customers (should match input count).
- Segment distribution (Champions should be 5-15% of total).
- Average spend per segment (should decrease from Champions to Lost).

## Rollback

If the script produces unexpected results:

1. Check the random seed: `np.random.seed(42)` in the script.
2. Revert to the last known good commit:
   ```bash
   git checkout HEAD~1
   ```
3. Delete output files before re-running:
   ```bash
   rm 1_customer_segments.png customer_segments_output.csv
   ```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Module not found | Missing dependencies | Run `pip install pandas numpy matplotlib seaborn` |
| Permission denied on save | Write access to directory | Run from a writable directory or use full path |
| ZeroDivisionError | Empty dataset | Increase n_customers above 10 |
| Wrong segment counts | Changed score thresholds | Reset `assign_segment` to original values |
| PNG file corrupted | Disk space or interruption | Delete file and re-run |

## Escalation

If the issue is not resolved by the troubleshooting steps:

1. Check the GitHub Issues page for known problems.
2. Open a new issue with:
   - Full error message and stack trace.
   - Python version (`python --version`).
   - Operating system.
   - Script modifications (if any).

## Maintenance

- **Weekly**: Re-run with fresh data to keep segments current.
- **Monthly**: Review segment definitions against business feedback.
- **Quarterly**: Evaluate whether 5 segments is still optimal.
