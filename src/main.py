#! /usr/bin/env python3
import subprocess
import sys

# Constants
helpMessage = """
Solpkg: A wrapper for eopkg
Options:
  install -> Install the desired package
  upgrade -> Do a complete upgrade
  remove  -> remove the desired program
  clean   -> clean the system and remove orphaned packages
  search  -> Search for a package
  info    -> Display info of a package
  version -> Shows the version of Solpkg
  cp      -> Configure pending packages
  list-installed (li) - Prints the list with all installed packages
  list-pending (lp) - List the pending packages
  list-repo (lr) - List the repos
  list-sources (ls) - List of the available sources
  list-upgrades (lu) - List all packages that need to be updated
               """


def INSTALL():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f"sudo eopkg install {new}", shell=True)


def VERSION():
    print("Solpkg version: 1.2.0")
    subprocess.call("eopkg --version", shell=True)


def UPGRADE():
    subprocess.call("sudo eopkg up", shell=True)


def REMOVE():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f"sudo eopkg rm {new}", shell=True)


def CLEAN():
    subprocess.call('sudo eopkg clean && sudo eopkg rmo', shell=True)


def SEARCH():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f'sudo eopkg sr {new}', shell=True)


def INFO():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f'sudo eopkg info {new}', shell=True)


def pending():
    subprocess.call("sudo eopkg cp", shell=True)


def list_installed():
    subprocess.call("sudo eopkg li", shell=True)


# It is not working now. Gonna just leave this as an option.
def list_newest():
    subprocess.call("sudo eopkg list-newest", shell=True)


def list_pending():
    subprocess.call("sudo eopkg list-pending", shell=True)


def list_repo():
    subprocess.call("sudo eopkg list-repo", shell=True)


def list_sources():
    subprocess.call("sudo eopkg list-sources", shell=True)


def list_upgrades():
    subprocess.call("sudo eopkg list-upgrades", shell=True)


abbreviationsDict = {"i": INSTALL, "u": UPGRADE, "r": REMOVE, "c": CLEAN,
                     "s": SEARCH, "vs": VERSION,
                     "cp": pending, "li": list_installed, "lp": list_pending,
                     "lr": list_repo, "ls": list_sources, "lu": list_upgrades}


def DO_WORK():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('Wrong usage. Run with --help flag to see current commands.')
    else:
        for arguments in args:
            if arguments == '--help':
                print(helpMessage)
                break
            else:
                try:
                    if arguments in abbreviationsDict.keys():
                        # get your function based on key in abbreviationsDict
                        required_function = abbreviationsDict[arguments]
                        required_function()  # Execute this function.
                        break
# Since the user input a command that can't be used as the name of a function.
                    elif arguments.startswith("list-"):
                        abbreviation = f"l{arguments[5]}"
                        # Same logic of the first If.
                        required_function = abbreviationsDict[abbreviation]
                        required_function()
                        break
                    else:
                        # install = INSTALL + () = INSTALL() and eval it.
                        eval(f"{arguments.upper()}()")
                        break
# (NameError) will be thrown in case you use a command which is not present.
                except NameError:
                    print('Unrecognized argument.')
                    print("Try running with --help flag to see current commands")
                    break


if __name__ == '__main__':
    DO_WORK()

