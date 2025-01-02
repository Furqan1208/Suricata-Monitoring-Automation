# Suricata-Monitoring-Automation
A comprehensive solution for deploying Suricata, monitoring its logs, and automating email notifications for real-time alerts.

## Suricata Installation  

Suricata is an open-source intrusion detection system (IDS) and intrusion prevention system (IPS). Follow the steps below to install and configure Suricata on your system.  

### Step 1: Update the System  
```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Suricata  
```bash
sudo apt install suricata -y
```

### Step 3: Configure Suricata
Edit the configuration file to enable fast.log:
```bash
sudo nano /etc/suricata/suricata.yaml
```

Locate the fast.log section and ensure it is enabled:
```bash
outputs:
  - fast:
      enabled: yes
```
### Step 4: Start Suricata
Start Suricata as a service or in daemon mode:
```bash
sudo systemctl start suricata
```

### Step 5: Verify Logging
Ensure fast.log is being generated in /var/log/suricata/:
```bash
tail -f /var/log/suricata/fast.log
```

# Email Alert Automation
Python Script Overview
The Python script continuously monitors fast.log and sends email notifications for specific alerts based on their SIDs.

## Installation
### Step 1: Install Required Libraries
Ensure Python 3.x is installed. Then, install the required libraries:
```bash
pip install smtplib
```

### Step 2: Configure the Script
Download the suricata_email_alert.py file and update the email configuration in the script:
```bash
smtp_username = '***@***.com'  # Replace with your email address
smtp_password = '***'         # Replace with your app-specific password
from_email = '***@***.com'    # Replace with your email address
to_email = '***@***.com'      # Replace with recipient's email address
fast_log_path = '/var/log/suricata/fast.log'  # Path to Suricata's fast.log
```

### Step 3: Run the Script
Run the script to monitor Suricata alerts and send email notifications:
```bash
python3 suricata_email_alert.py
```
### Example Alerts and Notifications
![Screenshot 2025-01-02 133734](https://github.com/user-attachments/assets/bea7c7b7-c342-4fd0-8ef8-64fb86fe4e5c)

![Screenshot 2025-01-02 133421](https://github.com/user-attachments/assets/79a36a08-980a-424a-ba0a-6f91068cad45)


