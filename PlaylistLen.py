# importing the module
from pytube import YouTube
from pytube import Playlist

# link of the video to be downloaded
playlist_link=input("Input Playlist Link: ")

try:
	# object creation using YouTube
	# which was imported in the beginning
	playlist_obj = Playlist(playlist_link)
except Exception as e:
	print("Connection Error",e) #to handle exception
playlist_obj = Playlist(playlist_link)

total = 0
avrg = 0
nums = []
for yt in playlist_obj.videos:
	#to set the name of the file
	leng = yt.length
	nums.append(leng)
	avrg = sum(nums)/len(nums)
	print(yt.title,"- len",leng,"- avg",avrg)
	total += leng


print("total:",total, "seconds ==",total/60,"minutes ==",total/60/60,"hrs")
print("average:",avrg," seconds ==",avrg/60,"minutes")
