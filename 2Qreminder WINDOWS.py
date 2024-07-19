#!/usr/bin/env python3


import time
from plyer import notification

def remind(message, interval):
    while True:
        notification.notify(
            title='Reminder',
            message=message,
            timeout=10
        )
        time.sleep(interval)

if __name__ == "__main__":
    reminder_message = "1. How are you feeling currently? 2. What is one positive affirmation you need to hear right now?"
    interval_seconds = 30 * 60  # 30 minutes
    remind(reminder_message, interval_seconds)
import time
from plyer import notification
from datetime import datetime

def remind(message, interval, start_hour, end_hour):
    while True:
        current_hour = datetime.now().hour
        if start_hour <= current_hour < end_hour:
            notification.notify(
                title='Reminder',
                message=message,
                timeout=10
            )
        time.sleep(interval)

if __name__ == "__main__":
    reminder_message = "1. How are you feeling currently? 2. What is one positive affirmation you need to hear right now?"
    interval_seconds = 30 * 60  # 30 minutes
    start_hour = 7  # 7 AM
    end_hour = 16  # 4 PM (16 in 24-hour format)
    remind(reminder_message, interval_seconds, start_hour, end_hour)
