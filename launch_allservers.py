# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

def launch_netserver(serverIp):
   remoteCmd = subprocess.Popen(['ssh','b_carmel@{ip}'.format(ip=serverIp),'./netserver'])
   remoteCmd.wait()

def launch_ntttcp(serverIp):
   remoteCmd = subprocess.Popen(['ssh','b_carmel@{ip}'.format(ip=serverIp),'./ntttcp','-r -D -e'])
   remoteCmd.wait()

def launch_allservers(input,bench):
   with open(input, 'r') as f:
      for i,line in enumerate(f):
          if (line.isspace()):
             continue
          ip=line.strip()
          funcName="launch_{s}".format(s=bench)
          globals()[funcName](ip)

if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input", help="Specify the ip addresses in sperated line")
   parser.add_argument("-s", "--serverType", choices=["netserver","ntttcp"], type=str, help="Specify the bench type. Default is 'netserver'", default="netserver")
   args = parser.parse_args()
   if args.input is None:
      print("No input file")
   else:
      launch_allservers(args.input,args.serverType)
