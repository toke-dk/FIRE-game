import pygame.display
from pygame.locals import *
import pygame_stuff.progress_bar
import random
from sys import exit
import time


def next_question(quiz_sets, index):
    return quiz_sets[index]


def color_decide(number):
    if number >= 0:
        return (0, 255, 0)
    elif number < 0:
        return (255, 0, 0)


def change_in_information(income_change, money_change, total_income):

    income_change_text = font.render(f"{f'+' if income_change >= 0 else ''}{income_change},-", False, color_decide(income_change))
    money_change_text = font.render(f"{f'+' if money_change >= 0 else ''}{money_change},-", False, color_decide(money_change))
    total_income_text = font.render(f"{f'+' if total_income >= 0 else ''}{total_income},-", False, color_decide(total_income))


    income_change_text_rect = income_change_text.get_rect()
    money_change_text_rect = money_change_text.get_rect()
    total_income_text_rect = total_income_text.get_rect()


    money_change_text_rect.bottomright = (screen.get_width(), screen.get_height() - 50)
    total_income_text_rect.bottomright = (screen.get_width(), screen.get_height() - 50)
    income_change_text_rect.bottomleft = (0, screen.get_height() - 50)

    screen.blit(income_change_text, income_change_text_rect)
    screen.blit(money_change_text, money_change_text_rect)
    pygame.display.update(income_change_text_rect)
    pygame.display.update(money_change_text_rect)
    time.sleep(3)
    # displays the new income
    pygame.draw.rect(screen, (0,0,0), total_income_text_rect)
    pygame.draw.rect(screen, (0,0,0), money_change_text_rect)
    screen.blit(total_income_text, total_income_text_rect)
    pygame.display.update(money_change_text_rect)
    pygame.display.update(total_income_text_rect)
    time.sleep(2)
    screen.fill((0,0,0))


width = 1700
height = 900
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("FIRE-spillet")

pygame.display.flip()
running = True

gamle_penge = 0
din_inkomst = 0
nye_penge = 0
pris = 0
question_id = 0
start_screen = True
invest_screen = False
end_screen = False

font = pygame.font.Font("freesansbold.ttf", 32)

