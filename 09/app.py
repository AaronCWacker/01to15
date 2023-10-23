import streamlit as st
import json

urls = [
    "https://huggingface.co/spaces/awacke1/CB-GR-Chatbot-Blenderbot",
    "https://huggingface.co/spaces/awacke1/TTS-STT-Blocks",
    "https://huggingface.co/spaces/awacke1/Prompt-Refinery-Text-to-Image-Generation",
    "https://huggingface.co/spaces/awacke1/Video-Summary",
    "https://huggingface.co/spaces/awacke1/AI-MovieMaker-Comedy",
    "https://huggingface.co/spaces/awacke1/ChatGPT-Memory-Chat-Story-Generator",
    "https://huggingface.co/spaces/awacke1/CloneAnyVoice",
    "https://huggingface.co/spaces/awacke1/ChatGPT-Streamlit-2",
    "https://huggingface.co/spaces/awacke1/WikipediaUltimateAISearch",
    "https://huggingface.co/spaces/awacke1/RLHF.Cognitive.Episodic.Semantic.Memory",
    "https://huggingface.co/spaces/awacke1/Memory-Shared",
    "https://huggingface.co/spaces/awacke1/VideoSwap",
    "https://huggingface.co/spaces/awacke1/AI-Wikipedia-Search",
    "https://huggingface.co/spaces/awacke1/AutoMLUsingStreamlit-Plotly",
    "https://huggingface.co/spaces/awacke1/NLP-Lyric-Chorus-Image",
    "https://huggingface.co/spaces/awacke1/OpenAssistant-Chatbot-FTW-Open-Source",
    "https://huggingface.co/spaces/awacke1/ChatGPTStreamlit7",
    "https://huggingface.co/spaces/awacke1/MultiPDF-QA-ChatGPT-Langchain",
    "https://huggingface.co/spaces/awacke1/SOTA-Plan",
    "https://huggingface.co/spaces/awacke1/AIandSmartTools",
    "https://huggingface.co/spaces/awacke1/3DVirtualFood",
    "https://huggingface.co/spaces/awacke1/Gradio-Gallery-Health-Medical-Icon-Sets",
    "https://huggingface.co/spaces/awacke1/DatasetAnalyzer",
    "https://huggingface.co/spaces/awacke1/PrompTart",
    "https://huggingface.co/spaces/awacke1/sileod-deberta-v3-base-tasksource-nli",
    "https://huggingface.co/spaces/awacke1/File-Memory-Operations-Human-Feedback-Gradio",
    "https://huggingface.co/spaces/awacke1/Bloom.Big.Science.Continual.Generator",
    "https://huggingface.co/spaces/awacke1/Ontology-Gradio",
    "https://huggingface.co/spaces/awacke1/HTML5-Aframe-3dMap-Flight",
    "https://huggingface.co/spaces/awacke1/Bloom.Generative.Writer",
    "https://huggingface.co/spaces/awacke1/Voice-ChatGPT-Streamlit-12",
    "https://huggingface.co/spaces/awacke1/HTML5-AR-VR",
    "https://huggingface.co/spaces/awacke1/AnimationAI",
    "https://huggingface.co/spaces/awacke1/GenerativeWordsandImages",
    "https://huggingface.co/spaces/awacke1/AR-VR-IOT-Demo",
    "https://huggingface.co/spaces/awacke1/ArtStyleFoodsandNutrition",
    "https://huggingface.co/spaces/awacke1/CarePlanQnAWithContext",
    "https://huggingface.co/spaces/awacke1/VideoSummaryYoutube3",
    "https://huggingface.co/spaces/awacke1/AW-01ST-CSV-Dataset-Analyzer",
    "https://huggingface.co/spaces/awacke1/Try.Playing.Learning.Sharing.On.This",
    "https://huggingface.co/spaces/awacke1/google-flan-t5-base",
    "https://huggingface.co/spaces/awacke1/PubMed-Parrot-Paraphraser-on-T5",
    "https://huggingface.co/spaces/awacke1/Writing-Grammar-And-Paraphrase-w-Pegasus",
    "https://huggingface.co/spaces/awacke1/runwayml-stable-diffusion-v1-5",
    "https://huggingface.co/spaces/awacke1/DockerGoFlanT5",
    "https://huggingface.co/spaces/awacke1/GradioContinualGenerator",
    "https://huggingface.co/spaces/awacke1/StreamlitSuperPowerCheatSheet"
]

# Extract the last part of each URL (after the last '/') to serve as the name of the button
url_names = [url.split('/')[-1] for url in urls]

