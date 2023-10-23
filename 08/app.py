import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
import urllib
import base64

EXCLUDED_FILES = ['app.py', 'requirements.txt', 'pre-requirements.txt', 'packages.txt', 'README.md','.gitattributes', "backup.py","Dockerfile"]

def download_file(url, local_filename):
    if url.startswith('http://') or url.startswith('https://'):
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)
            return local_filename
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")

def download_html_and_files(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')

    base_url = urllib.parse.urlunparse(urllib.parse.urlparse(url)._replace(path='', params='', query='', fragment=''))

    for link in soup.find_all('a'):
        file_url = urllib.parse.urljoin(base_url, link.get('href'))
        local_filename = urllib.parse.urlparse(file_url).path.split('/')[-1]
        if local_filename:
            link['href'] = local_filename
            download_file(file_url, local_filename)
    
    with open("index.html", "w") as file:
        file.write(str(soup))

def list_files(directory_path='.'):
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return [f for f in files if f not in EXCLUDED_FILES]

def get_download_link(file):
    with open(file, "rb") as f:
        bytes = f.read()
        b64 = base64.b64encode(bytes).decode()
        href = f'<a href="data:file/octet-stream;base64,{b64}" download=\'{file}\'>Click to download {file}</a>'
    return href

def show_download_links():
    st.sidebar.write('Here are the files you can download:')
    for file in list_files():
        st.sidebar.markdown(get_download_link(file), unsafe_allow_html=True)

def main():
    st.sidebar.title('Bulk Download Tool')
    url = st.sidebar.text_input('Please enter a URL to bulk download text and files')
    if st.sidebar.button('📥 Get All the Content'):
        download_html_and_files(url)
        show_download_links()
    if st.sidebar.button('📂 Show Download Links'):
        show_download_links()

if __name__ == "__main__":
    main()
