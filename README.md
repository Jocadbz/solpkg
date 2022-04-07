# Solpkg

[![Based License](https://custom-icon-badges.herokuapp.com/badge/BASED_LICENSE-696969?logo=gigachad&style=for-the-badge)](https://github.com/thatonecalculator/BASED-LICENSE)

An wrapper for eopkg package manager

### What this does?

It is basically an wrapper for eopkg package manager. it makes syntax more simple.

### Functions

#### Installing packages
```bash
solpkg [i or install] <package> # -> same as "eopkg it"
```
#### Updating the system
```bash
solpkg [u or upgrade] # -> same as "eopkg up"
```

#### Printing package info
```bash
solpkg info <package> # -> same as "eopkg info"
```

#### Removing orphan packages
```bash
solpkg [c or clean] # -> same as "eopkg clean && eopkg rmo"
```

#### Removing packages
```bash
solpkg [r or remove] <package> # -> same as "eopkg rm"
```

#### Searching packages
```bash
solpkg [s or search] <package> # -> same as "eopkg sr"
```

#### Version of solpkg and EOPKG
```bash
solpkg [info] # -> same as "eopkg --version"
```

### How to install ?
Just move the binary to ```/usr/bin/```. And you are good to go.
