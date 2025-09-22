# Customer Support Ticket Analyzer

This repository contains a simple Python script (`analyzer.py`) to analyze customer support ticket data from `tickets.csv`.

## Features
The script provides three types of analysis:
1. **Summary Statistics**
   - Total number of tickets
   - Average resolution time (in hours)
   - Average satisfaction score
2. **Category Analysis**
   - Tickets grouped by category (e.g., Technical, Billing, Account)
   - Average resolution time per category
   - Average satisfaction score per category
3. **Agent Performance**
   - Tickets handled per agent
   - Average resolution time per agent
   - Average satisfaction score per agent

## Requirements
- Python 3.8+
- [pandas](https://pandas.pydata.org/)

Install dependencies with:
```bash
pip install pandas
````

## Usage

Place your `tickets.csv` file in the project root (same directory as `analyzer.py`).
The CSV file must have the following columns:

```
ticket_id, category, priority, resolution_hours, satisfaction, agent
```

Run the script:

```bash
python analyzer.py
```

## Example Output

```
Total Tickets: 95
Average Resolution: 12.5 hours
Average Satisfaction: 3.8/5

Categories:
Technical: 32 tickets, 18.2h avg, 3.4/5
Billing: 25 tickets, 7.1h avg, 4.2/5
Account: 38 tickets, 11.8h avg, 3.9/5

Agents:
Alice: 28 tickets, 14.1h avg, 4.0/5
Bob: 35 tickets, 11.8h avg, 3.7/5
Carol: 32 tickets, 12.0h avg, 3.8/5
```

## Notes

* Ensure the CSV file is correctly formatted.
* Any missing or incorrect columns will raise an error.
