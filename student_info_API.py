import requests 

ucid = input("Enter your UCID: ")
first = input("Enter your first name: ")
last = input("Enter your last name: ")
github = input("Enter your github username: ")
discord = input("Enter your discord user name: ")
cartoon = input("Enter your favorite cartoon: ")
language = input("Enter your favorite language: ")
game = input("Enter your favorite movie, game or book: ")
section = input("Enter your section: ")

data = {
    "UCID": ucid,
    "first_name": first,
    "last_name": last,
    "github_username": github,
    "discord_username": discord,
    "favorite_cartoon": cartoon,
    "favorite_language": language,
    "movie_or_game_or_book": game,
    "section": section
}

status = {
    400: "Bad Request – check data format",
    403: "Forbidden",
    404: "Not Found - check API endpoint",
    500: "Server Error – try again later."
}

try:
    r = requests.post('https://student-info-api.netlify.app/.netlify/functions/submit_student_info', json = data)
    r.raise_for_status()
    print("Success:", r.status_code)
    print(r.json())
except requests.exceptions.HTTPError as e:
    code = e.response.status_code
    print("Error Code", code, status.get(code))
