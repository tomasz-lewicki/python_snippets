from pytube import YouTube

#YouTube('https://www.youtube.com/watch?v=ZK3O402wf1c').streams.first().download()

def show_progress(stream, chunk, file_handle, bytes_remaining):
    #if(bytes_remaining%100==0):
        print(int(file_handle.tell()*100/(file_handle.tell()+bytes_remaining)),' %')

print("Provide link to the video")

link = input()

yt=YouTube(link)

yt.register_on_progress_callback(show_progress)

yt.streams.filter(progressive=True).order_by('resolution').desc().all()[0].download()
