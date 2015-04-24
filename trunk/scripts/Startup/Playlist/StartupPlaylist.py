import shutil
 
new_StartUp = 'Q://skin/rapier-clarity-mod/scripts/Startup/Playlist/Startup.xml'
old_StartUp = 'Q://skin/rapier-clarity-mod/720p/Startup.xml'

new_sounds = 'Q://skin/rapier-clarity-mod/scripts/Startup/Playlist/sounds.xml'
old_sounds = 'Q://skin/rapier-clarity-mod/sounds/sounds.xml'

######################################################################################
##############################  REPLACE FILES  #######################################
######################################################################################

shutil.copyfile(new_StartUp,old_StartUp)
shutil.copyfile(new_sounds,old_sounds)
