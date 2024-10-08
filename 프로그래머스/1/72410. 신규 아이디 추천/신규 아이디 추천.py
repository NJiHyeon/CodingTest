def solution(new_id):
    import re
    new_id = new_id.lower() #1
    new_id = re.sub('[^a-z0-9-_.]', '', new_id) #2
    while '..' in new_id: #3
        new_id = new_id.replace('..', '.')
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id