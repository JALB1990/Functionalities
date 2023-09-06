# ---------- defining states ---------
ONE , TWO = range(2)

# ---------- functions ---------
def incident_command(update,context):
     chat_id = update.message.chat_id
     bot.send_message(chat_id , text = "Hello , in order to create an incident, you need to be identified. Please enter your employee id or your email.")
     return ONE

def got_contact(update,context):
 chat_id = update.message.chat_id
 contact_input = update.message.text-lower() # get the contact_input
 context.user_data["contact_input"] = contact_input # to use it later (in next func)
 try:
  cs.check(contact_input)
 except:
  bot.send_message(chat_id , text = f"Error. The employee id or the email {contact_input} is wrong or does not exist")
  return ConversationHandler.END
 else:
  contact_id = CS.check(contact_input)
  bot.send_message(chat_id , text = f"Thanks {contact_id} ! please enter your incident description:")
  return TWO

def got_inc_desc(update,context):
 chat_id = update.message.chat_id
 inc_desc = update.message.text # now we got the incident
 #contact_input = context.user_data["contact_input"] # we had the contact_input , remember ?!
 ref_number = ic.inc_create(contact_id,inc_desc)
 bot.send_message(chat_id , text = f"Completed ! your Reference Number is {ref_number}")
 return ConversationHandler.END

def cancel(update,context):
     chat_id = update.message.chat_id
     bot.send_message(chat_id , text = "process canceled !")
     return ConversationHandler.END

# ---------- conversation handler ---------
CH = ConversationHandler (entry_points = [CommandHandler("incident", incident_command)],
 states = {ONE : [MessageHandler(Filters.text , got_contact)],
 TWO : [MessageHandler(Filters.text , got_inc_desc)]
 },
 fallbacks = [MessageHandler(Filters.regex('cancel'), cancel)],
 allow-reentry = True)

# -------- add handler ---------
updater.dispatcher.add_handler(CH)