quiz_sets = [
            {"sp??rgsm??l": "Du f??ler at du mangler noget. Du har s?? meget lyst til at k??be et eller andet. Hvad vil du "
                          "helst v??lge:",
             "valgmuligheder": [{"tekst": "A. Bil", "point": -10, "pris": 8000, "inkomststigning": -200},
                                {"tekst": "B. Hjemmelavet vaskepulver", "point": 5, "pris": 10, "inkomststigning": 10},
                                {"tekst": "C. B??ger og h??ber du f??r dem l??st", "point": -3, "pris": 50, "inkomststigning": 0}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du har lige f??et den tanke at du m??ske kunne overveje et barn, men er usikker. Hvad v??lger du?",
             "valgmuligheder": [{"tekst": "A. Vent til senere", "point": 4, "pris": 0, "inkomststigning": 0},
                                {"tekst": "B. F?? et barn", "point": -5, "pris": 0, "inkomststigning": -200},
                                {"tekst": "C. L??g penge til siden til et barn", "point": 8, "pris": 0, "inkomststigning": -20}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du vil gerne pr??ve at f?? fat i nogle passiver hvordan f??r du r??d til det?",
             "valgmuligheder": [{"tekst": "A. du pr??ver lykken og spiller lotto 2 gange om ugen", "point": -40, "pris": -100, "inkomststigning": -200},
                                {"tekst": "B. Du arbejder mere s?? du kan tjene flere penge", "point": 5, "pris": 0, "inkomststigning": 15},
                                {"tekst": "C. Du finder steder i din ??konomi hvor du kan spare", "point": 40, "pris": 0, "inkomststigning": 200}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du skal p?? en date. Du har i langt ??nsket dig en k??reste og dette er din mulighed!",
             "valgmuligheder": [{"tekst": "A. Du k??ber en overd??dig middag og scorer hende/ham", "point": -10, "pris": 2000, "inkomststigning": -100},
                                {"tekst": "B. Du tager hende p?? en billig date. S?? scorer hende ikke", "point": 5, "pris": 50, "inkomststigning": 0},
                                {"tekst": "C. Du aflyser daten", "point": 4, "pris": 0, "inkomststigning": 0}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du vil gerne s??tte dig ind i hvordan du kan k??be assets for at blive ??konomisk uafh??ngig, hvad g??r du?",
             "valgmuligheder": [{"tekst": "A. Finder tidspunkter p?? din dag, til at s??tte dig ind", "point": 15, "pris": 0, "inkomststigning": 0},
                                {"tekst": "B. Betaler for et abbonoment, de siger at de kan hj??lpe dig", "point": -40, "pris": 100, "inkomststigning": -60},
                                {"tekst": "C. Du siger op fra dit job, og h??ber p?? at du tager dig sammen", "point": 13, "pris": 0, "inkomststigning": -400}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du har altid ??nsket at dine for??ldre havde mere tid med dig. Hvad vil du g??re nu som voksen?",
             "valgmuligheder": [{"tekst": "A. Blive ved med at arbejde, fordi der jo ikke er andre muligheder", "point": -18, "pris": 0, "inkomststigning": 0},
                                {"tekst": "B. Du k??ber en masse aktiver(assets)", "point": 40, "pris": 400, "inkomststigning": 120},
                                {"tekst": "C. Du arbejder mindre, og f??r mindre i l??n", "point": 6, "pris": 0, "inkomststigning": -200}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du kan k??be en del af en lejlighed, du har allerede en god en i forvejen, hvad g??r du?",
             "valgmuligheder": [{"tekst": "A. K??ber den og lejer den ud til andre", "point": 45, "pris": 400, "inkomststigning": 100},
                                {"tekst": "B. Du kigger p?? den men bruger ingen penge, da du har en i forvejen", "point": 0, "pris": 0, "inkomststigning": 0},
                                {"tekst": "C. K??ber den og fot??ller folk at de kan k??be den billigt", "point": -5, "pris": 600, "inkomststigning": -100}],
             "svar": "A"
             },
            {"sp??rgsm??l": "Du overvejer at sige op for at starte op, for at starte din egen forretning",
             "valgmuligheder": [{"tekst": "A. Du lader v??r med at sige op, fordi du indser at det nok ikke bliver til noget", "point": -10, "pris": 0, "inkomststigning": 0},
                                {"tekst": "B. Du starter virksomhed. Det koster nogle penge, men du tager chancen.", "point": 20, "pris": 800, "inkomststigning": random.randint(-100, 400)},
                                {"tekst": "C. Du siger op, men dropper ideen og bliver ansat i en anden virksomhed.", "point": -15, "pris": 0, "inkomststigning": -10}],
             "svar": "A"
             },

        ]

quiz_set = next_question(quiz_sets, question_id)
points = 0
penge = 200
inkomst = 100

# text on pygame
penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
question_text = font.render(f"{quiz_set['sp??rgsm??l']}", False, (250, 250, 0))

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
        # the invest price is changing
        investing_sets = [{"option": "A. Bitcoin (stor risiko)", "winning_price": 1 + random.uniform(1, 1.6),
                           "losing_price": 1 - random.uniform(0.8, 1)},
                          {"option": "B. Disney (mellem risiko)", "winning_price": 1 + 1 /random.uniform(6, 9),
                           "losing_price": 1 - 1 / random.uniform(7, 10)},
                          {"option": "C. S&P 500 (lille risiko)",
                           "winning_price": 1 + 1 /random.uniform(10, 13),
                           "losing_price": 1 - 1 / random.uniform(12, 14)}, ]
        if start_screen:
            screen.fill((0,0,0))
            start_font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 64)
            start_font_undertext = pygame.font.Font("fonts/PlayfairDisplaySC-Italic.ttf", 30)
            start_text = start_font.render("Fire-spillet", False, (255,255,0))
            under_text = start_font_undertext.render("( Tryk enter for at starte )", False, (255,255,0))
            start_font_undertext_rect = under_text.get_rect()
            start_text_rect = start_text.get_rect()
            start_text_rect.center = (screen.get_width()//2, height//3)
            start_font_undertext_rect.center = (screen.get_width()//2, height//1.5)
            screen.blit(start_text, start_text_rect)
            screen.blit(under_text, start_font_undertext_rect)
            pygame.display.flip()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    start_screen = False
        # if the screen is invest
        elif invest_screen:
            screen.fill((0, 0, 0))

            penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
            inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
            question_text = font.render(f"Du kan v??lge og investrer i 3 forskellige ting: ", False, (250, 250, 0))

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

                        # gevinst
                        gevinst = 0

                        # (if option 1)
                        if arrow["number"] == 0:
                            # (youve won)
                            if sandsynlighed <= 3:
                                print("win")
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 3:
                                print("lose")
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]
                                print(f'Price {investing_sets[arrow["number"]]["losing_price"]}')
                        if arrow["number"] == 1:
                            # (youve won)
                            if sandsynlighed <= 5:
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 5:
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]
                        if arrow["number"] == 2:
                            # (youve won)
                            if sandsynlighed <= 9:
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["winning_price"]
                            elif sandsynlighed > 10:
                                gevinst += investing_amount_int * investing_sets[arrow["number"]]["losing_price"]
                        gevinst = round(gevinst, 1)
                        penge += gevinst
                        penge += inkomst
                        print(f"gevinst{gevinst}")
                        # the amount to invest
                        investing_amount = ""

                        # new round
                        screen.fill((0,0,0))
                        invest_screen = False
                        # only start new round if there is another question
                        question_id += 1
                        arrow["number"] = 0
                        print(gevinst)
                        change_in_information(0, round(gevinst - investing_amount_int, 1), inkomst)
                        if question_id < len(quiz_sets):
                            quiz_set = next_question(quiz_sets, question_id)
                            end_screen = True
            text_surface = font.render(investing_amount, True, (255, 255, 0))
            screen.blit(text_surface, input_rect)
            pygame.display.flip()

        # if the screen is normal
        else:
            screen.fill((0,0,0))
            pygame_stuff.progress_bar.update_bar(screen, points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    arrow["number"] = 0
                if event.key == pygame.K_b:
                    arrow["number"] = 1
                if event.key == pygame.K_c:
                    arrow["number"] = 2

                if event.key == pygame.K_i:
                    arrow["number"] = 3

                if event.key == pygame.K_s:
                    arrow["number"] = 4

                if event.key == pygame.K_RETURN:
                    # if it is the invest option
                    if arrow["number"] == 3:
                        arrow["number"] = 0
                        invest_screen = True
                    elif arrow["number"] == 4:
                      change_in_information(0, 0, inkomst)
                      penge += inkomst
                      arrow["number"] = 0
                      question_id += 1
                      if question_id < len(quiz_sets):
                          quiz_set = next_question(quiz_sets, question_id)
                    elif quiz_set["valgmuligheder"][arrow["number"]]["pris"] < penge:
                        # giving points
                        change_in_information(quiz_set["valgmuligheder"][arrow["number"]]["inkomststigning"],
                                                -quiz_set["valgmuligheder"][arrow["number"]]["pris"],
                                                inkomst)
                        penge -= quiz_set["valgmuligheder"][arrow["number"]]["pris"]
                        penge += inkomst
                        points += quiz_set["valgmuligheder"][arrow["number"]]["point"]
                        inkomst += quiz_set["valgmuligheder"][arrow["number"]]["inkomststigning"]

                        arrow["number"] = 0
                        # only start new round if there is another question
                        question_id += 1
                        if question_id < len(quiz_sets):
                            quiz_set = next_question(quiz_sets, question_id)
                            end_screen = True

            penge_tekst = font.render(f"Penge: {penge},-", False, (250, 250, 0))
            inkomst_tekst = font.render(f"Indkomst: {inkomst},-", False, (250, 250, 0))
            question_text = font.render(f"{quiz_set['sp??rgsm??l']}", False, (250, 250, 0))

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
            if arrow["number"] == 3 or arrow["number"] == 4:
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

            invester_tekst = font.render(f"I. Invest??r", False, (250, 250, 0))
            spar_op_tekst = font.render(f"S. Spar op", False, (250, 250, 0))

            invester_tekst_rect = invester_tekst.get_rect()
            spar_op_tekst_rect = invester_tekst.get_rect()

            invester_tekst_rect.topleft = (width // 10, height // 10 + 50 * 4)
            spar_op_tekst_rect.topleft = (width // 10, height // 10 + 50 * 5)

            screen.blit(invester_tekst, invester_tekst_rect)
            screen.blit(spar_op_tekst, spar_op_tekst_rect)

            pygame.display.flip()
            screen.fill(color=(0, 0, 0))
            if question_id == len(quiz_sets):
                time.sleep(1)
                running = False
                quit()
