import requests
import pandas as pd
import math

df = pd.DataFrame()
df['Title'] = file_names

src_ids = []

for index, row in df.iterrows():
  title = row['Title']

  files = [
      ('file', ('file', open("/path/to/folder/containing/pdfs" + title, 'rb'), 'application/octet-stream'))  # Adjust accordingly
  ]
  headers = {
      'x-api-key': 'sec_xxxxxxxxxx' # Adjust accordingly
  }

  response = requests.post(
      'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

  if response.status_code == 200:
      src = response.json()
      srcId = src['sourceId']
      src_ids.append(srcId)
  else:
      print('Status:', response.status_code)
      print('Error:', response.text)
      print('Title:', title)
      src_ids.append(math.nan)

new_column_name = 'SourceID'
new_column_data = src_ids
df[new_column_name] = new_column_data
