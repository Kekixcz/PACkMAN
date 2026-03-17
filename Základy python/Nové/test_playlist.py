playlist = [
    ["Shape of You", "Ed Sheeran", "03:54"],
    ["Perfect", "Ed Sheeran", "04:40"],
    ["Blinding Lights", "The Weeknd", "03:20"],
    ["Bohemian Rhapsody", "Queen", "05:55"],
    ["Bad Guy", "Billie Eilish", "03:14"],
    ["Hallelujah", "Leonard Cohen", "04:39"]
]

def time_to_seconds(t):
    minutes, seconds = map(int, t.split(':'))
    return minutes * 60 + seconds

celkove = 0
nejdelsi = None
interpret_set = set()

for nazev, interpret, delka in playlist:
    sec = time_to_seconds(delka)
    celkove += sec
    interpret_set.add(interpret)
    if nejdelsi is None or sec > time_to_seconds(nejdelsi[2]):
        nejdelsi = [nazev, interpret, delka]

minuty = celkove // 60
sekundy = celkove % 60

print(f"Nejdelší je: {nejdelsi}")
print(f"Celková délka playlistu je: {minuty} minut {sekundy} sekund")
print(f"Unikátní interpretá jsou: {interpret_set}")
