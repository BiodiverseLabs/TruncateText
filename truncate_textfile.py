import pandas as pd
import os

def truncate_text_file(input_file, output_file, num_rows, num_columns):
    try:
        # Read the tab-delimited text file
        df = pd.read_csv(input_file, delimiter='\t', low_memory=False)
        
        # Truncate the DataFrame by the given number of rows and columns
        truncated_df = df.iloc[:num_rows, :num_columns]
        
        # Save the truncated DataFrame to a new tab-delimited text file
        truncated_df.to_csv(output_file, sep='\t', index=False)
        print(f"File successfully truncated and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Automatically find the first text file in the current folder
    current_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = None
    for file in os.listdir(current_folder):
        if file.endswith(".txt"):
            input_file = os.path.join(current_folder, file)
            break

    if input_file is None:
        print("No text file found in the current folder.")
    else:
        # Create output file path with "truncated_" prefix
        base_name = os.path.basename(input_file)
        output_file = os.path.join(current_folder, f"truncated_{base_name}")
        
        num_rows = int(input("Enter the number of rows to retain: "))
        num_columns = int(input("Enter the number of columns to retain: "))
        
        truncate_text_file(input_file, output_file, num_rows, num_columns)