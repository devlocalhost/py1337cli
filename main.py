#!/usr/bin/python3

from py1337x import py1337x
from pprint import pprint
from platform import system as sysname
from os import system
from sys import exit

# ALT_DOMAINS = ['1337x.to', '1337x.tw', '1377x.to', '1337xx.to', '1337x.st', 'x1337x.ws', 'x1337x.eu', 'x1337x.se', '1337x.is', '1337x.gd']

CLEARCMD = None # set to pass to ignore and not clear the terminal

def clearscr():
    if CLEARCMD != None:
        system(CLEARCMD)

    elif CLEARCMD == 'pass':
        pass

    elif CLEARCMD == None:
        if sysname() == 'Windows':
            system('cls')

        elif sysname() == 'Linux' or sysname() == 'Darwin':
            system('clear')

        else:
            print(f'Clear command not defined!')

def getinfo(search, category, sort, order):
    cli = py1337x()
    data = cli.search(search, category=category, sortBy=sort, order=order)

    if data['itemCount'] == 0:
        input(f'No results about "{search}" found. Did you select the right category or entered the correct search term? Press enter to continue...')
        clearscr()
        main()

    for items in data['items']:
        name = items['name']
        torrentid = items['torrentId']
        link = items['link']
        seeders = items['seeders']
        leechers = items['leechers']
        size = items['size']
        uploaded_at = items['time']
        uploader = items['uploader']

        print(f'{name} uploaded by {uploader} ({size})\nLink: {link}\nSeeders/leechers: {seeders}/{leechers}\nTorrent ID: {torrentid}\nUploaded at: {uploaded_at}\n-----------------------------------------')
        print(items)
def main():
    clearscr()

    action = int(input('I want to search for... (0 to exit)\n     1) Movies\n     2) TV\n     3) Games\n     4) Music\n     5) Apps\n     6) Anime\n     7) Documentaries\n --> '))

    if action == 1:
        clearscr()

        movie = input('[Movies] I want to search for... (b to go back)\n --> ')

        if movie.lower() == 'b':
            clearscr()
            main()

        getinfo(movie, 'movies', 'seeders', 'desc')
        
    elif action == 2:
        clearscr()

        tv = input('[TV] I want to search for... (b to go back)\n --> ')

        if tv.lower() == 'b':
            clearscr()
            main()

        getinfo(tv, 'tv', 'seeders', 'desc')

    elif action == 3:
        clearscr()

        game = input('[Games] I want to search for... (b to go back)\n --> ')

        if game.lower() == 'b':
            clearscr()
            main()

        getinfo(game, 'games', 'seeders', 'desc')

    elif action == 4:
        clearscr()

        music = input('[Music] I want to search for... (b to go back)\n --> ')

        if music.lower() == 'b':
            clearscr()
            main()

        getinfo(music, 'music', 'seeders', 'desc')

    elif action == 5:
        clearscr()

        app = input('[Apps] I want to search for... (b to go back)\n --> ')

        if app.lower() == 'b':
            clearscr()
            main()

        getinfo(app, 'apps', 'seeders', 'desc')

    elif action == 6:
        clearscr()

        anime = input('[Anime] I want to search for... (b to go back)\n --> ')

        if anime.lower() == 'b':
            clearscr()
            main()

        getinfo(anime, 'anime', 'seeders', 'desc')

    elif action == 7:
        clearscr()

        documentary = input('[Documentaries] I want to search for... (b to go back)\n --> ')

        if documentary.lower() == 'b':
            clearscr()
            main()

        getinfo(documentary, 'documentaries', 'seeders', 'desc')

    elif action == 0:
        clearscr()
        exit()

main()