import os

# Define the paths
input_file_path = r"data\\allowed_words.txt"
output_file_path = r"Wordle\\src\\frontend\\wordle-frontend\\src\\components\words.js"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# Read the words from the text file
with open(input_file_path, 'r') as file:
    words = file.read().splitlines()

# Format the words into a JavaScript array
js_data = f"const data = {words};\nexport default data;"

# Write the JavaScript array to the output file
with open(output_file_path, 'w') as file:
    file.write(js_data)

print(f"JavaScript file created successfully at {output_file_path}")
