pip install schedule
import smtplib
import schedule
import time

# Your email and password (make sure to use an "App Password" if using Gmail)
email = "your_email@gmail.com"
password = "your_password"

# Recipient email address
recipient_email = "recipient_email@example.com"

# Define the function to send an email
def send_reminder_email():
    subject = "Daily Reminder"
    body = "Don't forget to work on your goals today!"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient_email, message)
            print("Reminder email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the daily reminder
schedule.every().day.at("08:00").do(send_reminder_email)  # Adjust the time as needed

# Main loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)

