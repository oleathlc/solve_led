import re


text = "turn on 0,0 through 999,999"


pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
command = re.findall(pattern, str(text))
for i in command:
        print(i)
print('Done')