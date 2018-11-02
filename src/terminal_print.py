import sys
import time

animation_frames = "|/-\\"

def print_itteration_status(msg, current, max):
  line = "[{}] {}/{}".format(msg, current, max)
  print_dynamic_line(line)

def print_progress_bar(msg, current, max):
  percentage = (current+1) * 100 / max
  line = "[{}] {}%".format(msg, int(percentage))
  print_dynamic_line(line)

def print_dynamic_line(line):
  sys.stdout.write("\r{0}".format(line))
  sys.stdout.flush()