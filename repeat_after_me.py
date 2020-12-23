#!/bin/env python3

import pyautogui as pi
import argparse
import datetime
from time import sleep



# this app is meant to be for simple actions that are tedious to repeat.
# pending actions to add: hotkey

# section for recording actions
def position():
    pos = pi.position()
    return "pos: {},{}".format(pos.x, pos.y)

def mouse_left():
    return "click: left"

def mouse_right():
    return "click: right"

def type_text(text):
    return "type: {}".format(text)

def press_btn(button):
    return "press: {}".format(button)

action_type = {
        "position" : position,
        "right" : mouse_right,
        "left" : mouse_left,
        "type" : type_text,
        "press" : press_btn
        }


# section to replay actions
def pyag_mouse(position):
    x, y = position.split(",")
    pi.moveTo(int(x), int(y))

def pyag_click(button):
    pi.click(button=button)

def pyag_text(text):
    pi.write(text, interval=0.15)

def pyag_press(button):
    pi.press(button)

pyag_type = {
    "pos" : pyag_mouse,
    "click" : pyag_click,
    "type" : pyag_text,
    "press" : pyag_press
        }


# main functions
def capture_actions():
    tracked_actions = []

    action_with_arg = ["type", "press"]

    while True:
        get_action = input("define action: [position, right, left, type, press or break]\n")

        if get_action == "break":
            break

        try:
            if any(x in get_action for x in action_with_arg):
                input_action = input("type action: ")
                tracked_actions.append(action_type[get_action](input_action))
            else:
                tracked_actions.append(action_type[get_action]())
        except:
            print("invalid entry")
            continue

    return tracked_actions


def save_actions(actions, filename):
    with open(filename, "w") as outf:
        for i in actions:
            outf.write("{}\n".format(i))


def replay_action(log_action):
    print(log_action)
    type_action, action = log_action.split(":", 1)
    pyag_type[type_action](action.strip())




# main section
def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-t', '--type', required=True, dest='rtype', type=int, help='define type: 1=record new actions, 2=replay actions from file')
    parser.add_argument('-f', '--filename', dest='fname', default='_action-log.txt', help='filename, if not defined yyyymmdd_HHMM_action-log.txt')
    parser.add_argument('-i', '--num-iteration', dest='iter', type=int, default='0', help='number of time to loop actions. (default: 0 will not loop, but will print actions)')

    args = parser.parse_args()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")

    if args.fname == "_action-log.txt":
        filename = timestamp + args.fname

        # test working directory for log
        #workdir = "$HOME/logs/"
        #filename = workdir + filename
    else:
        filename = args.fname


    if args.rtype == 1:
        log_actions = capture_actions()
    elif args.rtype == 2:
        with open(filename, "r") as logfile:
            log_actions = logfile.readlines()

    if args.iter == 0:
        print([x.rstrip('\n') for x in log_actions])
        save_actions(log_actions, filename)
    else:
        for i in range(args.iter):
            for x in log_actions:
                replay_action(x.rstrip('\n'))


if __name__ == "__main__":
    main()


