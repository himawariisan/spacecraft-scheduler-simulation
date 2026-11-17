from data import SCENARIOS
from algorithms import ALGORITHMS
from metrics import metrics


def run_scenario(title, tasks):
    print("=" * 78)
    print(f"СЦЕНАРІЙ: {title}")
    print("=" * 78)
    critical = min(tasks, key=lambda t: t["priority"])["name"]
    summary = []

    for algo_name, algo in ALGORITHMS.items():
        rows = metrics(tasks, algo(tasks))
        avg_ta = sum(r[3] for r in rows) / len(rows)
        avg_wt = sum(r[4] for r in rows) / len(rows)
        crit_wait = next(r[4] for r in rows if r[0] == critical)
        misses = sum(r[6] for r in rows)
        crit_missed = next(r[6] for r in rows if r[0] == critical)
        summary.append((algo_name, avg_wt, avg_ta, crit_wait, misses, crit_missed))

        print(f"\n--- {algo_name} ---")
        print(f"{'Задача':<24}{'Пріоритет':>7}{'Завершення':>12}{'Виконання':>11}{'Очікування':>12}{'Дедлайн':>9}{'Встигла':>9}")
        for name, prio, fin, ta, wt, dline, missed in rows:
            print(f"{name:<24}{prio:>7}{fin:>12}{ta:>11}{wt:>12}{dline:>9}{'НІ' if missed else 'так':>9}")
        print(f"Середнє: виконання = {avg_ta:.2f}, очікування = {avg_wt:.2f}; "
              f"пропущено дедлайнів: {misses} з {len(rows)}")

    print(f"\n>>> ПІДСУМОК (критична задача: «{critical}»)")
    print(f"{'Алгоритм':<28}{'Сер. очікув.':>14}{'Сер. викон.':>13}{'Очікув. крит.':>15}{'Пропущ. дедл.':>15}{'Крит. встигла':>15}")
    for algo_name, wt, ta, cw, ms, cm in summary:
        print(f"{algo_name:<28}{wt:>14.2f}{ta:>13.2f}{cw:>15}{ms:>15}{'НІ' if cm else 'так':>15}")
    print()


if __name__ == "__main__":
    for title, tasks in SCENARIOS.items():
        run_scenario(title, tasks)
