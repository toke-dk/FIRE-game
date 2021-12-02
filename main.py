import pygame.display
from pygame.locals import *
import pygame_stuff.progress_bar
import random
from sys import exit


def next_question(quiz_sets, index):
    return quiz_sets[index]


def invest_option(penge, inkomst):
    screen.fill((0,0,0))
    penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
    inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
    question_text = font.render(f"Du kan vælge og investerer i 3 forskellige risici: ", False, (250, 250, 0))

    penge_tekst_rect = penge_tekst.get_rect()
    inkomst_tekst_rect = inkomst_tekst.get_rect()
    question_text_rect = question_text.get_rect()

    penge_tekst_rect.bottomright = (width, height)
    inkomst_tekst_rect.bottomleft = (0, height)
    question_text_rect.center = (width // 2, height // 10)

    screen.blit(penge_tekst, penge_tekst_rect)
    screen.blit(inkomst_tekst, inkomst_tekst_rect)
    screen.blit(question_text, question_text_rect)

    # the arrow
    if arrow["number"] == 3:
        arrow["color"] = (255, 255, 0)
    elif quiz_set["valgmuligheder"][arrow["number"]]["pris"] > penge:
        arrow["color"] = (255, 0, 0)
    else:
        arrow["color"] = (255, 255, 0)

    arrow_text = font.render(f">", False, arrow["color"])
    arrow_text_rect = arrow_text.get_rect()
    arrow_text_rect.topleft = (width // 10 - 20, height // 10 + 50 * (arrow["number"] + 1))
    screen.blit(arrow_text, arrow_text_rect)
    # '
    # gevinst = 0
    # while True:
    #     while True:
    #         if type_invest.lower() == "a" or type_invest.lower() == "b" or type_invest.lower() == "c":
    #             break
    #         else:
    #             'print("Det skal være et af valgmulighederne")'
    #     while True:
    #         try:
    #             if beloeb > penge:
    #                 print('Du har ikke råd')
    #                 continue
    #             elif type(beloeb) != int:
    #                 continue
    #             break
    #         except:
    #             continue
    #     sandsynlighed = random.randint(1, 10)
    #     # the award system
    #     if type_invest.lower() == "a":
    #         if sandsynlighed <= 2:
    #             gevinst = beloeb
    #         elif sandsynlighed > 2:
    #             gevinst = -(beloeb/2)
    #         break
    #     elif type_invest.lower() == "b":
    #         if sandsynlighed <= 5:
    #             gevinst = beloeb/7
    #         elif sandsynlighed > 5:
    #             gevinst = beloeb/8
    #         break
    #     elif type_invest.lower() == "c":
    #         if sandsynlighed <= 9:
    #             gevinst = beloeb/11
    #         elif sandsynlighed > 9:
    #             gevinst = beloeb/13
    #         break
    # gevinst = int(gevinst)
    # if gevinst < 0:
    #     'print(f"Fordi din investering ikke gik så godt, er din inkomst nu faldet med {gevinst}")'
    # elif gevinst > 0:
    #     'print(f"Din investering går rigtig godt, så din inkomst er steget med {gevinst}")'
    # elif gevinst == 0:
    #     'print("Din investering har desværre ikke gjort noget for dig så din inkomst er ikke steget")''
    #
    # inkomst += int(gevinst)
    # gamle_penge = penge
    # penge -= beloeb
    # nye_penge = penge
    # din_inkomst = inkomst
    # pris = beloeb
    if event.type == KEYDOWN:
        if event.key == K_a:
            print("aaa")
            return False
        pygame.display.flip()


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
invest_screen = False

font = pygame.font.Font("freesansbold.ttf", 32)

quiz_sets = [
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bil", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Bill", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. Billl", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 300, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købeee?",
             "valgmuligheder": [{"tekst": "A. Billll", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
        ]
investing_sets = [{"option": "A. Bitcoin (stor risiko)", "winning_price": 1 + 1, "losing_price": 1 - 1/2},
                  {"option": "B. Disney (mellem risiko)", "winning_price": 1 + 1/7, "losing_price": 1 - 1/8},
                  {"option": "C. s&p500 (lille risiko)", "winning_price": 1 + 1/11, "losing_price": 1 - 1/13},]
random.shuffle(quiz_sets)

quiz_set = next_question(quiz_sets, question_id)
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

arrow = {"is_selected" : True, "number" : 0, "color" : (255,255,0)}
random.shuffle(quiz_sets)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if the screen is invest
        if invest_screen:
            screen.fill((0, 0, 0))

            penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
            inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
            question_text = font.render(f"Du kan vælge og investerer i 3 forskellige ting: ", False, (250, 250, 0))

            penge_tekst_rect = penge_tekst.get_rect()
            inkomst_tekst_rect = inkomst_tekst.get_rect()
            question_text_rect = question_text.get_rect()

            penge_tekst_rect.bottomright = (width, height)
            inkomst_tekst_rect.bottomleft = (0, height)
            question_text_rect.center = (width // 2, height // 10)

            screen.blit(penge_tekst, penge_tekst_rect)
            screen.blit(inkomst_tekst, inkomst_tekst_rect)
            screen.blit(question_text, question_text_rect)

            arrow["color"] = (255, 255, 0)
            arrow_text = font.render(f">", False, arrow["color"])
            arrow_text_rect = arrow_text.get_rect()
            arrow_text_rect.topleft = (width // 10 - 20, height // 10 + 50 * (arrow["number"] + 1))
            screen.blit(arrow_text, arrow_text_rect)

            # options
            pos = 0
            for investing_set in investing_sets:
                pos += 50
                investing_text = font.render(f"{investing_set['option']}", False, (250, 250, 0))
                investing_text_rect = investing_text.get_rect()
                investing_text_rect.topleft = (width // 10, height // 10 + pos)
                screen.blit(investing_text, investing_text_rect)

            if event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    arrow["number"] = 0
                if event.key == pygame.K_b:
                    arrow["number"] = 1
                if event.key == pygame.K_c:
                    arrow["number"] = 2

                if event.key == pygame.K_i:
                    arrow["number"] = 3

                if event.key == pygame.K_RETURN:
                    # new round
                    screen.fill((0,0,0))
                    invest_screen = False
                    question_id += 1
                    quiz_set = next_question(quiz_sets, question_id)
            pygame.display.flip()
            # '
            # gevinst = 0
            # while True:
            #     while True:
            #         if type_invest.lower() == "a" or type_invest.lower() == "b" or type_invest.lower() == "c":
            #             break
            #         else:
            #             'print("Det skal være et af valgmulighederne")'
            #     while True:
            #         try:
            #             if beloeb > penge:
            #                 print('Du har ikke råd')
            #                 continue
            #             elif type(beloeb) != int:
            #                 continue
            #             break
            #         except:
            #             continue
            #     sandsynlighed = random.randint(1, 10)
            #     # the award system
            #     if type_invest.lower() == "a":
            #         if sandsynlighed <= 2:
            #             gevinst = beloeb
            #         elif sandsynlighed > 2:
            #             gevinst = -(beloeb/2)
            #         break
            #     elif type_invest.lower() == "b":
            #         if sandsynlighed <= 5:
            #             gevinst = beloeb/7
            #         elif sandsynlighed > 5:
            #             gevinst = beloeb/8
            #         break
            #     elif type_invest.lower() == "c":
            #         if sandsynlighed <= 9:
            #             gevinst = beloeb/11
            #         elif sandsynlighed > 9:
            #             gevinst = beloeb/13
            #         break
            # gevinst = int(gevinst)
            # if gevinst < 0:
            #     'print(f"Fordi din investering ikke gik så godt, er din inkomst nu faldet med {gevinst}")'
            # elif gevinst > 0:
            #     'print(f"Din investering går rigtig godt, så din inkomst er steget med {gevinst}")'
            # elif gevinst == 0:
            #     'print("Din investering har desværre ikke gjort noget for dig så din inkomst er ikke steget")''
            #
            # inkomst += int(gevinst)
            # gamle_penge = penge
            # penge -= beloeb
            # nye_penge = penge
            # din_inkomst = inkomst
            # pris = beloeb
        # if the screen is normal
        else:
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

            # the arrow
            if arrow["number"] == 3:
                arrow["color"] = (255, 255, 0)
            elif quiz_set["valgmuligheder"][arrow["number"]]["pris"] > penge:
                arrow["color"] = (255, 0,0)
            else:
                arrow["color"] = (255, 255, 0)

            arrow_text = font.render(f">", False, arrow["color"])
            arrow_text_rect = arrow_text.get_rect()
            arrow_text_rect.topleft = (width // 10 - 20, height // 10 + 50 * (arrow["number"] + 1))
            screen.blit(arrow_text, arrow_text_rect)

            # prints the options
            pos = 0
            for i in quiz_set["valgmuligheder"]:
                pos += 50
                question_text = font.render(f"{i['tekst']} : {i['pris']},-", False, (250, 250, 0))
                question_text_rect = penge_tekst.get_rect()
                question_text_rect.topleft = (width // 10, height // 10 + pos)
                screen.blit(question_text, question_text_rect)

            invester_tekst = font.render(f"I. Invester", False, (250, 250, 0))

            invester_tekst_rect = invester_tekst.get_rect()

            invester_tekst_rect.topleft = (width // 10, height // 10 + 50 * 4)

            screen.blit(invester_tekst, invester_tekst_rect)

            pygame.display.flip()

            if event.type == pygame.KEYDOWN and question_id != len(quiz_sets):
                if event.key == pygame.K_a:
                    arrow["number"] = 0
                if event.key == pygame.K_b:
                    arrow["number"] = 1
                if event.key == pygame.K_c:
                    arrow["number"] = 2

                if event.key == pygame.K_i:
                    arrow["number"] = 3

                if event.key == pygame.K_RETURN:
                    # if it is the invest option
                    if arrow["number"] == 3:
                        arrow["number"] = 0
                        invest_screen = True
                    elif quiz_set["valgmuligheder"][arrow["number"]]["pris"] < penge:
                        arrow["number"] = 0
                        print(quiz_set["valgmuligheder"][arrow["number"]]["pris"])
                        print(penge)
                        quiz_set = next_question(quiz_sets, question_id)
                        question_id += 1

                if event.key == pygame.K_a:
                    print("a")
                pygame.display.flip()
                pygame.display.flip()
                screen.fill(color=(0, 0, 0))

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


