from django.shortcuts import render


def video(request, slug):
    video = {"titulo": "Video Aperitivo: 7lions", "vimeo_id": 735480456}
    return render(request, "aperitivos/video.html", context={"video": video})
