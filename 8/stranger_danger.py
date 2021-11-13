import json, math
with open("souls.json") as file:
  data = json.load(file)
  min = 2147483647
  for i, n in enumerate(data):
    for n_2 in data[i+1:]:
      if abs(n + n_2) < min:
        min = abs(n + n_2)
        lmao = n
        yeet = n_2
  print(str(min), str(lmao), str(yeet))
