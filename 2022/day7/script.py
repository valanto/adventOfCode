import os


def build_filesystem():
  file_system = dict()
  file = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r")
  current_dir = ""
  ongoing_command = None
  for line in file:
    line = line.strip()
    if line.startswith("$"):
      line = line[1:].strip()
      if line.startswith("cd"):
        line = line[2:].strip()
        if line == "/":
          current_dir = ""
        elif line== "..":
          current_dir = "/".join(current_dir.split("/")[:-1])
        else:
          current_dir ="/".join([d for d in (current_dir.split("/") +[line]) if d != ""])
  

    elif line.startswith("dir"):
      line = line[3:].strip()
      if len(current_dir)>0:
        file_system["{0}/{1}".format(current_dir, line)] = dict(size=0, dir=True)
      else:
        file_system[line] = dict(size=0, dir=True)


    else:
      (size, file) = line.split(" ")
      size=int(size)
      file_system["{0}/{1}".format(current_dir, file)] = dict(size=size, dir=False)
      

  for folder in file_system.keys():
    if file_system[folder]["dir"]:
    
      for item in file_system.keys():
        if item.startswith(folder) and not file_system[item]["dir"]:
          file_system[folder]["size"]+= file_system[item]["size"]
          

  return file_system

def part2():
  disk_space = 70000000
  update_space = 30000000
  file_system = build_filesystem()
  
  used_space=0
  for item in file_system.keys():
    if not file_system[item]["dir"]:
      used_space += file_system[item]["size"]
  available_space = disk_space - used_space
  missing_space = update_space - available_space
  smallest_folder = None
  for item in file_system.keys():
    if file_system[item]["dir"] and file_system[item]["size"] >= missing_space and (smallest_folder is None or smallest_folder> file_system[item]["size"]):
      smallest_folder=file_system[item]["size"]


  return smallest_folder


def part1():
  file_system = build_filesystem()
  
  small_directories_size = 0
  for item in file_system.keys():
    if file_system[item]["dir"] and file_system[item]["size"] <= 100000:
      small_directories_size += file_system[item]["size"]


  return small_directories_size


print("part1: {0}".format(part1()))
print("part2: {0}".format(part2()))