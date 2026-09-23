import json
import os

File_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(File_PATH):
        return []
    with open(File_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(File_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)