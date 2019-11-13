#!/bin/bash 

#check if the folder where you are running this command/script contains folders named policy manager and systemlogs, if so, continue if not, then show an error.

today=`date +%Y-%m-%d.%H:%M:%S`
folder=$(basename `pwd`)
exec > initial-analysis-$folder-$today.txt 2>&1

#exec > ~/LOGS/initial_analysis.txt 2>&1

echo "HardWare or Virtual Appliance: "
echo "-----------------------------"
echo
grep -i 'HARDWARE_VERSION' ./tmp*/SystemLogs/sysinfo.txt
echo




echo "Server list:"
echo "------------"
echo
sed -n '/Cluster servers table/,//p' ./tmp*/PolicyManagerLogs/postgres-info.txt
echo




echo "ClearPass Version: "
echo "-----------------"
echo
cat ./tmp*/PolicyManagerLogs/tips-version.properties
echo


echo "FIPS enabled or not: "
echo "--------------------"
echo
cat ./tmp*/PolicyManagerLogs/fips-config.properties
echo



echo "Is node disabled or not:"
echo "-----------------------"
echo
cat ./tmp*/PolicyManagerLogs/localnode.status
echo



echo "Server failed over or not: "
echo "-------------------------"
echo
cat ./tmp*/PolicyManagerLogs/cluster-failover.json
echo


echo
echo "Core files generated or not :"
echo "----------------------------"
echo
cat ./tmp*/PolicyManagerLogs/core-files.list
echo 



echo "The network details of the server from which logs were collected: "
echo "-----------------------------------------------------------------"
echo
cat  ./tmp*/PolicyManagerLogs/system-network-config.properties
echo



echo "License Details: "
echo "-----------------"
echo
grep -i '|license_key=' ./tmp*/PolicyManagerLogs/activation-client/activation-client.log.0 | tail -n 1 
echo



echo "Previous partitions: "
echo "--------------------"
echo
grep -i 'title ClearPass Platform' ./tmp*/SystemLogs/grub.conf
echo


echo "Insight Enabled nodes: "
echo "----------------------"
echo
cat ./tmp*/PolicyManagerLogs/netevents-info.txt 
echo


echo "Database sizes: "
echo "--------------"
echo
value=`grep 'APP_MINOR_VERSION' ./tmp*/PolicyManagerLogs/tips-version.properties | cut -d "=" -f 2`
value2=`grep 'APP_SERVICE_RELEAS' ./tmp*/PolicyManagerLogs/tips-version.properties | cut -d "=" -f 2`
if [ $value == 7 -o $value2 == 10 ]
then
	sed -n '/Size of all databases/,/[^A-Z a-z -]$/p' ./tmp*/PolicyManagerLogs/postgres-info.txt
else
	sed -n '/Top database sizes:/,/Relation names in tipsdb:/p' ./tmp*/PolicyManagerLogs/postgres-info.txt
fi
echo

isInFile=$(cat ./tmp*/PolicyManagerLogs/tips-version.properties | grep -c "APP_MINOR_VERSION=7")
sys_reqInFile=$(cat ./tmp*/PolicyManagerLogs/tips-utils/utils.log | grep -c 'Current system configuration')

if [ $isInFile -eq 0  -a $sys_reqInFile -eq 0 ]
then
#	if [  ]
	echo "System requirements: "
	echo "-------------------"
	echo
	sed -n '/Current system configuration/,/^$/p' ./tmp*/PolicyManagerLogs/tips-utils/utils.log | tail -n 18
else

	echo "System requirements: "
	echo "-------------------"
	echo
	sed -n '/Current system configuration/,/^$/p' ./tmp*/PolicyManagerLogs/tips-utils/utils.log | tail -n 18
	echo

fi
echo "Server reboot history: "
echo "---------------------"
echo
sed -n '/System login activity:/,//p' ./tmp*/SystemLogs/sysinfo.txt
echo


echo "Licenses :"
echo "--------"
echo
count=`ls ./tmp*/ConfigBackup/ | wc -l`
config_file_exist=`ls -l ./tmp*/ | grep -i Config`

if [ $? == 0  ]; then
if [ $count == 1 ]; then
tar xzf ./tmp*/ConfigBackup/config-backup.tgz -C ./tmp*/ConfigBackup/
pg_restore ./tmp*/ConfigBackup/PolicyManager/tipsdb.pgdump > tipsdb_content.txt
pg_restore ./tmp*/ConfigBackup/AppPlatform/AppPlatform.pgdump > appPlatform_content.txt
echo
sed -n '/^COPY license_info/,/^$/p' appPlatform_content.txt
echo
sed -n '/^COPY license_info/,/^$/p' tipsdb_content.txt
else
echo "else block - that means, the file is already extracted."
pg_restore ./tmp*/ConfigBackup/AppPlatform/AppPlatform.pgdump > appPlatform_content.txt
echo
sed -n '/^COPY license_info/,/^$/p' appPlatform_content.txt
echo
pg_restore ./tmp*/ConfigBackup/PolicyManager/tipsdb.pgdump > tipsdb_content.txt
sed -n '/^COPY license_info/,/^$/p' tipsdb_content.txt
fi
fi
echo


echo "Virutal IP config:"
echo "-----------------"
echo
if [ -e ./tmp*/PolicyManagerLogs/vip-service/vip* ]
then
	cat ./tmp*/PolicyManagerLogs/vip-service/vip*
else
	sed -n '/COPY cppm_virtual_ip_nodes/,/Data for Name: device_dict/p' tipsdb_content.txt
fi
echo
echo

echo "CPPM Application access control lists: "
echo "--------------------------------------"
echo
cat ./tmp*/SystemLogs/etc/httpd/conf.d/cppm-access-control.conf
echo

cp  initial-analysis* ~/LOGS/
echo `pwd`

ls -lsh

