import requests


def get_name_by_id(id: int) -> str:
    r = requests.get("https://leetcode.com/api/problems/algorithms/")
    data = r.json()
    for each in data["stat_status_pairs"]:
        if int(each["stat"]["question_id"]) == id:
            return each["stat"]["question__title_slug"]
    return "NOT FOUND"
