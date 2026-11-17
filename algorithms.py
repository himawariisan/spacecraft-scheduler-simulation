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

ALGORITHMS = {
    "FIFO": fifo,
    "SJF": sjf,
}
