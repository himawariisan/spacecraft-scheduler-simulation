# Вхідні дані: набори задач бортового комп'ютера

SCENARIOS = {
    "Штатна робота": [
        {"name": "Керування орієнтацією", "burst": 2, "arrival": 0, "priority": 1, "deadline": 3},
        {"name": "Зв'язок із Землею",     "burst": 4, "arrival": 1, "priority": 3, "deadline": 10},
        {"name": "Збір телеметрії",       "burst": 3, "arrival": 2, "priority": 2, "deadline": 6},
        {"name": "Тепловий контроль",     "burst": 1, "arrival": 3, "priority": 2, "deadline": 6},
        {"name": "Наукові виміри",        "burst": 5, "arrival": 4, "priority": 4, "deadline": 15},
    ],
    "Аварійна ситуація": [
        {"name": "Наукові виміри",        "burst": 8, "arrival": 0, "priority": 4, "deadline": 20},
        {"name": "Зв'язок із Землею",     "burst": 4, "arrival": 1, "priority": 3, "deadline": 14},
        {"name": "Збір телеметрії",       "burst": 3, "arrival": 2, "priority": 2, "deadline": 10},
        {"name": "Аварійна стабілізація", "burst": 2, "arrival": 3, "priority": 1, "deadline": 4},
        {"name": "Тепловий контроль",     "burst": 1, "arrival": 4, "priority": 2, "deadline": 8},
    ],
}

QUANTUM = 2