# Associate each URL with a relevant emoji based on keywords in its name
emoji_mapping = {
    "Chatbot": "🤖",
    "TTS": "🗣️",
    "STT": "👂",
    "Video": "🎥",
    "MovieMaker": "🍿",
    "ChatGPT": "💬",
    "Voice": "🎙️",
    "Wikipedia": "📖",
    "Memory": "🧠",
    "AI": "🧠",
    "OpenAssistant": "🤝",
    "3D": "🕶️",
    "AR": "👓",
    "VR": "🕶️",
    "Animation": "🖌️",
    "Dataset": "📊",
    "Gradio": "📻",
    "HTML5": "🌐",
    "Writing": "✍️",
    "Grammar": "🖋️",
    "Paraphrase": "🔄",
    "Streamlit": "🌠"
}

# Map each URL name to its most relevant emoji
url_emojis = []
for name in url_names:
    associated_emoji = "🔗"  # Default emoji
    for keyword, emoji in emoji_mapping.items():
        if keyword in name:
            associated_emoji = emoji
            break
    url_emojis.append(associated_emoji)

#url_emojis[:5], url_names[:5]  # Display the first 5 URL names with their associated emojis

import streamlit as st
import json
import webbrowser

# Function to load the history of clicks from the text file
def load_history():
    try:
        with open("click_history.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {url: 0 for url in urls}

# Function to save the updated history of clicks to the text file
def save_history(history):
    with open("click_history.txt", "w") as f:
        json.dump(history, f)

# Load the history of clicks
history = load_history()

# Display the buttons for each URL
for url, name, emoji in zip(urls, url_names, url_emojis):
    if st.button(f"{emoji} {name}"):
        # Open the URL in a new browser tab using JavaScript
        st.write('<script>window.open("'+url+'", "_blank");</script>', unsafe_allow_html=True)
        # Update the history of clicks
        history[url] += 1
        save_history(history)
    # Display the number of times the URL was opened below its corresponding button
    st.write(f"Clicked: {history[url]} times")

import time
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# ... [rest of the initial code remains unchanged] ...

# Streamlit app
def main():

    # Session state to hold the value of AutoRepeat button across reruns
    if "auto_repeat" not in st.session_state:
        st.session_state.auto_repeat = "On"
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0  # Use 0 as a default index

    # Load the history of clicks
    history = load_history()

    # Display the buttons for each URL
    for url, name, emoji in zip(urls, url_names, url_emojis):
        #if st.button(f"{emoji} {name}"):
        if st.button(f"{emoji} {name}", key=url):  # using the URL as the unique key
            # Open the URL in a new browser tab using JavaScript
            st.write('<script>window.open("'+url+'", "_blank");</script>', unsafe_allow_html=True)
            # Update the history of clicks
            history[url] += 1
            save_history(history)
        # Display the number of times the URL was opened below its corresponding button
        st.write(f"Clicked: {history[url]} times")

# Function to load the history of clicks from the text file
def load_history():
    try:
        with open("click_history.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {url: 0 for url in urls}

# Function to save the updated history of clicks to the text file
def save_history(history):
    with open("click_history.txt", "w") as f:
        json.dump(history, f)

# Streamlit app
def main():
    # Load the history of clicks
    history = load_history()

    # Create a list of URLs with their associated names, emojis, and click counts
    url_data = [{'url': url, 'name': name, 'emoji': emoji, 'clicks': history[url]} 
                for url, name, emoji in zip(urls, url_names, url_emojis)]

    # Sort the list by click counts in descending order
    url_data.sort(key=lambda x: x['clicks'], reverse=True)

    # Display the sorted URLs in columns up to four columns wide
    num_cols = min(4, len(url_data))
    cols = st.columns(num_cols)

    for i, data in enumerate(url_data):
        col = cols[i % num_cols]
        with col:
            if st.button(f"{emoji} {name}", key=url):  # using the URL as the unique key
                # Open the URL in a new browser tab using JavaScript
                st.write('<script>window.open("'+data['url']+'", "_blank");</script>', unsafe_allow_html=True)
                # Update the history of clicks
                history[data['url']] += 1
                save_history(history)
            # Display the number of times the URL was opened below its corresponding button
            st.write(f"Clicked: {history[data['url']]} times")



if __name__ == "__main__":
    main()


# Timer logic
if st.session_state.auto_repeat == "On":
    timer_placeholder = st.empty()
    for i in range(10, 0, -1):
        timer_placeholder.text(f"Reloading in {i} seconds...")
        time.sleep(1)
    history = load_history()  # Reload the history after the countdown

    # Display the Bokeh graph showing the click counts
    non_zero_urls = [name for url, name in zip(urls, url_names) if history[url] > 0]
    non_zero_counts = [history[url] for url in urls if history[url] > 0]

    source = ColumnDataSource(data=dict(urls=non_zero_urls, counts=non_zero_counts))

    p = figure(x_range=non_zero_urls, plot_height=350, title="Click Counts per URL",
               toolbar_location=None, tools="")
    p.vbar(x='urls', top='counts', width=0.9, source=source)
    p.xaxis.major_label_orientation = 1.2

    st.bokeh_chart(p)