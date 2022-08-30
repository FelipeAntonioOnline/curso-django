from django.shortcuts import get_object_or_404, render

from aperitivos.models import Video

videos = [
    Video(slug="motivacao", titulo="Video Aperitivo: 7lions", vimeo_id=735480456),
    Video(slug="instalacao-windows", titulo="Instalação Windows", vimeo_id=2511497668),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, "aperitivos/video.html", context={"video": video})
