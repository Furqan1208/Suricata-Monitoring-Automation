import smtplib
import time

# Email Configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'  
smtp_password = 'your_app_password'  
from_email = 'your_email@gmail.com'  
to_email = 'recipient@example.com'  

subject = 'Suricata Alert Notification'

# Path to Suricata fast.log
fast_log_path = '/var/log/suricata/fast.log'

# Function to send email
def send_email(alert_message):
    body = f'Suricata Alert:\n\n{alert_message}'
    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_email, message)
            print("Alert email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to monitor the log file
def monitor_fast_log():
    try:
        print("Monitoring Suricata fast.log for alerts...")
        with open(fast_log_path, 'r') as log_file:
            log_file.seek(0, 2)  # Move to the end of the file

            while True:
                line = log_file.readline()
                if not line:
                    time.sleep(1)  # Wait for new lines
                    continue

                # Check for specific alert patterns
                if ':2100498:' in line or ':2100499:' in line:  # Example SID matches
                    print(f"Alert found: {line.strip()}")
                    send_email(line.strip())
    except FileNotFoundError:
        print(f"Error: The log file '{fast_log_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    monitor_fast_log()
