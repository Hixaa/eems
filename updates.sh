#!/bin/bash

"[+] Creating data_storage folder"
mkdir -p /data_storage
cd /components

echo "[+] Backup Existing Code"
mv app.py app.py.bak
mv cloudService.py cloudService.py.bak

echo "[+] Getting new source"
wget https://raw.githubusercontent.com/Hixaa/eemsV3/main/xaees/components/cloudService.py
wget https://raw.githubusercontent.com/Hixaa/eemsV3/main/xaees/components/app.py

config_file="/config_xaees.ini"

function update_company_id {
	company_id="$1"
	sed -i "s/^\(id *= *\).*/\1$company_id/" "$config_file"
}

function update_url {
	new_url="https://rakshaiot.com/api/v1/ioEntry"
	sed -i "s,^\(url *= *\).*,\1$new_url," "$config_file"
}

if [ $# -eq 1 ]; then
	argument="$1"
	update_company_id "$argument"
	update_url
	echo "[+] Config Updated"
else
	echo "Usage: $0 <company_id>"
	exit 1

fi

echo "[+] Redownloading source"
cd /home/pi
rm -rf eemsv2
git clone https://github.com/hixaa/eemsv2

echo "[*] Done"
