import subprocess
import schedule
import datetime

dns_servers = [
  None,  # Use the default
  "8.8.8.8",  # Google public DNS
  "208.67.222.222",  # OpenDNS
]

domains = [
  "heartbeat.spangle.org.uk"
]

delay = 5  # Seconds to wait between attempts
logfile = "dns_probe.log"

def check_dns():
  now = datetime.datetime.now()
  for domain in domans:
    for dns_server in dns_servers:
      args = [domain]
      if dns_server:
        args.append(dns_server)
      result = subprocess.run(["host", *args], capture_output=True, text=True)
      with open(logfile, "a") as f:
        f.write(f"{now.isoformat()} Domain: {domain}; DNS: {dns_server}; Status: {result.returncode}; StdOut: {result.stdout}; StdErr: {result.stderr}")

schedule.every(5).seconds.do(check_dns)
