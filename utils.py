# 1
def load_candidates_from_json(path):
    """
    возвращает список всех кандидатов
    :param path: файл со списком кандидатов
    :return: список всех кандидатов
    """
    import json

    with open(path, encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates

# 2
def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    :param candidate_id: id кандидата
    :return: кандидат с определенным id
    """
    for candidate in load_candidates_from_json("candidates.json"):
        if int(candidate_id) == candidate["id"]:
            return candidate

# 3
def get_candidates_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    :param candidate_name: Имя кандидата
    :return: Кандидат с определенным id
    """
    candidates = load_candidates_from_json("candidates.json")
    list_candidates = []

    for candidate in candidates:
        if candidate_name.lower() == candidate["name"].lower():
            list_candidates.append(candidate)

    return list_candidates

# 4
def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    :param skill_name: навык для поиска кандидатов
    :return: найденные кандидаты с определенным навыком
    """
    candidates = load_candidates_from_json("candidates.json")
    list_candidates = []

    for candidate in candidates:
        skills = candidate["skills"].split(", ")
        for skill in skills:
            if skill_name.lower() == skill.lower():
                list_candidates.append(candidate)

    return list_candidates
