# Алгоритми планування

def _non_preemptive(tasks, key):
    time, remaining, finish = 0, list(tasks), {}
    while remaining:
        ready = [t for t in remaining if t["arrival"] <= time]
        if not ready:                       # процесор простоює
            time = min(t["arrival"] for t in remaining)
            continue
        t = min(ready, key=key)
        time += t["burst"]
        finish[t["name"]] = time
        remaining.remove(t)
    return finish

def fifo(tasks):
    return _non_preemptive(tasks, key=lambda t: t["arrival"])

def sjf(tasks):
    return _non_preemptive(tasks, key=lambda t: (t["burst"], t["arrival"]))

def priority(tasks):
    return _non_preemptive(tasks, key=lambda t: (t["priority"], t["arrival"]))


def priority_preemptive(tasks):
    time, finish = 0, {}
    left = {t["name"]: t["burst"] for t in tasks}
    while left:
        ready = [t for t in tasks if t["name"] in left and t["arrival"] <= time]
        if not ready:
            time += 1
            continue
        t = min(ready, key=lambda t: (t["priority"], t["arrival"]))
        left[t["name"]] -= 1
        time += 1
        if left[t["name"]] == 0:
            del left[t["name"]]
            finish[t["name"]] = time
    return finish


ALGORITHMS = {
    "FIFO": fifo,
    "SJF": sjf,
    "Priority": priority,
    "Priority (з витісненням)": priority_preemptive,
}
