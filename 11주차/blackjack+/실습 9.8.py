# 요구사항
# 1 .게임을 시작하면 "Welcomt to Softopia Casino" 다음과 같은 환영 메시지를 실행창에 프린트한다.
# 2. 카드는 1벌(52장)을 잘 섞어서 사용한다. 다 쓰면 1벌을 새로 만들어 다시 잘 섞어서 사용한다.
# 3. 카드는 처음 2장씩 나누어 주는데, 손님, 딜러, 손님, 딜러 순으로 나누어주고, 딜러의 첫 카드는 감춘다.
# 4. 카드는 spade J와 같은 형식으로 한 줄에 한 장씩 텍스트로 실행창에 프린트한다.
# 5. 감추는 카드는 **** ** 로 프린트한다.
# 6. 딜러의 카드를 먼저 다음과 같은 형식으로 보여 준다.
## My cards are:
##   **** **
##   Heart 7
# 7. 그리고 손님의 카드를 다음과 같은 형식으로 보여준다.
## Your cards are:
##    Spade A
##    Diamond K
# 8. 손님은 점수가 21점 미만인 경우 카드를 추가로 요청할 수 있다. 
# 9. 손님에게 다음과 같이 추가 카드를 원하는지 물어봐야 하며, 손님은 y(예) 또는 n(아니오)로 의사를 표시한다. (뒷부분 밑줄은 빈칸을 표시)
## Hit? (y/n)_
# 10. 받은 카드는 다음과 같은 요령으로 바로 보여줘야 한다. (앞부분 밑줄은 빈칸을 표시)
## _Club Q
# 11. 딜러는 카드의 합이 16점 이하이면 카드를 추가로 한 장 무조건 받아야 하며, 16점을 넘으면 더 이상 받을 수 없다.
# 12. A(에이스)는 1점 또는 11점 중 하나를 유리한 똑으로 선택할 수 있어야 한다. 
# 13. 손님이 이기면 You won.을 프린트하고 다음 라운드로 넘어간다. 그런데 첫 두장의 합이 21이 되어 블랙잭으로 이기면 Blackjack! You won.을, 딜러의 버스트로 이기면 I bust! You won.을 프린트한다.
# 14. 딜러가 이기면 I won.을 프린트하는데, 손님의 버스트로 이기면 You bust! I won.을 프린트한다.
# 15. 비기면 We draw.를 프린트한다.
# 16. 손님이 버스트로 진 경우를 제외하고 라운드의 종료와 함께 딜러의 카드를 모두 보여준다.
# 17. 손님이 소지하고 있는 칩의 개수를 매 라운드마다 알려주어야 한다. 게임 시작할 때 0개에서 시작하여 매 라운드마다 손님이 이기면 1개씩 증가하고, 지면 1개씩 감소한다. 블랙잭으로 이기면 2개씩 증가한다. 딜러는 블랙잭으로 이겨도 보너스가 없다. 손님이 보유하고 있는 칩의 개수는 매 라ㅋ운드의 말미에 Chips = 6과 같은 형식으로 보여주어야 한다.
# 18. 매 라운드마다 게임을 계속할지 아래와 같은 형식으로 물어봐야 하며(뒷부분 밑줄은 빈칸을 표시), 손님음 y 또는 n으로 의사를 표시한다.
## Play More? (y/n)_
# 19. 매 라운드 사이의 구분을 위해서 새 라운드는 -----로 시작을 표시한다.
# 20. 게임을 마치면 다음과 같은 이별 메시지를 프린트한다.
## Bye!


