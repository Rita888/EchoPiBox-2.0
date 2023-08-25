import os

# Function to read the content of a file and return it as a list of lines
def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Folder path where CSV files are located
folder_path = "/Users/rita/Thesis/Survey/Data From Sites/Analysis/Site A - Cotswold/"

# List all files in the folder
filenames = os.listdir(folder_path)

# Filter only CSV files
csv_filenames = [filename for filename in filenames if filename.endswith('.csv')]

# List to store the content lines of each file
file_contents = []

# List to store the names of files that were appended
appended_files = []

for file_name in csv_filenames:  # Iterate only through CSV files
    file_path = os.path.join(folder_path, file_name)
    lines = read_file_lines(file_path)
    if lines:
        appended_files.append(file_name)
        file_contents.extend(lines[1:])  # Skip the first line (header) and append the rest

# Merge the content lines
merged_content = ''.join(file_contents)

# Write the merged content to a new file
output_file = os.path.join(folder_path, 'output_combined.csv')
with open(output_file, 'w') as output:
    output.write(merged_content)

print("Content from the following files has been combined and written to", output_file)
for file_name in appended_files:
    print(file_name)
