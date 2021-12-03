import pygame.display
from pygame.locals import *
import pygame_stuff.progress_bar
import random
from sys import exit


def next_question(quiz_sets, index):
    return quiz_sets[index]


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
             "valgmuligheder": [{"tekst": "A. 1Bil", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. 2Bill", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købe?",
             "valgmuligheder": [{"tekst": "A. 3Billl", "point": 2, "pris": 300, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 300, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
            {"spørgsmål": "Hvad vil du helst købeee?",
             "valgmuligheder": [{"tekst": "A. 4Billll", "point": 2, "pris": 100, "inkomststigning": 10},
                                {"tekst": "B. Tog", "point": 5, "pris": 12, "inkomststigning": 7},
                                {"tekst": "C. Hus", "point": 100, "pris": 12, "inkomststigning": 10}],
             "svar": "A"
             },
        ]
investing_sets = [{"option": "A. Bitcoin (stor risiko)", "winning_price": 1 + 1.2, "losing_price": 1 - 1},
                  {"option": "B. Disney (mellem risiko)", "winning_price": 1 + 1/7, "losing_price": 1 - 1/8},
                  {"option": "C. S&P 500 (lille risiko)", "winning_price": 1 + 1/11, "losing_price": 1 - 1/13},]
random.shuffle(quiz_sets)
print(quiz_sets)

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
investing_amount = ""
investing_amount_int = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame_stuff.progress_bar.update_bar(screen, points)
        # if the screen is invest
        if invest_screen:
            screen.fill((0, 0, 0))

            penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
            inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
            question_text = font.render(f"Du kan vælge og investrer i 3 forskellige ting: ", False, (250, 250, 0))

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
            # for typing
            input_rect = pygame.Rect(50, height // 1.9, 140, 32)
            color = (255, 255, 0)
            pygame.draw.rect(screen, color, input_rect, 2)

            if event.type == KEYDOWN:
                if event.key == pygame.K_a:
                    arrow["number"] = 0
                if event.key == pygame.K_b:
                    arrow["number"] = 1
                if event.key == pygame.K_c:
                    arrow["number"] = 2
                if event.key == pygame.K_i:
                    arrow["number"] = 3

                if event.key == pygame.K_BACKSPACE:
                    investing_amount = investing_amount[:-1]
                # accepting numbers
                if event.key == K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    try:
                        if int(investing_amount + event.unicode) <= penge:
                            investing_amount += event.unicode
                            investing_amount_int = int(investing_amount)
                            print(f"invest: {investing_amount}")
                    except:
                        ""
                if event.key == pygame.K_RETURN:
                    if investing_amount != "":
                        sandsynlighed = random.randint(1,10)

                        # they pay for the stock
                        penge -= investing_amount_int

                        # (if option 1)
                        if arrow["number"] == 0:
                            # (youve won)
                            if sandsynlighed <= 3:
                                print("win")
                                penge += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 3:
                                print("lose")
                                penge += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]
                                print(f'{investing_amount_int * investing_sets[arrow["number"]]["losing_price"]}')
                        if arrow["number"] == 1:
                            # (youve won)
                            if sandsynlighed <= 5:
                                penge += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 5:
                                penge += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]
                        if arrow["number"] == 2:
                            # (youve won)
                            if sandsynlighed <= 9:
                                penge += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 10:
                                penge += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]

                        print(penge)
                        # the amount to invest
                        investing_amount = ""

                        # new round
                        screen.fill((0,0,0))
                        invest_screen = False
                        # only start new round if there is another question
                        question_id += 1
                        if question_id < len(quiz_sets):
                            quiz_set = next_question(quiz_sets, question_id)
            text_surface = font.render(investing_amount, True, (255, 255, 0))
            screen.blit(text_surface, input_rect)
            pygame.display.flip()

        # if the screen is normal
        else:
            if event.type == pygame.KEYDOWN:
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
                        # giving points
                        penge -= quiz_set["valgmuligheder"][arrow["number"]]["pris"]
                        points += quiz_set["valgmuligheder"][arrow["number"]]["point"]
                        inkomst += quiz_set["valgmuligheder"][arrow["number"]]["inkomststigning"]

                        arrow["number"] = 0
                        # only start new round if there is another question
                        if question_id < len(quiz_sets):
                            quiz_set = next_question(quiz_sets, question_id)


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
                arrow["color"] = (255, 0, 0)
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

            invester_tekst = font.render(f"I. Investér", False, (250, 250, 0))

            invester_tekst_rect = invester_tekst.get_rect()

            invester_tekst_rect.topleft = (width // 10, height // 10 + 50 * 4)

            screen.blit(invester_tekst, invester_tekst_rect)

            pygame.display.flip()
            screen.fill(color=(0, 0, 0))
            if question_id == len(quiz_sets):
                time.sleep(1)
                running = False
                quit()

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


