# Розрахунок показників: час виконання, очікування, перевірка дедлайнів

def metrics(tasks, finish):
    rows = []
    for t in tasks:
        turnaround = finish[t["name"]] - t["arrival"]   # час виконання
        waiting = turnaround - t["burst"]               # час очікування
        missed = turnaround > t["deadline"]             # дедлайн пропущено
        rows.append((t["name"], t["priority"], finish[t["name"]], turnaround, waiting,
                     t["deadline"], missed))
    return rows
