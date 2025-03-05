import pandas as pd
import os

def main():
    csv_file = "students.csv"
    
    # Check if the CSV file exists
    if os.path.exists(csv_file):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        print("CSV file read successfully!")
    else:
        print("File not found. Creating sample data...")
        # Create sample data if file doesn't exist
        data = {
            "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "Age": [21, 22, 20, 23, 21],
            "Grade": ["A", "B", "A", "C", "B"]
        }
        df = pd.DataFrame(data)
        # Write the sample data to a CSV file
        df.to_csv(csv_file, index=False)
        print("Sample CSV file created as 'students.csv'.")

    # Display the DataFrame
    print("\nData:")
    print(df)

    # Perform simple analysis:
    avg_age = df["Age"].mean()
    grade_counts = df["Grade"].value_counts()

    print("\nAverage Age:", avg_age)
    print("\nGrade Counts:")
    print(grade_counts)

    # Prepare analysis summary DataFrame
    analysis_data = {
        "Metric": ["Average Age"],
        "Value": [avg_age]
    }
    analysis_df = pd.DataFrame(analysis_data)
    # Save analysis results to a new CSV file
    analysis_df.to_csv("analysis.csv", index=False)
    print("\nAnalysis saved to 'analysis.csv'.")

if __name__ == "__main__":
    main()
