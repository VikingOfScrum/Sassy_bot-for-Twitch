''' 
A bot that interacts with host and viewers on twitch.

A twitch bot that connects to twitch irc and interacts with host and viewers by searching
for key words for triggering a command or by a simple command flag "!" followed by a command
following the flag. Some of the commands will include a game and various other tasks.

Joey Hanson

import required modules
set up required connection information for twitch
create function for commands
create function for game
create interactive chat function
create function for ping pong with server
create main bot function 
'''

import string
import random
from FateBot import Fate_Bot
import socket
import irc

WORD_LIST = "words.txt"
SERVER = 'irc.twitch.tv' 
PORT = 6667
PASS = "oauth:s0t9elirohr4ro1jbl525zzaq0binx"
BOT = 'Sassy_Bot'
CHANNEL = 'vendicious'
OWNER = '11bviking'     #^ required information to connect to twitch server with bot
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send((  "PASS " + PASS + "\n" + 
            "NICK " + BOT + "\n" +
            "JOIN #" + CHANNEL + "\n").encode())   #sends the required information to twitch to gain access to channel and encodes it

def connecting_to_chat():
    '''Continues to try to Connect to chat room of HOST using while loop '''
    connecting = True
    while connecting:
        read_buffer_join = irc.recv(1024)
        read_buffer_join = read_buffer_join.decode()
        for i in read_buffer_join.split("\n")[0:-1]:
            connecting = connected_to_chat(i)

def connected_to_chat(i):
    '''Check to see if it has succesfully connected to chat room by reading 
    the lines one by one and if END  of /NAMES is last line if is returns false to
    end loop to connecting_to_chat if else returns true and trys to connect again '''
    if ("End of /NAMES list" in i):
        print("Sassy_Bot has joined " + CHANNEL + "'s channel." )
        send_message_chat(irc, "Sassy Bot has Joined")
        return False
    else:
        return True

def send_message_chat(irc, message):
    '''Sets up a place holder message to let the channel know the bot has connected. '''
    message_temp = "PRIVMSG #" + CHANNEL + " :" + message
    irc.send((message_temp + "\n").encode())

def slice_user(line):
    '''Slices the user's name from the rest of the message to make it more readable for humans '''
    split_user = line.split(":", 2)
    user = split_user[1].split("!", 1)[0]
    return user
def slice_message(line):
    '''Slices the user's message from the rest of the message to make it more readable for humans '''
    try:
        split_message = (line.split(":", 2))[2]
    except:
        split_message = ""
    return split_message

def user_or_server(line):
    '''Checks to see if message is from user or twitch server, user returns false, server returns true '''
    if "PRIVMSG" in line:
        return False
    else:
        return True

def dice_game(user):
    '''Plays a  dice game from another file and returns the values and sends them in to chat'''
    fate, messag = Fate_Bot()
    mes = (f"{user}, You have rolled a {fate} and....{messag}")
    send_message = "PRIVMSG #" + CHANNEL + " :" + mes
    irc.send((send_message + "\n").encode())

def random_word():
    '''Opens the file words.txt splits all the words and selects a random word to display'''
    inFile = open(WORD_LIST, "r")
    line = inFile.readline()
    word_list = line.split()
    word = random.choice(word_list)
    send_word = "PRIVMSG #" + CHANNEL + " :" + word
    irc.send((send_word + "\n").encode())

def main():
    '''Main function of bot. Calls on connecting_to_chat to start connection. Then if connection is made
    it goes through a while True loop to continue monitoring the chat feed for a ping request from twitch.
    It will respond to request with a pong. It will also interact with viewers with a few commands be it a
    dice game or a random word from a text file'''

    connecting_to_chat()
    
    
    while True:  
        
        try:
            read_buffer = irc.recv(1024).decode() # decodes data from server
        except:
            read_buffer = ""
        for line in read_buffer.split("\r\n"):
            if line == "":
                continue
            if "PING" in line and user_or_server(line):
                msg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msg)
                print(msg)        #^ responds to server's pings
                continue
            if"!dice" in line:
                user = slice_user(line)  # calls dice game from FateBot.py
                dice_game(user)  
            if "Hello" and "twitch_bot_uber_eats" in  line:
                user = slice_user(line)
                hi_message = "Hello, " + user + "!"               
                send_hello =  "PRIVMSG #" + CHANNEL + " :" + hi_message
                irc.send((send_hello + "\n").encode())      #^ Says hello back to the user who said hi to bot
            if "!randomword" in line:
                random_word()
            else:
                user = slice_user(line)
                message = slice_message(line) #< prints messages in terminal for everything else from users
                print(user + ": "+ message)
            sleep(.1)
            #^ helps with load 
        
        


    