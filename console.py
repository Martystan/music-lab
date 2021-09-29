import pdb
from models.album import Album

from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()



artist1 = Artist("The Beatles")
artist_repository.save(artist1)

artist2 = Artist("Elvis Presley")
artist_repository.save(artist2)

album1 = Album("The White Album", "rock", artist1)
album_repository.save(album1)







pdb.set_trace()