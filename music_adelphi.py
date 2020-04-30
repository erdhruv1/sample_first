class Track:

    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre


class Album:

    def __init__(self, trackObj):
        self.album_dict = {}

        self.album_dict[trackObj.title] = trackObj


class Artist:

    def __init__(self, album, albumObj):
        self.artist_dict = {}

        self.artist_dict[album] = albumObj

def main():
    numberOfTracks = []
    numberOfAlbums = []

    uniqueTracks = {}
    uniqueAlbums = {}
    uniqueArtist  = {}

    with open('music.csv', mode='r', encoding='utf-8') as myFile:
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
            albumObj  = Album(trackObj)
            artistObj = Artist(album, albumObj)

            uniqueArtist[artist] = artistObj

            #Count
            numberOfTracks.append(albumObj.album_dict)
            numberOfAlbums.append(artistObj.artist_dict)


    #Remove Duplicates
    for i in numberOfTracks:
        uniqueTracks[list(i.keys())[0]] = list(i.values())[0]

    for j in numberOfAlbums:
        uniqueAlbums[list(j.keys())[0]] = list(j.values())[0]

    print("Tracks: {0}".format(len(uniqueTracks)))
    print("Albums: {0}".format(len(uniqueAlbums)))
    print("Artist: {0}".format(len(uniqueArtist)))



if __name__ == '__main__':
    main()