# 블랙잭+ 알고리즘
# 1. 환영인사를 프린트한다.
## print("Welcomt to Softopia Casino")
# 2. members.csv 파일에서 멤버 기록을 읽고 로그인 절차를 통해서 사용자이름, 게임시도 횟수, 이긴 횟수, 칩 보유개수, 전체 멤버 딕셔너리 정보를 수집한다.
## username, tries, wins, chips, members = login(load_members())
# 3. 잘 섞은 카드 1벌을 준비한다.
## deck = fresh_deck()
# 4. 손님이 원하는 한, 단계 5~14를 반복한다.
# 5. 카드를 1장씩 손님, 딜러, 손님, 딜러 순으로 배분한다.
## dealer = []
## player = []
## card, deck = hit(deck) # 1장 뽑아서
## player.append(card) # 손님에게 주고
## card, deck = hit(deck) # 1장 뽑아서
## dealer.append(card) # 딜러에게 주고
## card, deck = hit(deck) # 1장 뽑아서
## player.append(card) # 손님에게 주고
## card, deck = hit(deck) # 1장 뽑아서
## dealer.append(card) # 딜러에게 준다.
# 6. 딜러의 첫 카드를 제외하고 모두 보여준다.
## print("My caards are:")
## print(" ", "****", "**")
## print(" ", dealer[1][0], dealer[1][1])
# 7. 손님의 카드를 보여준다.
## show_cards(player, "Your cards are:")
# 8. 손님과 딜러의 카드 두 장의 합을 각각 계산한다.
## score_player = count_score(player)
## score_dealer = count_score(dealer)
# 9. 손님의 카드의 합 score_player가 21이면 블랙잭으로 손님이 이긴다. chips에 2를 더한다.
# 10. 손님의 카드 합이 21을 넘지 않는 한 손님이 원하면 카드를 더 준다. 21을 넘으면 손님이 버스트되어 딜러가 이기고 chips에서 1을 뺀다.
# 11. 손님의 카드 합이 21을 넘지 않았으면, 딜러의 차례이다. 딜러의 카드 합을 계산하여 16 이하이면 16이 넘을 때까지 무조건 카드를 더 받고, 17 이상이 되는 순간 더 이상 받지 않는다.
# 12. 딜러의 카드 합이 21을 넘으면 딜러가 버스트 되어 손님이 이기고 chips에 1을 더한다.
# 13. 둘 다 21이 넘지 않으면 큰 쪽이 이긴다. 손님이 이기면 chips에 1을 더하고, 딜러가 이기면 chips에서 1을 빼고, 비기면 변동 없다.
# 14. 더 할지 손님에게 물어봐서 그만하길 원하면 끝낸다.
# 15. 게임이 진행되는 동안 승패 횟수와 칩의 휙득 개수를 추적하여, 게임이 끝난 뒤 결과를 멤버 딕셔너리에 적용하여 수정하고, members.csv 파일에 저장한다.
# 16. 해당 세션의 게임 결과를 다음과 같이 요약하여 보여준다.
## You played 21 games and won 11 of them.
## Your winning percentage taday is 52.4%
# 17. 지금까지의 칩 최다 보유 멤버를 5명까지 보여준다.
## show_top5(members)

from cardgame import *

def blackjack():
    print("Welcome to Softopia Casino")
    username, tries, wins, chips, members = login(load_members())
    deck = fresh_deck()
    play = 0
    win = 0
    while True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)      
        print("My cards are:")
        print("  **** **")
        print(" ", dealer[1][0], dealer[1][1])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            print("Blackjack! You won.")
            chips += 2
            win += 1
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card[0], card[1])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                    win += 1
                elif score_dealer == score_player:
                    print("We draw.")
                    win += 0.5
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                    win += 1
                else:
                    print("I won.")
                    chips -= 1
        print("Chips =", chips)
        play += 1
        if not more("Play more? (y/n) "):
            break
    print("-----")
    print("You played", play, "games and won", win, "of them")
    wpercent = 100 * win / play if play > 0 else 0    
    print("Your winning percentage today is", "{0:.1f}".format(wpercent), "%")
    tries += play
    wins += win
    members[username] = (members[username][0], tries, wins, chips)
    store_members(members)
    show_top5(members)
    print("Bye!")

blackjack()