# importing the module
from pytube import YouTube
from pytube import Playlist

download_choice = input("Type Paylist or Video: ").strip().lower()


if download_choice == "playlist":
# PLAYLIST
	# link of the video to be downloaded
	playlist_link=input("Input Playlist Link: ")

	try:
		# object creation using YouTube
		# which was imported in the beginning
		playlist_obj = Playlist(playlist_link)
	except:
		print("Connection Error") #to handle exception
	playlist_obj = Playlist(playlist_link)

	for yt in playlist_obj.videos:
		#to set the name of the file
		print(yt.title)
		file_name = str(yt.title)
		
		# CHOOSE AUDIO OR VIDEO
		av_choice = input("Type 'a' for audio only or 'v' for both: ").strip().lower()

		if av_choice == "a":
		# AUDIO
			# ask user what filetype
			file_ext = input("file extension: ").strip().lower()
			if file_ext in ["", "*", "none"]:
				file_ext = None
			# ask user which audio stream
			audio_streams_str = str(yt.streams.filter(only_audio=True, file_extension=file_ext))
			print("skip, done, or choose itag:")
			itag = input(audio_streams_str + "\nitag:")

			if itag == "skip":
				print("Skipped!")
				continue
			elif itag == "done":
				print("All Skipped!")
				break

			# download
			audio_stream = yt.streams.get_by_itag(itag)
			try:
				audio_stream.download(filename=file_name)
			except:
				print("Download Error")
			print(file_name, "Downloaded Successfully")

		elif av_choice == "v":
		# VIDEO
			# ask user what filetype
			file_ext = input("file extension: ").strip().lower()
			if file_ext in ["", "*", "none"]:
				file_ext = None
			# ask user which video stream
			video_streams_str = str(yt.streams.filter(progressive=True, file_extension=file_ext))
			print("skip, done, or choose itag:")
			itag = input(video_streams_str + "\nitag:")

			if itag == "skip":
				print("Skipped!")
				continue
			elif itag == "done":
				print("All Skipped!")
				break

			# download
			video_stream = yt.streams.get_by_itag(itag)
			try:
				video_stream.download(filename=file_name)
			except:
				print("Download Error")
			print(file_name, "Downloaded Successfully")

		else: 
			print("Incorrect input, skipping")


elif download_choice == "video":
# VIDEO 
	video_link=input("Input Video Link: ")

	try:
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(video_link)
	except:
		print("Connection Error") #to handle exception

	#to set the name of the file
	try:
		print(yt.title)
	except:
		print("Title Error")
	#file_name = str(yt.title)
	
	# CHOOSE AUDIO OR VIDEO
	av_choice = input("Type 'a' for audio only or 'v' for both: ").strip().lower()

	if av_choice == "a":
	# AUDIO
		# ask user what filetype
		file_ext = input("file extension: ").strip().lower()
		if file_ext in ["", "*", "none"]:
			file_ext = None
		# ask user which audio stream
		audio_streams_str = str(yt.streams.filter(only_audio=True, file_extension=file_ext))
		print("choose itag:")
		itag = input(audio_streams_str + "\nitag:")

		# download
		audio_stream = yt.streams.get_by_itag(itag)
		try:
			audio_stream.download()#filename=file_name)
		except:
			print("Download Error")
		print("Downloaded Successfully")

	elif av_choice == "v":
	# VIDEO
		# ask user what filetype
		file_ext = input("file extension: ").strip().lower()
		if file_ext in ["", "*", "none"]:
			file_ext = None
		# ask user which video stream
			video_streams_str = str(yt.streams.filter(progressive=True, file_extension=file_ext))
			print("choose itag:")
			itag = input(video_streams_str + "\nitag:")

			# download
			video_stream = yt.streams.get_by_itag(itag)
			try:
				video_stream.download()#filename=file_name)
			except:
				print("Download Error")
			print("Downloaded Successfully")

	else: 
		print("Incorrect input, cancelling")

print('Task Completed!')
