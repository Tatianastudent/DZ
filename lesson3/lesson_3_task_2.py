from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S26", "+79247304570"),
    Smartphone("Samsung", "Galaxy S25", "+79145253265"),
    Smartphone("Redmi", "Note 15 pro", "+79143256480"),
    Smartphone("Redmi", "Note A5", "+79246572890"),
    Smartphone("Xonor", "Turbo", "+79990576680")
    ]

for smartphone in catalog:
    print(f'{smartphone.brand}, {smartphone.model}, {smartphone.number}')