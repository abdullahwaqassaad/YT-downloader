import streamlit as st
from yt_dlp import YoutubeDL
import os

st.title("📥 Video Downloader")
st.write("Download YouTube videos, Shorts, Instagram Reels, and TikTok videos")

url = st.text_input("Enter Video URL")

if st.button("Download"):
    if url:
        try:
            ydl_opts = {
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'format': 'best'
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
