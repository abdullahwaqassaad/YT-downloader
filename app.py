import streamlit as st
from yt_dlp import YoutubeDL
import os

st.title("📥 Video Downloader")
st.write("Download YouTube, TikTok, and Instagram videos")

url = st.text_input("Enter Video URL")

if st.button("Download"):
    if url:
        try:
            ydl_opts = {
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Accept-Language': 'en-US,en;q=0.9',
                }
            }
            os.makedirs("downloads", exist_ok=True)
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            with open(filename, "rb") as f:
                st.download_button(
                    label="Download File",
                    data=f,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

            st.success("✅ Video downloaded!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a URL")
