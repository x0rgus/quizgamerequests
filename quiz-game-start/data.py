import requests, json
question_data = []
URL = "https://opentdb.com/api.php?amount=12&type=boolean"
r = requests.get(URL)
parsed = json.loads(r.text)
for question in parsed["results"]:
    question_data.append(question)
print(question_data)