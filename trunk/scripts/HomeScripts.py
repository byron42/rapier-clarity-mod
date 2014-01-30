# HomeScripts script by Wyrm (xTV-SAF) #
# Prompt user for name of script and output skin strings #
# containing required info to run script from the home screen #

# main import's
import xbmc,xbmcgui
import fileinput,os,sys,re,string

SCRIPTDIR = 'special://xbmc/scripts'

def getscriptname():
	# Get the directory contents and put them in **ScriptList**
	ScriptList = os.listdir(SCRIPTDIR)
	
	# Prompt User for script name
	dialog = xbmcgui.Dialog()
	Listnum = dialog.select(xbmc.getLocalizedString(31444), ScriptList)
	try:
		ScriptName = ScriptList [Listnum]
		
	except IndexError:
		sys.exit(2)
	else:
		return ScriptName

def main():
	SkinStringName = string.replace(str(sys.argv[1:]),"'","")
	SkinStringName = string.replace(SkinStringName,"[","")
	SkinStringName = string.replace(SkinStringName,"]","")

	ScriptName = getscriptname()
	
	ScriptDirectory = os.path.join(SCRIPTDIR, ScriptName)
	ScriptIconTBN = os.path.join(ScriptDirectory,"default.tbn")
	ScriptIconPNG = os.path.join(ScriptDirectory,"default.png")
	ScriptLocation = os.path.join(ScriptDirectory,"default.py")
	
	if os.path.isfile( ScriptIconTBN ):
		xbmc.executebuiltin("XBMC.Skin.SetString(" + SkinStringName + "-scripticon," + ScriptIconTBN + ")")
	elif os.path.isfile ( ScriptIconPNG ):
		xbmc.executebuiltin("XBMC.Skin.SetString(" + SkinStringName + "-scripticon," + ScriptIconPNG + ")")

	# Write out Skin strings with script info
	xbmc.executebuiltin("XBMC.Skin.SetString(" + SkinStringName + "-scriptloc," + ScriptLocation + ")")
	xbmc.executebuiltin("XBMC.Skin.SetString(" + SkinStringName + "-scriptlabel," + ScriptName + ")")
	
	# Reset homescript skin strings
	xbmc.executebuiltin("XBMC.Skin.Reset(" + SkinStringName + "-pluginfolder)")
	xbmc.executebuiltin("XBMC.Skin.Reset(" + SkinStringName + "-pluginwindow)")
	xbmc.executebuiltin("XBMC.Skin.Reset(" + SkinStringName + "-pluginname)")

if __name__ == '__main__':
	main()	

