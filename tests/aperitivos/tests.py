import pytest
from django.urls import reverse
from django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse("aperitivos:video", args=("motivacao",)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, "<title>Vídeo Aperitivo: 7lions</title>")


def test_titulo_video(resp):
    assert_contains(resp, "<title>Vídeo Aperitivo: 7lions</title>")
