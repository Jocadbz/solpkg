# import shit WHOAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# import Break
import os
import sys


def INSTALL():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    os.system(f'sudo eopkg it {new}')


def VERSION():
    print("Solpkg version: 1.4.0")
    os.system("eopkg --version")


def UPGRADE():
   os.system('sudo eopkg up')


def REMOVE():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f"sudo eopkg rm {new}")


def CLEAN():
   os.system('sudo eopkg clean && sudo eopkg rmo')


def SEARCH():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f'sudo eopkg sr {new}')


def INFO():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f'sudo eopkg info {new}')


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
         else:
            print('Unrecognised argument.')
            print('Try running with --help flag to see current commands')


if __name__ == '__main__':
    DO_WORK()
