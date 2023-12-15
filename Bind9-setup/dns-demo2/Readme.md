# Steps to use Bind9

- Inside /etc/systemd/resolved.conf, set DNSStubListener=no

- Execute: `sudo systemctl restart systemd-resolved`

- Execute: ```sudo docker-compose up```

# Steps to pass DNS traffic through Bind9

- Inside /etc/systemd/resolved.conf, set `DNS=127.0.0.1` (ip of the bind9 server)

- Execute: `sudo systemctl restart systemd-resolved`

# Steps to swith everything back to original form

- close the docker container
- Execute `sudo docker-compose down`
- reset all the changes done to /etc/systemd/resolved.conf file
- Execute: `sudo systemctl restart systemd-resolved`