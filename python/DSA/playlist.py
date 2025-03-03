# 🎧 Step 1: Create a dictionary of songs
playlist = {
    1: {"title": "Song A", "artist": "Artist 1", "duration": "3:45"},
    2: {"title": "Song B", "artist": "Artist 2", "duration": "4:10"},
    3: {"title": "Song C", "artist": "Artist 3", "duration": "2:58"},
}

# 🎶 Step 2: Display the playlist
def display_playlist():
    print("\n🎼 Current Playlist:")
    for key, song in playlist.items():
        print(f"{key}. {song['title']} - {song['artist']} [{song['duration']}]")

display_playlist()

# 🎤 Step 3: Add a new song
new_title = input("\nEnter song title: ")
new_artist = input("Enter artist name: ")
new_duration = input("Enter song duration (e.g., 3:30): ")

new_id = max(playlist.keys()) + 1  # Assign a new unique key
playlist[new_id] = {"title": new_title, "artist": new_artist, "duration": new_duration}

print("\n📀 Updated Playlist:")
display_playlist()

# 🎼 Step 4: Play a song
song_choice = int(input("\nEnter the song number to play: "))

if song_choice in playlist:
    print(f"\n🎶 Now Playing: {playlist[song_choice]['title']} by {playlist[song_choice]['artist']} 🎶")
else:
    print("\n❌ Invalid choice! Please enter a valid song number.")
