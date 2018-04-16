from pytube import Playlist

pl = Playlist("https://www.youtube.com/watch?v=CaCcOwJPytQ&list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT")
pl.download_all()
