import pytest
from django.urls import reverse
from django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse("aperitivos:video", args=("motivacao",)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, "<title>Video Aperitivo: 7lions</title>", html=True)


def test_iframe_video(resp):
    assert_contains(resp, 'src="https://player.vimeo.com/video/735480456')
