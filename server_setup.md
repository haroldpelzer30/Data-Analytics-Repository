# Cloud Infrastructure Documentation
**Host:** Linode (Akamai) VPS
**OS:** Ubuntu 22.04 LTS
**Purpose:** 24/7 Hosting for FlyGuy AeroSniper Market Scanner

### Configuration Details
* **Security:** Configured UFW (Uncomplicated Firewall) to restrict all ports except SSH.
* **Access:** Key-based SSH authentication enabled (Password login disabled).
* **Environment:** Python 3.10 virtual environment for dependency isolation.
* **Automation:** Crontab scheduled for 15-minute execution cycles to match candle intervals.
