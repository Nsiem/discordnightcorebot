import pipeclient

def nightcore():
    client = pipeclient.PipeClient()
    client.write(f'Import2: Filename="D:\....Coding\discordnightcorebot\songs\Temp.mp3"')
    client.write('SelectAll:')
    client.write('ChangeSpeed: Percentage=10')
    client.write(f'Export2: Filename="D:\....Coding\discordnightcorebot\songs\Tempnightcore.mp3"')
    client.write('RemoveTracks:')