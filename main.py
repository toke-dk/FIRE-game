import pygame
import pygame_stuff.progress_bar
from colour import Color

pygame.init()

screen = pygame.display.set_mode((200, 200))

pygame.display.set_caption("FIRE-spil")

pygame.display.flip()
running = True

red = Color("#0043A7")
colors = list(red.range_to(Color("green"), 10))

while True:
        quiz_sets = [
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
        ]
        points = 0
        penge = 200
        inkomst = 100

        for quiz_set in quiz_sets:
            quiz_set_items = list(quiz_set.items())
            print(f'\nPenge: {penge}, Inkomst: {inkomst} \n{quiz_set["spørgsmål"]}')
            for i in quiz_set["valgmuligheder"]:
                print(f'{i["tekst"]} : {i["pris"]}kr')
            run = True
            while run:
                # dette er fra den anden fil
                pygame_stuff.progress_bar.update_bar(screen, points)

                gaet = input("Skriv(A,B,C): ")
                # checks if it matchs the options
                for i in quiz_set["valgmuligheder"]:
                    # the first letter in the option
                    if gaet.upper() == i["tekst"][0]:
                        # checks if you can afford
                        if penge - i["pris"] >= 0:
                            points += int(i["point"])
                            print(f"{penge} - {i['pris']} = ")
                            # prisen du skal betale
                            penge -= i["pris"]
                            input(penge)
                            print(f"+ {inkomst} =")
                            # evt asset
                            inkomst += i["inkomststigning"]
                            # du får løn
                            penge += inkomst
                            run = False
                        else:
                            print("Du har ikke råd til det")
            input(f"Penge i alt: {penge}")

