from requests.models import HTTPError
from beautifultable import BeautifulTable
import math, sys, requests, htmllistparse, os.path, time

def conv(byte):
  if byte == 0:
      return "0B"
  suff = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
  i = int(math.floor(math.log(byte, 1024)))
  p = math.pow(1024, i)
  s = round(byte / p, 2)
  return "%s %s" % (s, suff[i])

def download(pkg):
  url = "https://archive.archlinux.org/packages/" + pkg[0] + "/" + pkg
  table = BeautifulTable()
  try:
    _, lst = htmllistparse.fetch_listing(url, timeout=30)
    filtered = list(filter(lambda q: not q.name.endswith(".sig"), lst))
    limit = 0
    for file in filtered:
      limit += 1
      table.rows.append([limit, file.name, time.strftime("%d/%m/%Y %H:%M:%S", file.modified), conv(file.size)])
    table.columns.header = ["index", "file", "last modified", "size"]
    print(table)
    index = 0
    while index == 0:
      temp = input("Select an index > ").strip()
      if not temp.isdigit():
        print("Invalid input.")
      elif int(temp) > limit or int(temp) <= 0:
        print("Index must not exceed the limit or below zero.")
      else:
        index = int(temp)
    target = filtered[index - 1]
    print("Downloading", target.name)
    r = requests.get(url + "/" + target.name)
    with open(target.name, 'wb') as f:
      f.write(r.content)
      print("Downloaded", target.name, "to current working dir.")
  except HTTPError as err:
    print(err)

if __name__ == "__main__":
  if len(sys.argv) == 2:
    download(sys.argv[1])
  else:
    print("Usage:", os.path.basename(__file__) or "wayback_machine.py", "package_name")
