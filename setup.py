import tarfile
  
# open file
file = tarfile.open('vectoriser.tar.gz')
  
# extracting file
file.extractall('./')
  
file.close()
