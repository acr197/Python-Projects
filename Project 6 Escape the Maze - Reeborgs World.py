{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Reeborg\'92s World Escape the Maze\
\
def turn_right():\
    turn_left()\
    turn_left()\
    turn_left() \
    \
#Prevent infinite error if robot starts without right wall\
while front_is_clear():\
    move()\
turn_left()\
\
#Main Loop when robot hits wall, turn. If not, move forward\
while not at_goal():\
    if not right_is_clear():\
        while wall_in_front():\
            turn_left()\
        move() \
    elif right_is_clear():\
        turn_right()\
        move()}