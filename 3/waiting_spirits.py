import json

with open("waitingSpirits.json") as file:
  data = json.load(file)
  res = []
  for i, height in enumerate(data):
    sight = 0
    for later_height in data[i+1:]:
      if height > later_height:
        sight+=1
      else:
        sight+=1
        break
    res.append(sight)

  print(res)
      
    
