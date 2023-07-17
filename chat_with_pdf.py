import requests

headers = {
    'x-api-key': 'sec_xxxxxxxxxx',  # Adjust accordingly
    "Content-Type": "application/json",
}

questions = ["question 1", "question 2",	"question 3"] # Adjust accordingly

for index, row in df.iterrows():
  for question in questions:
    data = {
        'sourceId': row['SourceID'],
        'messages': [
            {
                'role': "user",
                'content': "Any mention of " + question + "? Only yes or no answer.", # Adjust accordingly
            }
        ]
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        res = result['content']
        df.loc[df['Title'] == row['Title'], question] = res
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
