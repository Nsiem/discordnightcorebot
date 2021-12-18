from dotenv import load_dotenv
import os
import aiohttp
import asyncio
import youtube_dl


load_dotenv()
API_KEY = os.getenv('API_KEY')
    
# Retrieves anime list based on text search, returns json with up to 5 results at a time
async def search_youtube(searchQuery: str):
    url = f'https://youtube.googleapis.com/youtube/v3/search?key={API_KEY}&maxResults=1&q={searchQuery}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            youtube_list = await resp.json()
    session.close
    return youtube_list

def download_song(vID):
    url = f'https://www.youtube.com/watch?v={vID}'
    filename = "temp.mp3"
    options = {
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(url)

    print(f"Download complete... {filename}")


if __name__ == '__main__':
    search = "kda"
    result = asyncio.run(search_youtube(search))
    download_song(result['items'][0]['id']['videoId'])