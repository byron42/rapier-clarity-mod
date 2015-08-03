import zipfile

zfile_1 = zipfile.ZipFile('Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/script.cu.lrclyrics-(1.0.7).zip')
zip_1_destination = 'Q://scripts/'

zfile_2 = zipfile.ZipFile('Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/script.module.chardet-2.1.2.zip')
zip_2_destination = 'Q://scripts/.modules'

zfile_1.extractall(zip_1_destination)
zfile_2.extractall(zip_2_destination)