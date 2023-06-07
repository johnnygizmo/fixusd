# Fix Imported USD Materials' UVMaps Name from AmbientCG

After importing a USD material file from AmbientCG the UVMap is named "st".
This script goes over every material in your file and renames any UVMap node that references 'st' to 'UVMap'
