import json
import os
import sys

APP_NAME = "To Do by ksh"

def get_data_dir():
    appdata = os.getenv("APPDATA")
    data_dir = os.path.join(appdata, APP_NAME)
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

FILE_PATH = os.path.join(get_data_dir(), "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)
