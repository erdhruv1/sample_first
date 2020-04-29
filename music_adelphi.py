class Track:

    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre


class Album:

    def __init__(self, trackObjList):
        self.album_dict = {}

        for obj in trackObjList:
            self.album_dict[obj.title] = obj


class Artist:

    def __init__(self, uniqueAlbums, albumObj):
        self.artist_dict = {}

        self.artist_dict[albumName] = albumObj

def main():
    trackObjList = []
    albumList = []

    artist_dict = {}

    with open('music.csv', mode='r') as myFile:
        line = myFile.readlines()

        for i in line:
            myLine = i.strip()
            musicList = myLine.split(',')

            title    = musicList[0]
            duration = musicList[1]
            artist   = musicList[2]
            album    = musicList[3]
            genre    = musicList[4]

            trackObj  = Track(title, duration, genre)
            trackObjList.append(trackObj)
            albumList.append(album)

        albumObj = Album(trackObjList)

        unique_albums = dict(zip(albumList, albumObj.album_dict)).keys()
        artistObj = Artist(unique_albums, albumObj)

        # artist_dict[artist] = artistObj
        #
        # print("Artists: {0}".format(len(artist_dict)))
        # print("Albums: {0}".format(len(albumDict)))
        # print("Tracks: {0}".format(len(trackDict)))



if __name__ == '__main__':
    main()