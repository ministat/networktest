import argparse
import subprocess
import sys

def distribute_app(input):
   with open(input, 'r') as f:
      for i,line in enumerate(f):
          if (line.isspace()):
             continue
          ip=line.strip()
          killBgCmd = subprocess.Popen(['ssh','b_carmel@{}'.format(ip),'killall netserver; killall ntttcp'])
          killBgCmd.wait()
          remoteCmd = subprocess.Popen(['scp','bigfile','netserver','netperf','ntttcp','b_carmel@{}:~/'.format(ip)])
          remoteCmd.wait()

if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input", help="Specify the ip addresses in sperated line")
   args = parser.parse_args()
   if args.input is None:
      print("No input file")
   else:
      distribute_app(args.input)
