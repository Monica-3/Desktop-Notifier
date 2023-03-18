from plyer import notification
import time

title = 'Notification Title'
message = 'Notification Message'

while True:
    notification.notify(
        title=title,
        message=message,
        app_name='Python Notifier',
        timeout=10
    )
    time.sleep(60)

