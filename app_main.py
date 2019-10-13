#
from app.learn.egs_app import EgsApp

def main():
  print('DMRL v0.0.1 build 4')
  app = EgsApp()
  app.startup()

if '__main__' == __name__:
  main()
