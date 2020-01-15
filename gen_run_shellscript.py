# -*- coding: utf-8 -*-
import argparse
import random
import subprocess
import sys

DUR=120 # duration in seconds
SEND_SIZE=1024*1024
RECV_SIZE=1024*1024

def netperf_maerts_bench(senderIp,recverIp):
   cmd="nohup ssh b_carmel@{s} ./netperf -t TCP_MAERTS -H{r} -- -s {sendSz} -S {recvSz} &".format(s=senderIp, r=recverIp, sendSz=SEND_SIZE, recvSz=RECV_SIZE)
   print(cmd)

def netperf_sendfile_bench(senderIp,recverIp):
   cmd="nohup ssh b_carmel@{s} ./netperf -t TCP_SENDFILE -H{r} -F bigfile -- -s {sendSz} -S {recvSz} &".format(s=senderIp, r=recverIp, sendSz=SEND_SIZE, recvSz=RECV_SIZE)
   print(cmd)

def netperf_rr_bench(senderIp,recverIp):
   cmd="nohup ssh b_carmel@{s} ./netperf -t TCP_RR -H{r} -- -r {sendSz},{recvSz} -l {d} &".format(s=senderIp, r=recverIp, sendSz=SEND_SIZE, recvSz=RECV_SIZE, d=DUR)
   print(cmd)

def ntttcp_bench(senderIp, recverIp):
   cmd="nohup ssh b_carmel@{s} ./ntttcp -s{r} --show-tcp-retrans -x -t {d} -N -b 4M &".format(s=senderIp, r=recverIp, d=DUR)
   print(cmd)

def gen_script(input, bench):
   iplist=[]
   with open(input, 'r') as f:
      senderIp=""
      for i,line in enumerate(f):
          if (line.isspace()):
             continue
          ip=line.strip()
          iplist.append(ip)
      assert len(iplist) % 2 == 0, "IP list number must be even"
      random.shuffle(iplist) # shuffle the ip to construct random send<->recv pairs
      for i,ip in enumerate(iplist):
          if (i%2 != 0):
             func="{bench_name}_bench".format(bench_name=bench)
             globals()[func](senderIp, ip)
          senderIp=ip

if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input", help="Specify the ip addresses in sperated line")
   parser.add_argument("-t", "--type", choices=["netperf_sendfile","netperf_maerts","netperf_rr","ntttcp"], type=str, help="Specify the bench type. Default is 'netperf_sendfile'", default="netperf_sendfile")
   args = parser.parse_args()
   if args.input is None:
      print("No input file")
   else:
      if args.type != None:
         gen_script(args.input, args.type)
