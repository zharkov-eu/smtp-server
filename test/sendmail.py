import sys
import signal
import smtplib

def prompt(message):
    return input(message).strip()

def sigint_handler(signal, frame):
    print("\r\nThanks for using email client")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    fromaddr = prompt("From: ")
    toaddrs = prompt("To: ").split()

    msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))
    while 1:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        msg = msg + line + "\r\n"
else:
    fromaddr = "zharkov@yandex.ru"
    toaddrs = "kadyrov@example.com".split()

    msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))

    for i in range(0, 10000):
        msg = msg + "It is a big message!\r\n"

server = smtplib.SMTP('127.0.0.1', 2025, 'example.com')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()