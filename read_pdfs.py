import os

file_names = []
folder_path = "/path/to/folder/containing/pdfs"  # Adjust accordingly

for filename in os.listdir(folder_path):
  if os.path.isfile(os.path.join(folder_path, filename)):
        file_names.append(filename)
