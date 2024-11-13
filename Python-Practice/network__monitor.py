import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email alert configuration
email_alerts = True  # Set to False if you don't want email alerts
sender_email = "mesekooluwajuwon@gmail.com"  # Replace with your Gmail address
receiver_email = "mesekooluwajuwon@gmail.com"  # Replace with recipient email address
email_password = "twriqsbacuszurdf"  # Replace with app-specific password

smtp_server = "smtp.gmail.com"
smtp_port = 587

# List of devices to monitor with their IPs
devices = [
    {'name': 'Google DNS', 'ip': '8.8.8.8', 'status': 'Unknown'},
    {'name': 'Cloudflare DNS', 'ip': '1.1.1.1', 'status': 'Unknown'},
    {'name': 'Test Unreachable IP', 'ip': '192.0.2.1', 'status': 'Unknown'}  # This IP is unreachable, triggers Offline
]


# Function to send an email alert if a device goes offline or online
def send_email_alert(device):
    """Sends an email alert if a device changes status."""
    subject = f"ALERT: {device['name']} is {device['status']}"
    body = f"Device {device['name']} with IP {device['ip']} is currently {device['status']}."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email alert sent for {device['name']} ({device['ip']}) - {device['status']}.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Function to ping a device and return True if reachable
def ping_device(ip):
    """Pings a device by IP address and returns True if reachable."""
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return response == 0


# Function to log and print the status of each device
def log_status(device, status):
    """Logs the current status of the device and prints it."""
    print(f"{device['name']} ({device['ip']}) is {status}")


# Main monitoring loop
def monitor_devices():
    """Continuously monitor devices by pinging them."""
    print("Starting device health monitor...")
    while True:
        for device in devices:
            is_online = ping_device(device['ip'])
            new_status = "Online" if is_online else "Offline"

            # If the status has changed, log it and send an alert
            if device['status'] != new_status:
                log_status(device, new_status)
                device['status'] = new_status

                # Send alert if device goes offline or online
                if email_alerts:
                    send_email_alert(device)

        # Wait before pinging again (adjust sleep time as needed)
        time.sleep(60)  # Ping devices every 60 seconds

# Run the monitoring loop
monitor_devices()
