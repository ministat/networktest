import argparse
import subprocess
import sys

def get_ip(input):
   with open(input, 'r') as f:
      for i,line in enumerate(f):
          if (line.isspace()):
             continue
          hostname=line.strip()
          remoteCmd = subprocess.Popen(['ssh',hostname,'hostname -i'])
          remoteCmd.wait()

if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input", help="Specify the hostname file who has every hostname in sperated line")
   args = parser.parse_args()
   if args.input is None:
      print("No input file")
   else:
      get_ip(args.input)
