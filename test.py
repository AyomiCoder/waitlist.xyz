import smtplib

try:
    server = smtplib.SMTP('smtp-relay.brevo.com', 2525)
    server.starttls()
    server.login('alukoayomide623@gmail.com', 'pPbcydgDEMSvK9UL')
    print("SMTP Connection Successful")
    server.quit()
except Exception as e:
    print("SMTP Connection Failed:", e)