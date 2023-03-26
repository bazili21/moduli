import json
import pickle
with open('jsongroup','r', encoding='utf-8') as f:
    result = json.load(f)
print(result)
print(type(result))

with open('j.pikle', 'rb') as f:
    result = pickle.load(f)
print(result)
print(type(result))