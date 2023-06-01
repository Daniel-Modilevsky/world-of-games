from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def points_of_winning(difficulty):
    return difficulty * 3 + 5


def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, "r+") as f:
            current_score = int(f.read())
            new_score = current_score + points_of_winning(difficulty)
            f.seek(0)
            f.write(str(new_score))
            f.truncate()
    except FileNotFoundError:
        with open(SCORES_FILE_NAME, "w") as f:
            f.write(str(points_of_winning(difficulty)))
    except Exception as e:
        print(e)
        return BAD_RETURN_CODE
