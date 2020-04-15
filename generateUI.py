import subprocess
import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))


os.chdir(dir_path)
ui_files_list = glob.glob("*.ui")

for file in ui_files_list:
    ui_source = os.path.join(dir_path, file)
    ui_target = os.path.join(dir_path, file.replace('.ui','.py'))
    subprocess.run('pyuic5 '+ ui_source +' -o ' + ui_target)
    
print('Done')
