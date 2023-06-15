def parse_folder_path(fldr: str):
    pfldr = fldr.replace('\\','/')

    if 'uhb' in pfldr:
        return pfldr.replace(r'uhb','/mnt/uhb')
    
    else:
        return fldr
