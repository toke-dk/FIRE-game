import pygame.display
from pygame.locals import *
import pygame_stuff.progress_bar
import random
import pygame_stuff.button_class
from sys import exit

pygame.init()
unloadedbar = pygame.image.load("Billeder/loadedbar.png")
loadedbar = pygame.image.load("Billeder/loadedbar.png")

def show_calculation_after_every_round(gamle_penge, pris, din_inkomst, nye_penge):
    print(f"{gamle_penge} - {pris} = ")
    print(f"+ {din_inkomst} =")
    print(f"Penge i alt {nye_penge}")


def choose_crypto(penge, inkomst):
    gevinst = 0
    while True:
        print("A) Bitcoin (stor risiko)")
        print("B) s&p 500 (lige risiko)")
        print("C) Disney (lille risiko)")
        while True:
            if type_invest.lower() == "a" or type_invest.lower() == "b" or type_invest.lower() == "c":
                break
            else:
                print("Det skal være et af valgmulighederne")
        while True:
            try:
                beloeb = 2
                if beloeb > penge:
                    print('Du har ikke råd')
                    continue
                elif type(beloeb) != int:
                    continue
                break
            except:
                print("Det skal være et tal")
                continue
        sandsynlighed = random.randint(1, 10)
        # the award system
        if type_invest.lower() == "a":
            if sandsynlighed <= 2:
                gevinst = beloeb
            elif sandsynlighed > 2:
                gevinst = -(beloeb/2)
            break
        elif type_invest.lower() == "b":
            if sandsynlighed <= 5:
                gevinst = beloeb/7
            elif sandsynlighed > 5:
                gevinst = beloeb/8
            break
        elif type_invest.lower() == "c":
            if sandsynlighed <= 9:
                gevinst = beloeb/11
            elif sandsynlighed > 9:
                gevinst = beloeb/13
            break
    gevinst = int(gevinst)
    if gevinst < 0:
        print(f"Fordi din investering ikke gik så godt, er din inkomst nu faldet med {gevinst}")
    elif gevinst > 0:
        print(f"Din investering går rigtig godt, så din inkomst er steget med {gevinst}")
    elif gevinst == 0:
        print("Din investering har desværre ikke gjort noget for dig så din inkomst er ikke steget")

    inkomst += int(gevinst)
    gamle_penge = penge
    penge -= beloeb
    nye_penge = penge
    din_inkomst = inkomst
    pris = beloeb
    return gamle_penge, nye_penge, din_inkomst, pris


width = 800
height = 800
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("FIRE-spillet")

pygame.display.flip()
running = True

gamle_penge = 0
din_inkomst = 0
nye_penge = 0
pris = 0

font = pygame.font.Font("freesansbold.ttf", 32)

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
             "valgmuligheder": [{"tekst": "A. Bilfd", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Biadl", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købeee?",
             "valgmuligheder": [{"tekst": "A. Bilfd", "point": 2, "pris": 100, "inkomststigning": 10},
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
            button1 = pygame_stuff.button_class.Button(screen,50,100,200,50,(0, 0, 255),(255, 255, 255),"hello",(0, 0, 0),font)
            x, y = pygame.mouse.get_pos()
            print(x, y)
            button1.draw(x, y)
            click_x,click_y = pygame.mouse.get_pos()
            if button1.action(click_x, click_y):
                print("Button Clicked")

            # text on pygame
            penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
            inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
            question_text = font.render(f"{quiz_set['spørgsmål']}", False, (250, 250, 0))

            penge_tekst_rect = penge_tekst.get_rect()
            inkomst_tekst_rect = inkomst_tekst.get_rect()
            question_text_rect = question_text.get_rect()

            penge_tekst_rect.bottomright = (width, height)
            inkomst_tekst_rect.bottomleft = (0, height)
            question_text_rect.center = (width//2, height//10)

            screen.blit(penge_tekst, penge_tekst_rect)
            screen.blit(inkomst_tekst, inkomst_tekst_rect)
            screen.blit(question_text, question_text_rect)

            print(f'\nPenge: {penge}, Inkomst: {inkomst} \n{quiz_set["spørgsmål"]}')

            # prints the options
            pos = 0
            for i in quiz_set["valgmuligheder"]:
                pos += 50
                question_text = font.render(f"{i['tekst']} : {i['pris']},-", False, (250, 250, 0))
                question_text_rect = penge_tekst.get_rect()
                question_text_rect.topleft = (width//10, height//10 + pos)
                screen.blit(question_text, question_text_rect)

                print(f'{i["tekst"]} : {i["pris"]}kr')

            # it only stops when typed correct
            run = True
            while run:
                # dette er fra den anden fil
                pygame_stuff.progress_bar.update_bar(screen, points, loadedbar, unloadedbar)

                gaet = "a"

                # investing
                if gaet.upper() == "I":
                    # det er defineret ovenfor
                    gamle_penge, nye_penge, inkomst, pris = choose_crypto(penge, inkomst)
                    din_inkomst = inkomst
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
                            print(f"+ {inkomst} =")
                            # evt asset
                            inkomst += i["inkomststigning"]
                            # du får løn
                            penge += inkomst
                            run = False
                        else:
                            print("Du har ikke råd til det")

            # updates information
            screen.fill(color=(0,0,0))

