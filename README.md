# arch_wayback_machine
Download historical Arch Linux packages with one command.

## Dependencies
```
pip install beautifultable htmllistparse
```

## Installation
```bash
curl -o awm https://raw.githubusercontent.com/AlphaNecron/arch_wayback_machine/master/wayback_machine.py
sudo mv awm /usr/bin/awm
chmod +x /usr/bin/awm
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
