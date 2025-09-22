"""
Customer Support Ticket Analyzer

Analyzes support ticket data from `sample_tickets.csv`.

Functions: 
1. get_summary() overall ticket stats 
2. analyze_categories() breakdown by category 
3. analyze_agents() breakdown by agent
"""

import pandas as pd
from pathlib import Path

DATA_FILE = Path("sample_tickets.csv")


def load_data() -> pd.DataFrame:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"{DATA_FILE} not found. Please place sample_tickets.csv in the project root.")
    return pd.read_csv(DATA_FILE)


def get_summary() -> dict[str, float | int]:
    df = load_data()
    return {
        "total_tickets": int(len(df)),
        "avg_resolution": float(df["resolution_hours"].mean()),
        "avg_satisfaction": float(df["satisfaction"].mean()),
    }


def analyze_categories() -> pd.DataFrame:
    df = load_data()
    return (
        df.groupby("category")
        .agg(
            tickets=("ticket_id", "count"),
            avg_resolution=("resolution_hours", "mean"),
            avg_satisfaction=("satisfaction", "mean"),
        )
        .reset_index()
    )


def analyze_agents() -> pd.DataFrame:
    df = load_data()
    return (
        df.groupby("agent")
        .agg(
            tickets=("ticket_id", "count"),
            avg_resolution=("resolution_hours", "mean"),
            avg_satisfaction=("satisfaction", "mean"),
        )
        .reset_index()
    )


if __name__ == "__main__":
    try:
        summary = get_summary()
        print(f"Total Tickets: {summary['total_tickets']}")
        print(f"Average Resolution: {summary['avg_resolution']:.1f} hours")
        print(f"Average Satisfaction: {summary['avg_satisfaction']:.1f}/5\n")

        print("Categories:")
        for _, row in analyze_categories().iterrows():
            print(
                f"{row['category']}: {row['tickets']} tickets, "
                f"{row['avg_resolution']:.1f}h avg, "
                f"{row['avg_satisfaction']:.1f}/5"
            )

        print("\nAgents:")
        for _, row in analyze_agents().iterrows():
            print(
                f"{row['agent']}: {row['tickets']} tickets, "
                f"{row['avg_resolution']:.1f}h avg, "
                f"{row['avg_satisfaction']:.1f}/5"
            )
    except (FileNotFoundError, KeyError) as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure 'sample_tickets.csv' exists and has the correct columns.")
