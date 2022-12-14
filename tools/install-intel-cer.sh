#!/usr/bin/env bash
  
cd /usr/local/share/ca-certificates/
  
wget http://owrdropbox.intel.com/dropbox/public/Ansible/certificates/IntelCA5A-base64.crt
wget http://owrdropbox.intel.com/dropbox/public/Ansible/certificates/IntelCA5B-base64.crt
wget http://owrdropbox.intel.com/dropbox/public/Ansible/certificates/IntelSHA256RootCA-base64.crt
  
update-ca-certificates
systemctl daemon-reload
systemctl restart docker

