import pytest
from django.urls import reverse
from django_assertions import assert_contains
from model_bakery import baker

from aperitivos.models import Video


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse("aperitivos:video", args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse("aperitivos:video", args=(f"{video.slug}video_nao_existente",)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo, html=True)


def test_iframe_video(resp, video):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{video.vimeo_id}')


def test_status_code_404(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404
