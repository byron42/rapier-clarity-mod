import shutil
 
new_HomeNoCustom = 'Q://skin/rapier-clarity-mod/scripts/HomeCustomSettings/HomeNoCustom/Home.xml'
old_Home = 'Q://skin/rapier-clarity-mod/720p/Home.xml'

######################################################################################
##############################  REPLACE FILES  #######################################
######################################################################################

shutil.copyfile(new_HomeNoCustom,old_Home)