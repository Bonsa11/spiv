def parse_folder_path(fldr: str):
    if 'uhb/appdata' in fldr:
        if 'uhb/appdata/leicabs' in fldr:
            return fldr.replace('\\','/').replace(r'//uhb/appdata/leicabs','/mnt/uhb/appdata/leicabs')
        elif 'uhb/userdata/Pathology' in fldr:
            return fldr.replace('\\','/').replace(r'//uhb/userdata/Pathology','/mnt/uhb/userdata/Pathology')

    if '10.156.76.199' in fldr:
        return fldr.replace('\\','/').replace(r'//10.156.76.199/molecular_pathology_imaging','/mnt/molecular_pathology_imaging/')

    else:
        return fldr