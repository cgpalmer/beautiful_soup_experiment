import os
var = "test"
newpath = rf'file_outputs/{var}'
if not os.path.exists(newpath):
    os.makedirs(newpath)

