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

    # torrents.info(torrentId='258188')

    data = cli.search(search, category=category, sortBy=sort, order=order)

    if data['itemCount'] == 0:
        input(f'No results about "{search}" found. Did you select the right category or entered the correct search term? Press enter to continue...')
        clearscr()
        main()

    for items in data['items']:
        # name = items['name']
        torrentid = items['torrentId']
        link = items['link']
        # seeders = items['seeders']
        # leechers = items['leechers']
        # size = items['size']
        # uploaded_at = items['time']
        # uploader = items['uploader']

        torrentdata = cli.info(torrentId=torrentid)

        clearscr()

        if torrentdata['genre'] != None:
            srchgenre = str(', '.join(torrentdata['genre']).replace('\n', '').replace(' ,', ','))

        elif torrentdata['genre'] == None:
            srchgenre = 'Unknown'

        askaction = input(f'Press enter for next result, e to exit or b to go back\n\n{torrentdata["name"]} uploaded by {torrentdata["uploader"]} ({torrentdata["uploaderLink"]}) at {torrentdata["uploadDate"]}\n{torrentdata["description"]}\n -- Size/Resolution: {torrentdata["size"]}/{torrentdata["type"]}\n -- Seeders/Leechers: {torrentdata["seeders"]}/{torrentdata["leechers"]}\n -- Magnet link: {torrentdata["magnetLink"]}\n -- Torrent link: {link}\n -- Infohash: {torrentdata["infoHash"]}\n -- Total downloads: {torrentdata["downloads"]}\n -- Genre: {srchgenre}\n\n --> ')

        if askaction.lower() == 'b':
            main()

        elif askaction.lower() == 'e':
            clearscr()
            exit()
"""
{'category': 'Movies',
 'description': 'Shang-Chi must confront the past he thought he left behind '
                'when he is drawn into the web of the mysterious Ten Rings '
                'organization.',
 'downloads': '83318',
 'genre': ['\nAction ', '\nAdventure ', '\nFantasy '],
 'images': ['https://checkmy.pictures/images/2021/11/09/12001564092508286891.th.jpg',
            'https://checkmy.pictures/images/2021/11/09/31204948271153801563.th.jpg',
            'https://checkmy.pictures/images/2021/11/09/92562990005263661478.th.jpg'],
 'infoHash': '8B6E306C2106794C47EA4C26811DDEEF9FCDC071',
 'language': 'English',
 'lastChecked': "Nov. 13th '21",
 'leechers': '2954',
 'magnetLink': 'magnet:?xt=urn:btih:8B6E306C2106794C47EA4C26811DDEEF9FCDC071&dn=Shang-Chi.And.The.Legend.Of.The.Ten.Rings.2021.1080p.BluRay.H264.AAC&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2720%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2760%2Fannounce&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12750%2Fannounce&tr=udp%3A%2F%2Ftracker.slowcheetah.org%3A14790%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce',
 'name': 'Shang-Chi.And.The.Legend.Of.The.Ten.Rings.2021.1080p.BluRay.H264.AAC',
 'seeders': '8963',
 'shortName': '\n\nShang-Chi and the Legend of the Ten... \n',
 'size': '2.5 GB',
 'thumbnail': 'https://www.1377x.to/img/movie/Shang-Chi-and-the-Legend-of-the-Ten-Rings-2021.jpg',
 'type': 'HD',
 'uploadDate': "Nov. 10th '21",
 'uploader': 'TheMorozko',
 'uploaderLink': 'https://www.1377x.to/TheMorozko/'}
 """

        # print(f'{name} uploaded by {uploader} ({size})\nLink: {link}\nSeeders/leechers: {seeders}/{leechers}\nTorrent ID: {torrentid}\nUploaded at: {uploaded_at}\n-----------------------------------------')

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