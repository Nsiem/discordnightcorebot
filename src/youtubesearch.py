from dotenv import load_dotenv
import os
import aiohttp
import asyncio
from youtubedownload import download_song

load_dotenv()
API_KEY = os.getenv('API_KEY')
    
# Retrieves anime list based on text search, returns json with up to 5 results at a time
async def search_youtube(searchQuery: str):
    url = f'https://youtube.googleapis.com/youtube/v3/search?part=id,snippet&maxResults=1&q={searchQuery}&key={API_KEY}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            youtube_list = await resp.json()
    session.close
    result = []
    result.append(await videoduration(youtube_list['items'][0]['id']['videoId']))
    result.append(youtube_list['items'][0]['id']['videoId'])   
    return result

# Retrieves details about specific video found
async def videoduration(v_id: str):
    url = f'https://youtube.googleapis.com/youtube/v3/videos?id={v_id}&part=contentDetails&key={API_KEY}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            videodetails = await resp.json()
    session.close
    result = True
    if('H' in videodetails['items'][0]['contentDetails']['duration']):
        result = False
    return result


if __name__ == '__main__':
    search = "kda"
    result = asyncio.run(search_youtube(search))
    vdetails = asyncio.run(videoduration(result['items'][0]['id']['videoId']))
    if('H' in vdetails['items'][0]['contentDetails']['duration']):
        print(False)
    print(vdetails['items'][0]['contentDetails']['duration'])
    download_song(result['items'][0]['id']['videoId'])