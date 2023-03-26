import json
import pickle

My_favorite_tracks = {'name': 'Linkinparc', 'Tracks': ['The end', 'live'],
                      'artist':'мумиитроль', 'песни': [{'name': 'полковник', 'год': 2000}, {'NAME': 'olala', 'anul': 2002}]}


print(My_favorite_tracks)
j_group = json.dumps(My_favorite_tracks)
print(j_group)
P_group = pickle.dumps(My_favorite_tracks)
print(P_group)

with open('jsongroup', 'w', encoding='utf-8') as f:
    json.dump(My_favorite_tracks, f)

with open('j.pikle', 'wb') as f:
    pickle.dump(My_favorite_tracks, f)

