import json
from collections import defaultdict

from selenium import webdriver

dictionary = defaultdict(list)
c=0

while c<10:
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/Software_metric"
    driver.get(url)
    script ="return window.performance.getEntries();"
    result = driver.execute_script(script)
    driver.close()
    
    for i in result:
        dictionary[i['name']].append(i['duration'])

    c=c+1


for key,value in dictionary.items():
    dictionary[key] = sum(value) / float(len(value))
    
for key,value in dictionary.items():
    print(key,value)

with open ("Average_Result_For_SW2.json", "w") as file:
    jason = json.dumps(dictionary, indent=8)
    file.write(jason)
    