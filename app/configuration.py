import os

host = "127.0.0.1"
port = 9006
hello_message = "Hello from door assistant"

log_file_name = "door_assistant.log"

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name