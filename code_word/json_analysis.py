import json
from pprint import pprint

with open('flash_LaaG.json', 'r') as f:
    data = json.load(f)

# with open('analysis.txt', 'w') as f:
#     f.write(str(data))
# pprint(data['flash']['commands'][1]['restrict'][1] + str(' ') + data['flash']['commands'][0]['args'])
print(data['flash']['commands'][1]['restrict'][1] + ' ' + data['flash']['commands'][0]['args'])
