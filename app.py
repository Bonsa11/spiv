import streamlit as st
from PIL import Image
import os

from openslide import open_slide

from utils import parse_folder_path

with st.sidebar:
    st.image('./Resources/logo.png')
    st.title('Sams Pathology Image Viewer')
    st.subheader("it's bad, but it works!")
    pages = ['Viewer',
             'Docs']
    choice = st.radio("Navigation", pages)
    st.warning("This tool is still in development, contact me @ samuel.bodza2@uhb.nhs.uk for feature requests, "
               "bugs or issues!")

if choice == "Viewer":
    st.title("Image Viewer")
    st.subheader("A place to view the basics of pathology images without needing extra software, for supported types "
                 "see the docs")

    fldr = st.text_input("Add the path to folder with your images in here. \n\n This does have to be a network path "
                         "that is accessible for a server")
    if fldr:
        fldr = parse_folder_path(fldr)
        if not os.path.exists(fldr):
            st.error('Path to folder doesnt exist, try another one')
        else:
            file = st.selectbox("Choose the image to view", [f for f in os.listdir(fldr)])
            file_path = os.path.join(fldr, file)
            ext = file.split('.')[-1].lower()

            # clear cache if too full
            if len(os.listdir('./Cache')) > 4:
                for f in os.listdir('./Cache'):
                    os.remove(os.path.join('./Cache', f))

            if ext == 'ndpi':
                slide = open_slide(file_path)
                region = (0, 0)
                level = st.slider(label='Choose the level of image. the smaller the value, the higher the resolution',
                                  min_value=0,
                                  max_value=slide.level_count - 1,
                                  value=slide.level_count - 3)
                size = slide.level_dimensions[level]
                st.text(f"Image is size: {size[0]} x {size[1]}")
                if size[0] * size[1] >= 178956970:
                    st.error('This level is too large and will error if attempted to be loaded')
                else:
                    if level <= 5:
                        st.warning('Bigger images will take longer to load, we recommend starting high and moving down if '
                                   'you need to')
                    load_metadata = st.checkbox('Get Metadata', value=False)
                    if st.button('Load this image!'):
                        with st.spinner("Loading..."):
                            img = slide.read_region(region, level, size)
                            tmp_path = os.path.join("./Cache", f"{file.split('.')[0]}_level_{level}.tif")
                            if not os.path.exists(tmp_path):
                                img.save(tmp_path)
                            try:
                                im = Image.open(tmp_path)
                                st.image(im, caption=f'{file}')
                            except Image.DecompressionBombError as img2big:
                                st.error('Image at this level is too big to load! increase the level and try again')
                                os.remove(tmp_path)
                            if load_metadata:
                                metadata = dict(slide.properties)
                                metadata_as_str = '\n'.join([f'{key} : {metadata[key]}' for key in metadata])
                                st.text(metadata_as_str)

            elif ext in ['tif', 'jpg', 'png', 'jpeg']:
                if st.button('Load this image!'):
                    with st.spinner("Loading..."):
                        im = Image.open(file_path)
                    st.image(im, caption=f'{file}')

            else:
                st.error("This file type is not supported yet, drop me an email and I'll add it")

elif choice == "Docs":
    st.title("Documentation")
    st.subheader("A place to find all the documentation for this tool, and some documentation for the surrounding "
                 "image types")
    st.text('I will 100% remember to do this')
