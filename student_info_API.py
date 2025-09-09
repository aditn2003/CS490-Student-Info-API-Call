import requests 

ucid = input("Enter your UCID:")
first = input("Enter your first name:")
last = input("Enter your last name:")
github = input("Enter your github username:")
discord = input("Enter your discord user name:")
cartoon = input("Enter your favorite cartoon:")
language = input("Enter your favorite language:")
game = input("Enter your favorite movie, game or book:")
section = input("Enter your section:")

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

r = requests.post('https://httpbin.org/post', json = data)

print(r.status_code)
print(r.text)
