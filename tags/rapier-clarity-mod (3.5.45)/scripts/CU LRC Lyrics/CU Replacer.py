import shutil
# import os
 
new_settings = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/settings.xml'
old_settings = 'Q://scripts/CU LRC Lyrics/resources/settings.xml'

new_musicOSD = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/MusicOSD.xml'
old_musicOSD = 'Q://skin/rapier-clarity-mod/720p/MusicOSD.xml'

# ===================================================================================
# SCRAPERS
# ===================================================================================
# alsong
new_ASscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/alsong/lyricsScraper.py'
old_ASscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/alsong/lyricsScraper.py'
# baidu
new_BDscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/baidu/lyricsScraper.py'
old_BDscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/baidu/lyricsScraper.py'
# darklyrics
# new_DLscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/darklyrics/lyricsScraper.py'
# old_DLscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/darklyrics/lyricsScraper.py'
# gomaudio
new_GMscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/gomaudio/lyricsScraper.py'
old_GMscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/gomaudio/lyricsScraper.py'
# lyrdb
new_LDBscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/lyrdb/lyricsScraper.py'
old_LDBscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/lyrdb/lyricsScraper.py'
# lyricsmode
new_LMscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/lyricsmode/lyricsScraper.py'
old_LMscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/lyricsmode/lyricsScraper.py'
# lyricstime
new_LTscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/lyricstime/lyricsScraper.py'
old_LTscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/lyricstime/lyricsScraper.py'
# lyricwiki
new_LWscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/lyricwiki/lyricsScraper.py'
old_LWscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/lyricwiki/lyricsScraper.py'
# minilyrics
new_MLscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/minilyrics/lyricsScraper.py'
old_MLscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/minilyrics/lyricsScraper.py'
# ttplayer
new_TTscraper = 'Q://skin/rapier-clarity-mod/scripts/CU LRC Lyrics/culrcscrapers/ttplayer/lyricsScraper.py'
old_TTscraper = 'Q://scripts/CU LRC Lyrics/resources/lib/culrcscrapers/ttplayer/lyricsScraper.py'


######################################################################################
##############################  REPLACE FILES  #######################################
######################################################################################

shutil.copyfile(new_settings,old_settings)
#******************************************************* SCRAPERS ********************
shutil.copyfile(new_ASscraper,old_ASscraper)
shutil.copyfile(new_BDscraper,old_BDscraper)
# shutil.copyfile(new_DLscraper,old_DLscraper)
shutil.copyfile(new_GMscraper,old_GMscraper)
shutil.copyfile(new_LDBscraper,old_LDBscraper)
shutil.copyfile(new_LMscraper,old_LMscraper)
shutil.copyfile(new_LTscraper,old_LTscraper)
shutil.copyfile(new_LWscraper,old_LWscraper)
shutil.copyfile(new_MLscraper,old_MLscraper)
shutil.copyfile(new_TTscraper,old_TTscraper)
#*************************************************************************************
shutil.copyfile(new_musicOSD,old_musicOSD)

# RUN CU.LRC.LYRICS!!!
xbmc.executebuiltin('XBMC.RunScript(Q:\scripts\CU LRC Lyrics\default.py)')