import shutil
 
new_HomeOriginal = 'Q://skin/rapier-clarity-mod/scripts/HomeCustomSettings/HomeNormal/Home.xml'
old_HomeOriginal = 'Q://skin/rapier-clarity-mod/720p/Home.xml'

######################################################################################
##############################  REPLACE FILES  #######################################
######################################################################################

shutil.copyfile(new_HomeOriginal ,old_HomeOriginal)