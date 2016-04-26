def labelmaker(label, list):
  labels = [label]*len(list)
  return zip(labels, list)

def make_levels(n=10):
  # Make 10 levels.  Beware: magic numbers!
  titles = labelmaker("title",["Level %d" %(i + 1) for i in range(n)])
 
  # Zip together your lists of data here
  data = zip(titles)
  
  levels = {}
  for i, level in enumerate(data):
    levels[i] = dict(level)
  return levels