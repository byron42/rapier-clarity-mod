import zipfile

zfile_1 = zipfile.ZipFile('Q://skin/rapier-clarity-mod/scripts/Rom Collection Browser/ElementTree_Install/script.module.elementtree-1.2.8.zip')
zip_1_destination = 'Q://scripts/.modules/'

zfile_2 = zipfile.ZipFile('Q://skin/rapier-clarity-mod/scripts/Rom Collection Browser/ElementTree_Install/RCB_Check.zip')
zip_2_destination = 'Q://scripts/'

zfile_1.extractall(zip_1_destination)
zfile_2.extractall(zip_2_destination)

xbmc.executebuiltin('XBMC.RunScript(special://skin/scripts/Rom Collection Browser/default.py)')
