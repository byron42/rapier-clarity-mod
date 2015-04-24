# for downloading the zip
import urllib
# for extracting it
import zipfile  

  

url      ='https://www.dropbox.com/s/gqcywo6r68b57zb/rapier-clarity-mod%20%283.5.4%29.zip?dl=1'
filename ='E://rapier-clarity-mod.zip'

# get latest build ZIP
urllib.urlretrieve(url, filename)


# extract it
zip = zipfile.ZipFile(r'E://rapier-clarity-mod.zip')  
zip.extractall(r'E://RAPIER')