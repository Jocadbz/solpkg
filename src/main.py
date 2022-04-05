# import shit WHOAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# import Break
from asyncio import subprocess
import os
import sys
import subprocess


def INSTALL():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f"sudo eopkg install {new}", shell=True)


def VERSION():
    print("Solpkg version: 1.4.0")
    subprocess.call("eopkg --version", shell=True)


def UPGRADE():
   os.system('sudo eopkg up')


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


def PENDINGS():
   subprocess.call(f"sudo eopkg cp", shell=True)


def DO_WORK():
   """ Function to handle command line usage"""
   args = sys.argv
   args = args[1:]  # First element of args is the file name

   if len(args) == 0:
      print('Wrong usage. Run with --help flag to see current commands.')
   else:
      for a in args:
         if a == '--help':
            print('Solpkg: An wrapper for eopkg')
            print('Options:')
            print(' install -> Install the desired package')
            print(' upgrade -> Do an complete upgrade')
            print(' remove  -> remove the desired program')
            print(' clean   -> clean the system and remove orphaned packages')
            print(' search  -> Search for an package')
            print(' info    -> Display info of an package')
            print(' version -> Shows the version of Solpkg')
            print(' cp      -> Configure pending packages  ')
         elif a == 'install' or a == 'i':
            INSTALL()
            break
         elif a == 'upgrade' or a == 'u':
            UPGRADE()
            break
         elif a == 'remove' or a == 'r':
            REMOVE()
            break
         elif a == "clean" or a == "c":
            CLEAN()
            break
         elif a == 'search' or a == 's':
            SEARCH()
            break
         elif a == 'info':
            INFO()
            break
         elif a == 'version' or a == 'vs':
             VERSION()
             break
         elif a == 'cp':
            PENDINGS()
         else:
            print('Unrecognised argument.')
            print('Try running with --help flag to see current commands')


if __name__ == '__main__':
    DO_WORK()