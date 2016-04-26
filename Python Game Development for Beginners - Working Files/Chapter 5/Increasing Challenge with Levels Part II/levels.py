def labelmaker(label, list):
  labels = [label]*len(list)
  return zip(labels, list)

def make_levels(n=10):
  # Make 10 levels.  Beware: magic numbers!
  titles = labelmaker("title",["Level %d" %(i + 1) for i in range(n)])
  boxturtle_minspeed = labelmaker("box_minspeed",[i + 3 for i in range(n)])
  boxturtle_maxspeed = labelmaker("box_maxspeed",[int(i*1.2) + 10 for i in range(n)])
  number_turtles = labelmaker("number_turtles",[i * 2 for i in range(1,n + 1)])
  
  data = zip(titles, boxturtle_minspeed, boxturtle_maxspeed, number_turtles)
  
  levels = {}
  for i, level in enumerate(data):
    levels[i] = dict(level)
  return levels