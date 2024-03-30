""" This file contains all the HTML / CSS strings for the different card types """
import os


def file_to_string(path):
    """Returns the content of a file as a string"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def path_relative_to_this_file(path):
    """Returns the absolute path of a file relative to this file"""
    return os.path.join(os.path.dirname(__file__), path)


def read_file(path):
    return file_to_string(path_relative_to_this_file(path))


HTMLforEditor = read_file("js/HTMLforEditor.js")

script_base = read_file("html/script_base.html")
script_cloze = read_file("html/script_cloze.html")

front = read_file("html/front.html") + script_base
back = read_file("html/back.html") + script_base

front_cloze = read_file("html/front_cloze.html") + script_cloze
back_cloze = read_file("html/back_cloze.html") + script_cloze

css = read_file("css/style_import.css")
