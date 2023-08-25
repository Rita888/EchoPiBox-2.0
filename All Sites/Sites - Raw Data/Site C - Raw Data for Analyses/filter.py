import os

# Folder path where the compiled CSV file is located
folder_path = "/Users/rita/Thesis/Survey/Data From Sites/Analysis/Site C - Windsor/"

# Input compiled CSV file name
input_filename = "output_combined.csv"  # Replace with the actual file name

# Output filtered CSV file name
output_filename = "output_filtered.csv"

# Full paths to input and output files
input_file_path = os.path.join(folder_path, input_filename)
output_file_path = os.path.join(folder_path, output_filename)

# List to store filtered lines
filtered_lines = []

# Read the input CSV file and filter lines based on the condition
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        parts = line.strip().split(',')
        if len(parts) >= 2 and float(parts[1]) >= 0.6:  # Assuming accuracy is the second value
            filtered_lines.append(line)

# Write filtered lines to the output CSV file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(filtered_lines)

print("Filtered lines have been saved to", output_file_path)
