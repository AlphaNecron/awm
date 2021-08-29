from requests.models import HTTPError
from beautifultable import BeautifulTable
import math, sys, requests, htmllistparse, os.path, time, re

def conv(byte):
  if byte == 0:
      return "0B"
  suff = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
  i = int(math.floor(math.log(byte, 1024)))
  p = math.pow(1024, i)
  s = round(byte / p, 2)
  return "%s %s" % (s, suff[i])

def find(pkg, ver):
  url = "https://archive.archlinux.org/packages/" + pkg[0] + "/" + pkg
  table = BeautifulTable()
  try:
    _, lst = htmllistparse.fetch_listing(url, timeout=30)
    if not ver == "":
      pattern = r"^{}-{}-(x86_64|i386|any).pkg.tar.(zst|xz|gz)$".format(pkg, ver)
      files = list(filter(lambda x: re.match(pattern, x), map(lambda y: y.name, lst)))
      if len(files) == 0:
        print("Couldn't find package", pkg, "with version", ver)
        return
      for file in files:
        print("Found", file)
        download(url + "/" + file, file)
      return
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
    target = filtered[index - 1].name
    download(url + "/" + target, target)
  except HTTPError as err:
    print(err)

def download(url, name):
  try:
    print("Downloading", name)
    r = requests.get(url)
    with open(name, 'wb') as f:
      f.write(r.content)
      print("Downloaded", name, "to current working dir.")
  except PermissionError:
    print("No permission to download.")
  except HTTPError as hterr:
    print("HTTP error", hterr)

if __name__ == "__main__":
  if len(sys.argv) == 2:
    pkg = sys.argv[1].split('@')
    if len(pkg) == 2:
      find(pkg[0], pkg[1])
    else:
      find(pkg[0], "")
  else:
    print("Usage:", os.path.basename(__file__) or "wayback_machine.py", "package[@version]")
