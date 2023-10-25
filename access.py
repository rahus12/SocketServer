import os
print(os.access("./index_files/scu.css",os.F_OK))
print(os.access("./index_files/scwu.css",os.R_OK))