from Constants import directories
from Constants.values import GENRES
from Util.files import getLyrics, create, partitionFiles
from lib.data import createLyricsObjects
from lib.ngrams import saveNgramDists, getFreqsByGenre, saveNGramDists

lyricsDir = directories.LYRIC_PATH
lyricsStore = directories.LYRICS_STORE
bigramTotality = directories.BIGRAMS_TOTALITY
trigramTotality = directories.TRIGRAMS_TOTALITY
bigramFreqs = directories.BIGRAMS_FREQS
trigramFreqs = directories.TRIGRAMS_FREQS
#bigramSongDict = directories.BIGRAMS_SONG_STORE
#trigramSongDict = directories.TRIGRAMS_SONG_STORE
#partitionFiles(lyricsDir, directories.PATH_TRAIN, directories.PATH_VAL, directories.PATH_TEST, directories.LOG_PATH)


for key in ['train', 'val', 'test']:
	create(lyricsStore[key])
	create(bigramTotality[key])
	create(trigramTotality[key])

for key in ['train', 'val', 'test']:
	#createLyricsObjects(lyricsDir[key], lyricsStore[key], bigramTotality[key], trigramTotality[key])
	saveNGramDists(lyricsStore[key], bigramTotality[key], trigramTotality[key])
	#getFreqsByGenre(lyricsStore[key], bigramTotality[key], trigramTotality[key], bigramFreqs[key], trigramFreqs[key])
