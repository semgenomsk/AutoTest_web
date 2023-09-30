from main import get_notMe, get_Me
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_1(login):
    res = get_notMe(login)
    lst = res["data"]
    lst_id = [el["id"] for el in lst]
    assert 80422 in lst_id, "test Failed"


def test_create_post(login):
    response = requests.post(data["url_posts"],
                             headers={"X-Auth-Token": login},
                             data={'title': data["title"],
                                   'description': data["description"],
                                   'content': data["content"]})

    lst_description = [el["description"] for el in get_Me(login)["data"]]
    assert data["description"] in lst_description, "test Failed"