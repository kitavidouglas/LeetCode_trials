# src/main.py
"""
Daily Dev Micro-Analytics
- Reads data/daily_metrics.csv
- Produces a line chart and a short summary in outputs/summary.md
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "daily_metrics.csv"
OUT_FIG = Path(__file__).resolve().parents[1] / "outputs" / "figures" / "daily_trends.png"
OUT_SUM = Path(__file__).resolve().parents[1] / "outputs" / "summary.md"

OUT_FIG.parent.mkdir(parents=True, exist_ok=True)
OUT_SUM.parent.mkdir(parents=True, exist_ok=True)

# Load
df = pd.read_csv(DATA, parse_dates=["date"]).sort_values("date")

# Simple derived metrics
df["coding_7d_ma"] = df["coding_minutes"].rolling(7, min_periods=1).mean()
df["tasks_7d_ma"] = df["tasks_done"].rolling(7, min_periods=1).mean()

# Plot
plt.figure(figsize=(9, 5))
plt.plot(df["date"], df["coding_minutes"], label="Coding minutes (daily)", marker="o")
plt.plot(df["date"], df["coding_7d_ma"], label="7-day MA - coding", linestyle="--")
plt.plot(df["date"], df["tasks_7d_ma"], label="7-day MA - tasks", linestyle=":")
plt.xlabel("Date")
plt.ylabel("Minutes / Tasks")
plt.title("Daily Dev Metrics")
plt.legend()
plt.tight_layout()
plt.savefig(OUT_FIG, dpi=150)
plt.close()

# Summary: last row insight
last = df.iloc[-1]
insight = (
    f"# Daily summary for {last['date'].date()}\n\n"
    f"- Coding minutes: {int(last['coding_minutes'])}\n"
    f"- Tasks done: {int(last['tasks_done'])}\n"
    f"- Focus score: {last['focus_score']}\n\n"
    f"## Short insight\n\n"
    f"The 7-day coding average is {last['coding_7d_ma']:.1f} minutes/day; tasks 7-day avg = {last['tasks_7d_ma']:.1f}.\n"
)

OUT_SUM.write_text(insight)
print("Report generated:", OUT_FIG, OUT_SUM)
