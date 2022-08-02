from django.shortcuts import render

videos = [
    {"slug": "motivacao", "titulo": "Video Aperitivo: 7lions", "vimeo_id": 735480456},
    {"slug": "instalacao-windows", "titulo": "Instalação Windows", "vimeo_id": 2511497668},
]

videos_dct = {dct["slug"]: dct for dct in videos}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
