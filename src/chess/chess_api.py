# Chess.com API wrapper for MCP server
# This file provides helper functions to interact with the Chess.com public API.
import requests

CHESS_API_BASE = "https://api.chess.com/pub"
headers= {"accept": "application/json", 
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64: x64) Python/3.10.0 requests/2.31.1"} # headers for API requests

def get_player_profile(username):
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_player_stats(username):
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

