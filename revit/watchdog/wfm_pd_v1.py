import getpass
import os
import time
import logging
from collections import namedtuple
from pathlib import Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath
from subprocess import PIPE, Popen
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer


logging.basicConfig(
    filename= r"C:\Users\Alex.Goldston\Desktop\development\python\bim mgmt\watchdog\log.txt",
    format= "%(asctime)s %(message)s",
    datefmt= "%m/%d/%Y %I:%M %p",
    level = logging.DEBUG,
)

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)

def sliceit(iterable, tup):
    return iterable[tup[0]:tup[1]].strip()

def convert_cat(line):
    Stat = namedtuple('Stat', 'date time directory size owner filename')
    stat_index = Stat(
        date=(0,11),
        time=(11,18),
        directory=(18,27),
        size=(27,35),
        owner=(35,59),
        filename=(59,-1))

    stat = Stat(date=sliceit(line, stat_index.date),
                    time=sliceit(line, stat_index.time),
                    directory=sliceit(line, stat_index.directory),
                    size=sliceit(line, stat_index.size),
                    owner=sliceit(line, stat_index.owner),
                    filename=sliceit(line, stat_index.filename))
    return stat

def stat(path):
    if not os.path.isdir(path):
        dirname, filename = os.path.split(path)
    else:
        dirname = path
    cmd = ["cmd", "/c", "dir", dirname, "/q"]
    session = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = session.communicate()[0].decode('cp437')

    if os.path.isdir(path):
        line = result.splitlines()[5]
        print(convert_cat(line))
        return convert_cat(line)
    else:
        for line in result.splitlines()[5:]:
            if filename in line:
                return convert_cat(line)
            else:
                raise Exception('Could not locate file')

def on_created(event):
    print(f"yo - {(os.path.abspath(event.src_path))} has been created")
    print(stat(path))
    path_string = str(os.path.abspath(event.src_path))
    logging.info('file created: ' + (path_string))

def on_deleted(event):
    print(f"what the BORK! someone deleted - {(os.path.abspath(event.src_path))}!")
    print(stat(path))
    path_string = str(os.path.abspath(event.src_path))
    logging.info('file created: ' + (path_string))

def on_modified(event):
    print(f"hey mate - {(os.path.abspath(event.src_path))} has been modified")
    print(stat(path))
    path_string = str(os.path.abspath(event.src_path))
    logging.info('file created: ' + (path_string))


def on_moved(event):
    print(f"ahoy, some muppet moved {(os.path.abspath(event.src_path))} to {(os.path.abspath(event.dest_path))}")
    print(stat(path))
    path_string = str(os.path.abspath(event.src_path))
    logging.info('file created: ' + (path_string))

def woof():
    return str("""\
             |\_/|                  
            | @ @   Woof! 
            |   <>              _  
            |  _/\------____ ((| |))
            |               `--' |   
        ____|_       ___|   |___.' 
        /_/_____/____/_______|
        """)

def welcome_user():
    user_name_input = getpass.getuser()
    print("________________________________________________________________")
    print("Hi %s, Welcome Fren." % user_name_input)
    print("\n")
    doggo = woof()
    print(doggo)
    print("________________________________________________________________")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

welcome_user()

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
