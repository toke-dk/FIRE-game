import pygame.display
from pygame.locals import *
import pygame_stuff.progress_bar
import random
from sys import exit


def next_question(quiz_sets, index):
    return quiz_sets[index]


def choose_crypto(penge, inkomst):
    gevinst = 0
    while True:
        while True:
            if type_invest.lower() == "a" or type_invest.lower() == "b" or type_invest.lower() == "c":
                break
            else:
                'print("Det skal være et af valgmulighederne")'
        while True:
            try:
                if beloeb > penge:
                    print('Du har ikke råd')
                    continue
                elif type(beloeb) != int:
                    continue
                break
            except:
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
        'print(f"Fordi din investering ikke gik så godt, er din inkomst nu faldet med {gevinst}")'
    elif gevinst > 0:
        'print(f"Din investering går rigtig godt, så din inkomst er steget med {gevinst}")'
    elif gevinst == 0:
        'print("Din investering har desværre ikke gjort noget for dig så din inkomst er ikke steget")'

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
question_id = 0

font = pygame.font.Font("freesansbold.ttf", 32)

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

quiz_set = next_question(quiz_sets, question_id)
random.shuffle(quiz_sets)
points = 0
penge = 200
inkomst = 100

# text on pygame
penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
question_text = font.render(f"{quiz_set['spørgsmål']}", False, (250, 250, 0))

penge_tekst_rect = penge_tekst.get_rect()
inkomst_tekst_rect = inkomst_tekst.get_rect()
question_text_rect = question_text.get_rect()

penge_tekst_rect.bottomright = (width, height)
inkomst_tekst_rect.bottomleft = (0, height)
question_text_rect.center = (width // 2, height // 10)

screen.blit(penge_tekst, penge_tekst_rect)
screen.blit(inkomst_tekst, inkomst_tekst_rect)
screen.blit(question_text, question_text_rect)
# prints the options
pos = 0
for i in quiz_set["valgmuligheder"]:
    pos += 50
    question_text = font.render(f"{i['tekst']} : {i['pris']},-", False, (250, 250, 0))
    question_text_rect = penge_tekst.get_rect()
    question_text_rect.topleft = (width // 10, height // 10 + pos)
    screen.blit(question_text, question_text_rect)
pygame.display.flip()

a_selected = True
b_selected = False
c_selected = False
i_selected = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        random.shuffle(quiz_sets)

        # last round
        if event.type == pygame.KEYDOWN and question_id == len(quiz_sets):
            print(question_id)
            print(len(quiz_sets))
            running = False
            quit()

        penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
        inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
        question_text = font.render(f"{quiz_set['spørgsmål']}", False, (250, 250, 0))

        penge_tekst_rect = penge_tekst.get_rect()
        inkomst_tekst_rect = inkomst_tekst.get_rect()
        question_text_rect = question_text.get_rect()

        penge_tekst_rect.bottomright = (width, height)
        inkomst_tekst_rect.bottomleft = (0, height)
        question_text_rect.center = (width // 2, height // 10)

        screen.blit(penge_tekst, penge_tekst_rect)
        screen.blit(inkomst_tekst, inkomst_tekst_rect)
        screen.blit(question_text, question_text_rect)

        if (a_selected):
            a = font.render(f">", False, (250, 250, 0))
            a_rect = a.get_rect()

            a_rect.topleft = (width // 10 - 20, height // 10 + 50 * 1)

            screen.blit(a, a_rect)
        elif (b_selected):
            b = font.render(f">", False, (250, 250, 0))
            b_rect = b.get_rect()

            b_rect.topleft = (width // 10 - 20, height // 10 + 50 * 2)

            screen.blit(b, b_rect)
        elif (c_selected):
            b = font.render(f">", False, (250, 250, 0))
            b_rect = b.get_rect()
            b_rect.topleft = (width // 10 - 20, height // 10 + 50 * 3)

            screen.blit(b, b_rect)
        elif (i_selected):
            b = font.render(f">", False, (250, 250, 0))
            b_rect = b.get_rect()

            b_rect.topleft = (width // 10 - 20, height // 10 + 50 * 4)

            screen.blit(b, b_rect)
        # prints the options
        pos = 0
        for i in quiz_set["valgmuligheder"]:
            pos += 50
            question_text = font.render(f"{i['tekst']} : {i['pris']},-", False, (250, 250, 0))
            question_text_rect = penge_tekst.get_rect()
            question_text_rect.topleft = (width // 10, height // 10 + pos)
            screen.blit(question_text, question_text_rect)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN and question_id != len(quiz_sets):
            if event.key == pygame.K_a:
                a_selected = True
                b_selected = False
                c_selected = False
                i_selected = False
            if event.key == pygame.K_b:
                a_selected = False
                b_selected = True
                c_selected = False
                i_selected = False
            if event.key == pygame.K_c:
                a_selected = False
                b_selected = False
                c_selected = True
                i_selected = False
            if event.key == pygame.K_i:
                a_selected = False
                b_selected = False
                c_selected = False
                i_selected = True

            if event.key == pygame.K_RETURN:
                screen.fill((0,0,0))
                print("fda")
                quiz_set = next_question(quiz_sets, question_id)

                # text on pygame
                penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
                inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
                question_text = font.render(f"{quiz_set['spørgsmål']}", False, (250, 250, 0))

                penge_tekst_rect = penge_tekst.get_rect()
                inkomst_tekst_rect = inkomst_tekst.get_rect()
                question_text_rect = question_text.get_rect()

                penge_tekst_rect.bottomright = (width, height)
                inkomst_tekst_rect.bottomleft = (0, height)
                question_text_rect.center = (width // 2, height // 10)

                screen.blit(penge_tekst, penge_tekst_rect)
                screen.blit(inkomst_tekst, inkomst_tekst_rect)
                screen.blit(question_text, question_text_rect)

                # prints the options
                pos = 0
                for i in quiz_set["valgmuligheder"]:
                    pos += 50
                    question_text = font.render(f"{i['tekst']} : {i['pris']},-", False, (250, 250, 0))
                    question_text_rect = penge_tekst.get_rect()
                    question_text_rect.topleft = (width // 10, height // 10 + pos)
                    screen.blit(question_text, question_text_rect)
                question_id += 1
            if event.key == pygame.K_a:
                print("a")
            pygame.display.flip()

            # it only stops when typed correct
            # run = True
            # while run:
            #     # dette er fra den anden fil
            #     pygame_stuff.progress_bar.update_bar(screen, points)
            #
            #     gaet = "a"
            #
            #     # investing
            #     if gaet.upper() == "I":
            #         # det er defineret ovenfor
            #         gamle_penge, nye_penge, inkomst, pris = choose_crypto(penge, inkomst)
            #         din_inkomst = inkomst
            #         run = False
            #     # checks if it matchs the options
            #     for i in quiz_set["valgmuligheder"]:
            #         # the first letter in the option
            #         if gaet.upper() == i["tekst"][0]:
            #             # checks if you can afford
            #             if penge - i["pris"] >= 0:
            #                 points += int(i["point"])
            #                 # prisen du skal betale
            #                 penge -= i["pris"]
            #                 # evt asset
            #                 inkomst += i["inkomststigning"]
            #                 # du får løn
            #                 penge += inkomst
            #                 run = False
            #             else:
            #                 'print("Du har ikke råd til det")'

            # updates information
            pygame.display.flip()
            screen.fill(color=(0,0,0))

