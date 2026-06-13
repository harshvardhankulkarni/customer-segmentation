# Customer Segmentation (RFM Analysis) - Demo Project

Segment customers into meaningful groups using Recency, Frequency, and Monetary scoring. This analysis helps businesses target the right customers with the right strategies.

This is a demo project using synthetic data to demonstrate RFM analysis techniques.

## Problem

Most businesses treat all customers the same. They send the same emails, the same offers, and the same messaging to everyone. This wastes money and misses opportunities. High-value customers get ignored. At-risk customers get no attention.

## Approach

Used RFM (Recency, Frequency, Monetary) analysis on synthetic customer data:

- **Recency**: Days since customer last purchased. Lower is better.
- **Frequency**: Total number of purchases. Higher is better.
- **Monetary**: Total amount spent. Higher is better.

Each customer got a score of 1-5 for each dimension. The combined RFM score (3-15) maps to a segment.

## Segments

| Segment | Description | Strategy |
|---------|-------------|----------|
| Champions | Highest RFM scores. Buy often and recently. | Loyalty programs. Exclusive access. Referral incentives. |
| Loyal Customers | Regular buyers with good scores. | Upsell and cross-sell. Membership perks. |
| Potential Loyalists | Recent buyers with average frequency. | Engagement campaigns. Product recommendations. |
| At Risk | Used to buy often but have not purchased recently. | Re-engagement emails. Special discounts. Win-back campaigns. |
| Lost | Long time since last purchase. Low frequency and spend. | Last-resort offers. Clean from active lists. |

## Results

- 200 customers analyzed across 5 segments.
- Champions (8.5% of customers) drive 28% of revenue.
- At Risk customers (9%) still have high average spend. Worth reactivating.
- A loyalty program targeting Champions and Loyal Customers yields the highest ROI.

## How to Run

```bash
pip install pandas matplotlib seaborn numpy
python 1_customer_segmentation.py
```

Output: `1_customer_segments.png` (chart) and `customer_segments_output.csv` (segmented data).

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn

## License

MIT
