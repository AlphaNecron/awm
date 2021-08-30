# arch_wayback_machine
Download historical Arch Linux packages with one command.

## Dependencies
```
pip install beautifultable htmllistparse
```

## Usage
```
wget https://raw.githubusercontent.com/AlphaNecron/arch_wayback_machine/master/wayback_machine.py
python wayback_machine.py package[@version]
                     ^^^     ^^^
                  required  optional
eg: python wayback_machine.py neofetch@7.1.0-2
```

## Demo
[![asciicast](https://asciinema.org/a/432870.svg)](https://asciinema.org/a/432870)
