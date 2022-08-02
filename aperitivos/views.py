from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {"titulo": "Video Aperitivo: 7lions", "vimeo_id": 735480456},
        'instalacao-windows': {"titulo": "Instalação Windows", "vimeo_id": 2511497668},
    }
    video = videos[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
