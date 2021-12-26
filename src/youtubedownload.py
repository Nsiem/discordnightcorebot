import yt_dlp

async def download_song(vID):
    url = f'https://www.youtube.com/watch?v={vID}'
    vinfo1 = yt_dlp.YoutubeDL().extract_info(
        url = url , download=False
    )
    vinfo = yt_dlp.YoutubeDL().extract_info(
        url = url , download=False
    )
    filename = f"{vinfo['title']}.mp3"

    options={
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'outtmpl': 'D:/....Coding/discordnightcorebot/songs/Temp.mp3'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([vinfo['webpage_url']])

    print(f"Download complete... {filename}")
    return filename