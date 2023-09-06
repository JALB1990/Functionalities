#import os
#os.chdir(r"C:\Users\Ionock_Issha\Dropbox\Python\Wasap")
#https://api.telegram.org/bot5084500279:AAEI4NnFQqy3ibV0O8QqkShbCcXXgkpB2ZE/getUpdates
import Constants as keys
from telegram.ext import *
import Responses as R
import telegram
import contact_search as cs
import inc_create as ic
import em_ch as ec
import incident_search as incs

print("Bot started")

def start_command(update,context):
 update.message.reply_text('''Hello Welcome to the bot,
 please select one of the options:
 /help Show help
 /incident Create a new incident
 /status show the incident status
 ''')
	
def help_command(update,context):
 update.message.reply_text('For help please visit www.google.com')

# ---------- defining states ---------
ONE , TWO = range(2)

# ---------- functions ---------
def incident_command(update,context):
 chat_id = update.message.chat_id
 context.bot.send_message(chat_id , text = "Hello , in order to create an incident, you need to be identified. Please enter your employee id or your email.")
 return ONE

def got_contact(update,context):
 chat_id = update.message.chat_id
 contact_input = update.message.text.lower() # get the contact_input
 context.user_data["contact_input"] = contact_input # to use it later (in next func)
 try:
  ec.check(contact_input)
 except:
  try:
   int(contact_input)
  except:
   context.bot.send_message(chat_id , text = f"Error. You entered an incorrect email address or employee id.")
   return ConversationHandler.END
  else:
   contact_id = cs.check(contact_input)
   if contact_id == False:
    context.bot.send_message(chat_id , text = f"The employee id or the email {contact_input} is wrong or does not exist")
    return ConversationHandler.END
   else:
    context.bot.send_message(chat_id , text = f"Thanks! please enter your incident description:")
    return TWO  
 else:
  contact_id = cs.check(contact_input)
  if contact_id == False:
   context.bot.send_message(chat_id , text = f"The employee id or the email {contact_input} is wrong or does not exist")
   return ConversationHandler.END
  else:
   context.bot.send_message(chat_id , text = f"Thanks! please enter your incident description:")
   return TWO

def got_inc_desc(update,context):
 chat_id = update.message.chat_id
 inc_desc = update.message.text # now we got the incident
 contact_input = context.user_data["contact_input"] # we had the contact_input , remember ?!
 #print(contact_input)
 contact_id = cs.check(contact_input)
 #print(contact_id)
 ref_number = ic.inc_create(contact_id,inc_desc)
 context.bot.send_message(chat_id , text = f"Completed ! your Reference Number is {ref_number}")
 return ConversationHandler.END

def cancel(update,context):
     chat_id = update.message.chat_id
     context.bot.send_message(chat_id , text = "process canceled !")
     return ConversationHandler.END

# ---------- conversation handler ---------
CH = ConversationHandler (entry_points = [CommandHandler("incident", incident_command)],
 states = {ONE : [MessageHandler(Filters.text , got_contact)],
 TWO : [MessageHandler(Filters.text , got_inc_desc)]
 },
 fallbacks = [MessageHandler(Filters.regex('cancel'), cancel)],
 allow_reentry = True)

def status_command(update,context):
 #print('status command')
 chat_id = update.message.chat_id
 context.bot.send_message(chat_id , text = "Hello , in order to search an incident stats, you need to include the reference number example 211201-000010")
 return ONE


def search_ref_number(update,context):
 #print('search')
 chat_id = update.message.chat_id
 ref_number = update.message.text.lower() # get the ref numb
 inc_status = incs.check(ref_number)
 if inc_status == False:
  context.bot.send_message(chat_id , text = f"The reference number {ref_number} retrieved no information. It is wrong or does not exist")
 else:
  context.bot.send_message(chat_id , text = f"Completed ! the incident {ref_number} has the status {inc_status}")
  return ConversationHandler.END


CH_status = ConversationHandler (entry_points = [CommandHandler("status", status_command)],
 states = {ONE : [MessageHandler(Filters.text , search_ref_number)]
 },
 fallbacks = [MessageHandler(Filters.regex('cancel'), cancel)],
 allow_reentry = True)
	
def handle_message(update,context):
 text = str(update.message.text).lower()
 response = R.sample_responses(text)
 update.message.reply_text(response)
	
def error(update,context):
	print(f"Update {update} caused error {context.error}")


def main():
	updater = Updater(keys.API_KEY,use_context=True)
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler("start",start_command))
	dp.add_handler(CommandHandler("help",help_command))
	dp.add_handler(CH)
	dp.add_handler(CH_status)
	dp.add_handler(MessageHandler(Filters.text,handle_message))

	dp.add_error_handler(error)
	
	updater.start_polling() #5seg
	updater.idle()

main()

