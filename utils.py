def parse_folder_path(fldr: str):
    if 'uhb/appdata/leicabs' in fldr:
        return fldr.replace('\\','/').replace(r'//uhb/appdata/leicabs','/mnt/uhb/')

    if '10.156.76.199' in fldr:
        return fldr.replace('\\','/').replace(r'//10.156.76.199/molecular_pathology_imaging','/mnt/molecular_pathology_imaging/')
