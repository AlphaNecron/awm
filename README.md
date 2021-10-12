# awm
Download historical Arch Linux packages with one command.

## Dependencies
```
pip install beautifultable htmllistparse
```

## Installation
```bash
git clone https://github.com/AlphaNecron/awm
cd awm
# or
mkdir awm
cd awm
curl https://raw.githubusercontent.com/AlphaNecron/awm/master/PKGBUILD
# and then
makepkg -sri
```

## Manual installation
```bash
curl -o awm https://raw.githubusercontent.com/AlphaNecron/awm/master/wayback_machine.py
sudo mv awm /usr/bin/awm
sudo chmod +x /usr/bin/awm
```

## Usage
```
awm package[@version]
      ^^^     ^^^
   required  optional
eg: awm neofetch@7.1.0-2
```

## Demo
[![asciicast](https://asciinema.org/a/432870.svg)](https://asciinema.org/a/432870)
