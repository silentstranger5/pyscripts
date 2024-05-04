import smtplib
import ssl

subject = input("Subject: ").strip()
fromaddr = input("From: ").strip()
toaddr = input("To: ").strip().split()
filename = input("Password file: ").strip()

try:
    f = open(filename, 'r')
except OSError:
    exit("Invalid password file.")
else:
    password = f.read()
    f.close()

msg = f"Subject: {subject}\r\n"
msg += f"From: {fromaddr}\r\n"
msg += f"To: {', '.join(toaddr)}\r\n\r\n"

print("Enter message, end with ^D (Unix) or ^Z (Windows): ")

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg += line

print("Message length is", len(msg))

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    try:
        smtp.login(fromaddr, password)
    except smtplib.SMTPAuthenticationError:
        exit("Invalid credentials.")
    else:
        smtp.sendmail(fromaddr, toaddr, msg)
