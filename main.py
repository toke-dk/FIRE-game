quiz_sets = [
    {"spørgsmål": "Hvad vil du helst købe?",
     "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100}, {"tekst": "B. Tog", "point": 5, "pris": 12},
                        {"tekst": "C. Hus", "point": 100, "pris": 12}],
     "svar": "A"
     },
]

for quiz_set in quiz_sets:
    points = 0
    penge = 500
    quiz_set_items = list(quiz_set.items())
    print(quiz_set["spørgsmål"])
    for i in quiz_set["valgmuligheder"]:
        print(i["tekst"])
    run = True
    while run:
        gaet = input("Skriv(A,B,C): ")
        for i in quiz_set["valgmuligheder"]:
            # the first letter in the option
            if gaet.upper() == i["tekst"][0]:
                points += int(i["point"])
                run = False
    print(points)
