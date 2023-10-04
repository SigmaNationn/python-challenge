# Importing Libraries
import pandas as pd

# Reading Data
df = pd.read_csv('Resources/budget_data.csv')

# Calculating total number of months
months_total = len(df)

# Calculating the net profit/loss for the entire period
total_profit_loss = df['Profit/Losses'].sum()

# Calculating profit/loss changes and storing them in a new column, after that calculating average of the changes.
df['Profit/Losses Change'] = df['Profit/Losses'].diff()
average = df['Profit/Losses Change'].mean()

# Calculating the greatest increase in profits, and greatest decrease in profits over time
increase_profit = df[df['Profit/Losses Change'] == df['Profit/Losses Change'].max()]
decrease_profit = df[df['Profit/Losses Change'] == df['Profit/Losses Change'].min()]

# Printing All the results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${total_profit_loss:.0f}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {increase_profit['Date'].values[0]}, {increase_profit['Profit/Losses Change'].values[0]}")
print(f"Greatest Decrease in Profits: {decrease_profit['Date'].values[0]}, {decrease_profit['Profit/Losses Change'].values[0]} ")

