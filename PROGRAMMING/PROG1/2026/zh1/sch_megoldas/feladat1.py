def check(text):
    users = {}
    for row in text:
        if ';' in row:
            user, vid = row.strip().split(';')
            if user not in users:
                users[user] = set()
            users[user].add(vid)
        else:
            break
    
    u1,u2 = text[-1].strip().split()
    vid1 = users.get(u1, set())
    vid2 = users.get(u2, set())
    c = vid1 & vid2
    union = vid1 | vid2
    return len(vid1), len(vid2), len(c), len(union)


if __name__ == "__main__":
    text =[
    "nora;vid-101",
    "nora;vid-102",
    "nora;vid-101",

    "tibi;vid-102",
    "tibi;vid-201",

    "dori;vid-999",
    "VEGE",

    "nora tibi"
    ]
    
    u1_db, u2_db, kozos_db, all_db = check(text)
    print(f"u1_egyedi_db={u1_db}")
    print(f"u2_egyedi_db={u2_db}")
    print(f"kozos_db={kozos_db}")
    print(f"osszes_db={all_db}")
