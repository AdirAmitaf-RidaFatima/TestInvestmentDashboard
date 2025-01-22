import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Specify the file path
file_path = r"tabula-PeriodicTradeSummaryReport.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
st.write("### Data Preview")
st.write(df.head())  # Streamlit will display the first few rows of the data

# Print the column names to verify (optional for debugging)
print(df.columns)

# Assuming the column with profit and loss is named 'Amount' (update according to your CSV file)
# Replace 'Security Name' and 'Amount' with the actual column names from your CSV
x_col = 'Security Name'  # Update this
y_col = 'Amount'  # Update this

# Create the Seaborn lineplot
st.write("### Profit and Loss by Each Company")

# Set the style for the plot
sns.set(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=x_col, y=y_col, marker="o")

# Add plot labels and title
plt.title('Profit and Loss by Each Company', fontsize=16)
plt.xlabel(x_col, fontsize=12)
plt.ylabel(y_col, fontsize=12)

# Display the plot in Streamlit
st.pyplot(plt)
