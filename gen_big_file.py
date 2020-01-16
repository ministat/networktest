# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

def gen_big_file0(serverIp):
   remoteCmd = subprocess.Popen(['ssh','b_carmel@{ip}'.format(ip=serverIp),'dd if=/dev/urandom of=bigfile bs=64M count=32'])
   remoteCmd.wait()

def gen_big_file(input):
   with open(input, 'r') as f:
      for i,line in enumerate(f):
          if (line.isspace()):
             continue
          ip=line.strip()
          gen_big_file0(ip)

if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input", help="Specify the ip addresses in sperated line")
   args = parser.parse_args()
   if args.input is None:
      print("No input file")
   else:
      gen_big_file(args.input)
