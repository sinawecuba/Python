# 8-6. City Names
def city_country(city, country):
    """Return a formatted string 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Call the function with three city-country pairs
print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))

print("\n")

# 8-7. Album
def make_album(artist, title, num_songs=None):
    """Return a dictionary containing information about an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

# Create three album dictionaries
album1 = make_album('nirvana', 'nevermind')
album2 = make_album('pink floyd', 'the wall', 26)
album3 = make_album('radiohead', 'ok computer')

# Print albums to verify
print(album1)
print(album2)
print(album3)

print("\n")

# 8-8. User Albums
while True:
    print("Enter album information (or 'q' to quit).")
    artist_input = input("Artist: ")
    if artist_input.lower() == 'q':
        break
    title_input = input("Album title: ")
    if title_input.lower() == 'q':
        break
    num_songs_input = input("Number of songs (optional, press enter to skip): ")
    if num_songs_input.lower() == 'q':
        break
    if num_songs_input.isdigit():
        album_info = make_album(artist_input, title_input, int(num_songs_input))
    else:
        album_info = make_album(artist_input, title_input)
    print(f"Album created: {album_info}\n")
