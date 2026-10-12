playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("تعداد آهنگ ها:", len(playlist))

print("اولین آهنگ:", playlist[0])
print("آخرین آهنگ:", playlist[-1])

playlist.append("Dynamite")

playlist.remove("Believer")

playlist.sort()
print("لیست مرتب شده:", playlist)

print("لیست شماره دار آهنگ ها:")
for index, song in enumerate(playlist, start=1):
  print(f"{index}. {song}")