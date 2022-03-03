# Solpkg
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

### How to install ?
Just move the binary to ```bin```. And you are good to go.

It is pretty basic right now, but i am working on this.
