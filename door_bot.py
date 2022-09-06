import logging

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
	format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#Buttons names
buttons = {
	'control_buttons':{
		'begin_button':'Begin',
		'start_button':'Start',
		'stop_button':'Stop',
		'exit_button':'Exit'
	},
	'switch_mode_buttons':{
		'camera_mode_button':'Camera mode',
		'voice_mode_button':'Voice mode',
		'remote_mode_button':'Remote mode'
	},
	'door_action_buttons':{
		'open_button':'Open',
		'close_button':'Close'
	},
	'bulb_action_buttons':{
		'turn_on_button':'Turn on',
		'turn_off_button':'Turn off'
	}
}

#Switch to camera mode
def camera_mode_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['remote_mode_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Camera mode on",
		reply_markup = reply_markup
	)

#Switch to voice mode
def voice_mode_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['remote_mode_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Voice mode on",
		reply_markup = reply_markup
	)

#Button for closing door
def close_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button'])
			],
			[
				KeyboardButton(text = buttons['door_action_buttons']['open_button']),
				KeyboardButton(text = buttons['door_action_buttons']['close_button'])
			],
			[
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_on_button']),
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_off_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Door closed.",
		reply_markup = reply_markup
	)

#Button for opening door
def open_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button'])
			],
			[
				KeyboardButton(text = buttons['door_action_buttons']['open_button']),
				KeyboardButton(text = buttons['door_action_buttons']['close_button'])
			],
			[
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_on_button']),
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_off_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Door opened.",
		reply_markup = reply_markup
	)

#Button for turning on bulb
def turn_on_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button'])
			],
			[
				KeyboardButton(text = buttons['door_action_buttons']['open_button']),
				KeyboardButton(text = buttons['door_action_buttons']['close_button'])
			],
			[
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_on_button']),
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_off_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Bulb turned on.",
		reply_markup = reply_markup
	)

#Button for turning off bulb
def turn_off_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button'])
			],
			[
				KeyboardButton(text = buttons['door_action_buttons']['open_button']),
				KeyboardButton(text = buttons['door_action_buttons']['close_button'])
			],
			[
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_on_button']),
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_off_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Bulb turned off.",
		reply_markup = reply_markup
	)

#Switch to remote control mode
def remote_mode_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button'])
			],
			[
				KeyboardButton(text = buttons['door_action_buttons']['open_button']),
				KeyboardButton(text = buttons['door_action_buttons']['close_button'])
			],
			[
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_on_button']),
				KeyboardButton(text = buttons['bulb_action_buttons']['turn_off_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Remote mode on",
		reply_markup = reply_markup
	)

#Stop working with smart door
def stop_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text =  buttons['control_buttons']['start_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True
	)

	update.message.reply_text(
		text = "Stoped.",
		reply_markup = reply_markup
	)

#Start working with smart door(show all options)
def start_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['switch_mode_buttons']['camera_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['voice_mode_button']),
				KeyboardButton(text = buttons['switch_mode_buttons']['remote_mode_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['stop_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Starting...",
		reply_markup = reply_markup
	)

#Exit from remote control
def exit_button_handler(update: Update, context: CallbackContext):
	update.message.reply_text(
		text = "Bye!",
		reply_markup = ReplyKeyboardRemove()
	)

#Begin remote control
def begin_button_handler(update: Update, context: CallbackContext):
	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text =  buttons['control_buttons']['start_button'])
			],
			[
				KeyboardButton(text = buttons['control_buttons']['exit_button'])
			]
		],
		resize_keyboard = True,
	)

	update.message.reply_text(
		text = "Let's begin!",
		reply_markup = reply_markup
	)

#Checks wich button was clicked
def button_checker(update: Update, context: CallbackContext):
	text = update.message.text

	#Main control buttons
	if text == buttons['control_buttons']['begin_button']:
		return begin_button_handler(update = update, context = context)
	elif text == buttons['control_buttons']['start_button']:
		return start_button_handler(update = update, context = context)
	elif text == buttons['control_buttons']['stop_button']:
		return stop_button_handler(update = update, context = context)
	elif text == buttons['control_buttons']['exit_button']:
		return exit_button_handler(update = update, context = context)

	#Switch mode buttons
	elif text == buttons['switch_mode_buttons']['camera_mode_button']:
		return camera_mode_button_handler(update = update, context = context)
	elif text == buttons['switch_mode_buttons']['voice_mode_button']:
		return voice_mode_button_handler(update = update, context = context)
	elif text == buttons['switch_mode_buttons']['remote_mode_button']:
		return remote_mode_button_handler(update = update, context = context)

	#Door action control buttons
	elif text == buttons['door_action_buttons']['open_button']:
		return open_button_handler(update = update, context = context)
	elif text == buttons['door_action_buttons']['close_button']:
		return close_button_handler(update = update, context = context)

	#Bulb action control buttons
	elif text == buttons['bulb_action_buttons']['turn_on_button']:
		return turn_on_button_handler(update = update, context = context)
	elif text == buttons['bulb_action_buttons']['turn_off_button']:
		return turn_off_button_handler(update = update, context = context)

#/start command
def start(update: Update, context: CallbackContext):
	user = update.effective_user

	reply_markup = ReplyKeyboardMarkup(
		keyboard = [
			[
				KeyboardButton(text = buttons['control_buttons']['begin_button'])
			],
		],
		resize_keyboard = True,
	)

	update.message.reply_markdown(
		 fr'Hi {user.mention_markdown()}!',
		reply_markup = reply_markup
	)

def main():
	updater = Updater(
		token = 'TOKEN',
		use_context = True
	)

	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(MessageHandler(Filters.text, button_checker))
	#dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	main()
