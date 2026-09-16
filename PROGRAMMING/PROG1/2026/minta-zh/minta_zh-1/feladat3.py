# Főprogram
if __name__ == "__main__":
    """ timestamp;user;action;value """

    data = [
    "2026-03-21 10:00;anna;LOGIN;-",
    "2026-03-21 10:01;anna;VIEW;python-alapok",
    "2026-03-21 10:02;bela;VIEW;python-alapok",
    "2026-03-21 10:03;anna;BUY;1200",
    "2026-03-21 10:04;bela;BUY;800",
    "2026-03-21 10:05;bela;ERROR;timeout",
    "2026-03-21 10:06;cili;VIEW;dict-es-set",
    "2026-03-21 10:07;cili;BUY;1000",
    "2026-03-21 10:08;cili;BUY;-5",
    ]

    actions = {"LOGIN": 0, "VIEW":0, "BUY":0, "ERROR":0}
    users = {}
    rows = 0
    firstErrorUser = None

    for row in data:
        parts = row.split(';')
        timestamp = parts[0]
        user = parts[1]
        action = parts[2]
        value = parts[3]

        if action not in actions:
            continue

        if action == "BUY":
            if not value.replace('-','').isdigit():
                continue
            a_value = int(value)
            if a_value <= 0:
                continue
        
        rows += 1
        actions[action] +=1

        if user not in users:
            users[user] = {
                "viewed": set(),
                "spent":0,
                "errors":0
            }

        if action == "VIEW":
            users[user]["viewed"].add(value)
        elif action == "BUY":
            users[user]["spent"] += int(value)
        elif action == "ERROR":
            users[user]["errors"] += 1
            if firstErrorUser is None:
                firstErrorUser = user
    
    # 3/A
    print(f"LOGIN = {actions['LOGIN']}")
    print(f"VIEW = {actions['VIEW']}")
    print(f"BUY = {actions['BUY']}")
    print(f"ERROR = {actions['ERROR']}\n")

    # 3/B
    buyers_list = []
    for user, data in users.items():
        buyers_list.append((user, data["spent"]))

    def buyer_sort(item):
        return(-item[1], item[0])

    top_buyers = sorted(buyers_list, key=buyer_sort)
    for i in range(min(2, len(top_buyers))):
        print(f"{top_buyers[i][0]} {top_buyers[i][1]}\n")

    # 3/C
    if rows > 0:
        rate = (actions["ERROR"] / rows * 100)
        print(f"hibaarány = {rate:.2f}%\n")

    error_users=[]
    for user, data in users.items():
        error_users.append((user, data["errors"]))
    
    def error_sort(item):
        return(-item[1],item[0])
    
    most_error = sorted(error_users, key=error_sort)[0]
    print(f"problemas_user= {most_error[0]} ({most_error[1]} error)\n")

    # 3/D
    for user in sorted(users.keys()):
        statdata = users[user]
        egyedi = len(data["viewed"])
        print(f"{user} view_egyedi_db={egyedi} koltes={statdata['spent']} error_db={statdata['errors']}\n")

    
    # 3/E
    print(f"Első hiba elkövetője: {firstErrorUser}")
    
