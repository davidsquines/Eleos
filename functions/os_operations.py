import os
import subprocess as sp

paths = {
    'spotify': "C:\\users\\user1\\appdata\\roaming\\spotify\\spotify.exe",
    'vs-code': "C:\\Users\\User1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'valorant' : "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
}

def open_spotify():
    sp.Popen(paths['spotify'])

def open_vs_code():
    sp.Popen(paths['vs-code'])

def open_valorant():
    sp.Popen(paths['valorant'])





