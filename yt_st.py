import streamlit as st
import requests

url = st.text_input("Enter the video URL you wish to extract a thumbnail from.")
slug = 'https://www.youtube.com/watch?v='

extract = st.button('Extract thumbnail')

if extract:

	if slug in url:
	  match = url.replace(slug, '')

	thumb = 'https://img.youtube.com/vi/' + match + '/maxresdefault.jpg'
	thumb_hq = 'https://img.youtube.com/vi/' + match + '/hqdefault.jpg'

	if requests.get(thumb).status_code == 404:
		st.image(thumb_hq)
	else:
		st.image(thumb)
