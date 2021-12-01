import pygame
import pygame_stuff.progress_bar
import random


def show_calculation_after_every_round(gamle_penge, pris, din_inkomst, nye_penge):
    print(f"{gamle_penge} - {pris} = ")
    input(nye_penge)
    print(f"+ {din_inkomst} =")
    print(f"Penge i alt {nye_penge}")


def choose_crypto(penge, inkomst):
    while True:
        try:
            beloeb = int(input("Hvor mange penge vil du investere: "))
            if beloeb > penge:
                # is doing except
                print("Du har ikke råd")
            else:
                # gevinst either raises 15 percent or falls 15 percent
                gevinst = random.randint(int(-(40 / 100 * beloeb)), int(40 / 100 * beloeb))
                if gevinst < 0:
                    print(f"Fordi din investering ikke gik så godt, er din inkomst nu faldet med {gevinst}")
                elif gevinst > 0:
                    print(f"Din investering går rigtig godt, så din inkomst er steget med {gevinst}")
                elif gevinst == 0:
                    print("Din investering har desværre ikke gjort noget for dig så din inkomst er ikke steget")
                inkomst += gevinst

                # for printing the stuff
                gamle_penge = penge
                penge -= beloeb
                nye_penge = penge
                din_inkomst = inkomst
                pris = beloeb

                return gamle_penge, nye_penge, din_inkomst, pris
        except:
            print("Det skal være et tal!\n")
            continue
    return



screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption("FIRE-spillet")

pygame.display.flip()
running = True

gamle_penge = 0
din_inkomst = 0
nye_penge = 0
pris = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
            {"spørgsmål": "Hvad vil du helst købeee?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
        ]
        random.shuffle(quiz_sets)
        points = 0
        penge = 200
        inkomst = 100

        for quiz_set in quiz_sets:
            quiz_set_items = list(quiz_set.items())
            print(f'\nPenge: {penge}, Inkomst: {inkomst} \n{quiz_set["spørgsmål"]}')

            # prints the options
            for i in quiz_set["valgmuligheder"]:
                print(f'{i["tekst"]} : {i["pris"]}kr')

            # it only stops when typed correct
            run = True
            while run:
                # dette er fra den anden fil
                pygame_stuff.progress_bar.update_bar(screen, points)

                gaet = input("Skriv(A,B,C,I): ")

                # investing
                if gaet.upper() == "I":
                    gamle_penge, nye_penge, din_inkomst, pris = choose_crypto(penge, inkomst)
                    run = False
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

