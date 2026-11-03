import pytest

pytestmark = pytest.mark.api


def url(api, path):
    return f"{api.base_url}{path}"


@pytest.mark.smoke
def test_get_single_post(api):
    r = api.get(url(api, "/posts/1"), timeout=10)
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert {"userId", "id", "title", "body"} <= body.keys()


def test_filter_posts_by_user(api):
    r = api.get(url(api, "/posts"), params={"userId": 1}, timeout=10)
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) == 10
    assert all(p["userId"] == 1 for p in posts)


def test_create_post_returns_201(api):
    payload = {"title": "qa test", "body": "created by pytest", "userId": 1}
    r = api.post(url(api, "/posts"), json=payload, timeout=10)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


def test_update_post(api):
    r = api.put(url(api, "/posts/1"),
                json={"id": 1, "title": "updated", "body": "x", "userId": 1},
                timeout=10)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"


def test_delete_post(api):
    assert api.delete(url(api, "/posts/1"), timeout=10).status_code == 200


def test_unknown_post_returns_404(api):
    assert api.get(url(api, "/posts/99999"), timeout=10).status_code == 404


def test_response_time_under_two_seconds(api):
    r = api.get(url(api, "/posts"), timeout=10)
    assert r.elapsed.total_seconds() < 2
