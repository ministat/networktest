. ./env.sh
INPUT_HOST=hostname.txt   # <- specify the hostname lists
IPLIST=iplist.txt
BATCH_SCRIPT=batch_run.sh

function launch_netperf()
{
  python launch_allservers.py -i $IPLIST -s netserver
}

function launch_ntttcp()
{
  python launch_allservers.py -i $IPLIST -s ntttcp
}

function launch_server()
{
  local func_name="launch_"$TYPE
  eval $func_name
}

function gen_script_netperf()
{
  python gen_run_shellscript.py -i $IPLIST -t netperf_sendfile > $BATCH_SCRIPT
  python gen_run_shellscript.py -i $IPLIST -t netperf_maerts >> $BATCH_SCRIPT
  python gen_run_shellscript.py -i $IPLIST -t netperf_rr >> $BATCH_SCRIPT
}

function gen_script_ntttcp()
{
  python gen_run_shellscript.py -i $IPLIST -t ntttcp > $BATCH_SCRIPT
}

function gen_script()
{
  local func_name="gen_script_"$TYPE
  eval $func_name
}

python get_ip.py -i $INPUT_HOST > $IPLIST # get the IPs for all nodes

python distribute_apps.py -i $IPLIST       # distribute the test apps together with data to test nodes.

launch_server
#if [ "$TYPE" == "netperf" ]; then
#  python launch_allservers.py -i $IPLIST -s netserver
#else
#  if [ "$TYPE" == "ntttcp" ]; then
#     python launch_allservers.py -i $IPLIST -s ntttcp
#  fi
#fi

gen_script

chmod +x $BATCH_SCRIPT
./$BATCH_SCRIPT
