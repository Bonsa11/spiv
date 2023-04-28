def parse_folder_path(fldr: str):
    pfldr = fldr.replace('\\','/')
    if 'uhb/appdata' in pfldr:
        if 'uhb/appdata/leicabs' in pfldr:
            return pfldr.replace(r'//uhb/appdata/leicabs','/mnt/uhb/appdata/leicabs')
        elif 'uhb/userdata/Pathology' in pfldr:
            return pfldr.replace(r'//uhb/userdata/Pathology','/mnt/uhb/userdata/Pathology')

    if '10.156.76.199' in pfldr:
        return pfldr.replace(r'//10.156.76.199/molecular_pathology_imaging','/mnt/molecular_pathology_imaging/')

    else:
        return fldr