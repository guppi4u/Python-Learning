"""
ALGO
1. Create playlist class
2. Add songs 
3. Remove songs 
4. Show songs 

"""

class Playlist:

    def __init__(self,name): # constructor
        self.name = name
        self.songs=[] # initalizing empty list 

    def add_song(self,song):
        self.songs.append(song)
        print(f'Song added !!')

    def remove_song(self,song):
        try:
            self.songs.remove(song)
            print('Song Removed !!!')
        except ValueError:
            print('Song is not present in the list')


    def show_songs(self):
        for song in self.songs:
            print( f'---{song}')        



if __name__ =='__main__':
    my_playlist =Playlist('Favorites')
    my_playlist.add_song('Madona')
    my_playlist.add_song('Usher')
    my_playlist.add_song('Jackson')
    my_playlist.add_song('David')
    my_playlist.add_song('Peter')

    my_playlist.show_songs() # just call method , dont put it print, else it will print None

    my_playlist.remove_song('Good')
    


            


    


        