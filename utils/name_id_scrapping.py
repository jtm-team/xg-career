from pathlib import Path

def name_id_scrapping():
    user_path = Path.cwd()
    complete_path = str(user_path.parent) +"/data/name_id_understat.txt"
    with open(complete_path) as f:
        lines = f.readlines()
        text = lines[0]
        text = text.replace("\'", "")
        text = text.replace("}", "")
        text = text.replace("{", "")
        splitted = text.split(",")
        dict_id_name = {}
        for i in range(1, len(splitted)):
            id = splitted[i].split(": ")[0][1:]
            name = splitted[i].split(": ")[1]
            dict_id_name[id] = name

    return dict_id_name

dict_id_name = name_id_scrapping()
