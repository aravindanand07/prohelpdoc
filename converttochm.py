import os
import chm

hhp_file = r"D:\a\prohelpdoc\prohelpdoc\build\htmlhelp\VCollabPro.hhp"
chm_file = r"D:\a\prohelpdoc\prohelpdoc\build\htmlhelp\VCollabPro.chm"

if os.path.exists(hhp_file):
    with open(hhp_file, 'r') as project_file:
        project_content = project_file.read()

    chm.create(hhp_file, chm_file, project_content)
    print(f"{chm_file} created successfully!")
else:
    print("HHP file not found!")
