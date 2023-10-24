import os

file1 = ""
path = "/index_files/1007751472.html"
p = os.getcwd()
p = p.replace('\\','/')
file1 = p + path

file2 = "index.html"

print(os.path.isfile(file1))

print(os.path.isfile("D:/things for university/yocket/Santa Clara/Course/COEN 317 distributed systems/PA-1-python/index_files/_livewhale_theme_global_styles_widgets.css"))