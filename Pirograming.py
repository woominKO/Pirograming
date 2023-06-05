import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_wins = 0

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Game:
    def __init__(self):
        self.players = []  # 유저들의 목록
        self.deck = []  # 카드 무작위 생성
        self.my_player = ""
    # __init__은 생성자 함수로 초깃값을 설정해준다. 만약 __init__이 아닌 다른 함수이름으로 작명하고
    # self.player에 접근하려고 하면 먼저 다른 함수이름으로 작명한 함수에 초깃값을 수동으로 설정해야 함

    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 1부터 13사이의 숫자의 무작위 숫자를 골라서 30개의 카드로 이루어진 덱을 만듭니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        self.players.append(Player("박신빈"))
        self.players.append(Player("윤정원"))
        self.players.append(Player("임담희"))
        self.players.append(Player("김용현"))

        print("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4) :", end="")
        # TODO 1-(1): 사용자로부터 캐릭터를 입력받아 my_player에 저장해주세요.
        WhichCharacter = int(input())-2
        self.my_player = self.players[WhichCharacter]
        ##### END OF TODO 1-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####
        for i in range(30):
            randomCard = random.randrange(1, 13)
            self.deck.append(randomCard)

        # TODO 1-(2) : 랜덤으로 1부터 13 사이의 카드 30장을 deck에 저장해주세요
        # random에 대한 함수를 공부해봅시다.

        ##### END OF TODO 1-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def set_play_order(self, round_num):
        """ 
        - [ 게임 진행 ] 부분에서 게임진행 순서를 정하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """
        # TODO 2 : 게임진행을 위한 플레이어를 재정렬해주세요.(ROUND 1 : 사전 순서로 이름을 오름차순으로 정렬, ROUND 2,3,4 : 점수를 기준으로 오름차순 정렬)
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        # Write code here..

        if round_num == 1:
            self.players = sorted(self.players, key=lambda x: x.name)
        elif round_num > 1:
            self.players = sorted(self.players, key=lambda x: x.score)

        ##### END OF TODO 2 (문제와 본 라인 사이에 코드를 작성하세요.) #####

    def play_round(self):
        """
        - [ 게임 진행 ] 라운드 진행을 담당하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """

        play_order = ",".join(map(str, self.players))

        print(f"게임은 {play_order} 순으로 진행됩니다.\n")

        # TODO 3-(1) : 카드를 뽑기 전에 self.deck을 랜덤으로 섞어주셔요.
        # Write code here..
        random.shuffle(self.deck)
        ##### END OF TODO 3-(1) (문제와 본 라인 사이에 코드를 작성하세요.) #####

        print("===========플레이어가 뽑은 카드============")
        # TODO 3-(2) : 플레이어들이 카드를 뽑는 부분입니다. 플레이어들이 뽑은 카드를 players_cards에 저장해주시고, 뽑을 때마다 어떠한 카드를 뽑았는지 출력하는 코드를 작성해주세요.
        # Write code here..
        players_card = []
        for i in range(4):
            print(f"{self.players[i]}(현재점수:{self.players[i].score})가 뽑은 카드 ")
            print(f"뽑은카드 {self.deck[-(i+1)]} ")
            players_card.append(self.deck[-(i+1)])

        MaxCard = max(players_card)
        MinCard = min(players_card)
        MaxPlayer = None

        for i, player in enumerate(self.players):
            if self.deck[-(i+1)] == MaxCard:
                MaxPlayer = player
                MaxPlayer.score += MaxCard - MinCard
                MaxPlayer.round_wins += 1
        # ##### END OF TODO 3-(3) (문제와 본 라인 사이에 코드를 작성하세요.) #####

    def play_game(self):
        """
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        for round_num in range(1, 5):

            self.set_play_order(round_num)

            print("===========================")
            print(f"     ROUND {round_num} - START")
            print("===========================")
            self.play_round()

            print("===========================")
            print(f"     ROUND {round_num} - END")
            print("===========================")
            # 라운드 종료 후 각 플레이어들의 현재 점수
            for order, player in enumerate(self.players, 1):
                print(f"{order}. {player} : {player.score}점")
            print()

    def game_result(self):

        # TODO 4-(1) : 점수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 점수")
        print("=============================")

        # Write code here..
        print(f"1.{self.players[0]}:{self.players[0].score} ")
        print(f"2.{self.players[1]}:{self.players[1].score} ")
        print(f"3.{self.players[2]}:{self.players[2].score} ")
        print(f"4.{self.players[3]}:{self.players[3].score} ")

        ##### END OF TODO 4-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

        # TODO 4-(2) : 승리 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 승리 횟수")
        print("=============================")
        # Write code here..
        print(f"1.{self.players[0]}:{self.players[0].round_wins} ")
        print(f"2.{self.players[1]}:{self.players[1].round_wins} ")
        print(f"3.{self.players[2]}:{self.players[2].round_wins} ")
        print(f"4.{self.players[3]}:{self.players[3].round_wins} ")

        ##### END OF TODO 4-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game(self):
        """
        - 게임 운영을 위한 함수입니다. 
        - 별도의 코드 작성이 필요 없습니다. 
        """

        self.start_game()
        self.play_game()
        self.game_result()


if __name__ == "__main__":
    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()

    game.game()
