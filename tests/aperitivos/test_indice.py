import pytest
from django.urls import reverse
from django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse("aperitivos:indice"))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize("titulo", ["Video Aperitivo: 7lions", "Instalação Windows"])
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


# def test_iframe_video(resp):
#     assert_contains(resp, 'src="https://player.vimeo.com/video/735480456')
