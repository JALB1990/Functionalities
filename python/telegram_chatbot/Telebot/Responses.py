from datetime import datetime
import inc_create as ic

def sample_responses(input_text):
 user_message = str(input_text).lower()
 if ("hello" or "hi") in user_message:
  return ('''Hello Welcome to the bot,
  please use the following commands:
  /incident Create incident
  /status Incident status
  /help Show help
  ''')
 if user_message in ("time"):
  now = datetime.now()
  date_time = now.strftime("%d/%m%y, %H:%M:%S")
  return str(date_time)
 return "no data retrieved"