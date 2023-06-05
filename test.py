import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_wins = 0

    def __str__(self) -> str:
        return f"{self.name}"


class Game:
    def __init__(self):
        self.players = []  # 유저들의 목록
        self.deck = []  # 카드 무작위 생성
        self.my_player = ""

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
        WhichCharacter = int(input()) - 1
        self.my_player = self.players[WhichCharacter]

        for _ in range(30):
            randomCard = random.randrange(1, 13)
            self.deck.append(randomCard)

    def set_play_order(self, round_num):
        """ 
        - [ 게임 진행 ] 부분에서 게임진행 순서를 정하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """
        if round_num == 1:
            self.players.sort(key=lambda x: x.name)
        elif round_num > 1:
            self.players.sort(key=lambda x: x.score)

    def play_round(self):
        """
        - [ 게임 진행 ] 라운드 진행을 담당하는 함수 입니다.
        - 동일 클래스의 play_game()에서 호출됩니다.
        """
        play_order = ",".join(map(str, self.players))
        print(f"게임은 {play_order} 순으로 진행됩니다.\n")

        random.shuffle(self.deck)

        print("===========플레이어가 뽑은 카드============")

        players_card = []
        for i in range(4):
            print(f"{self.players[i]}(현재점수:{self.players[i].score})가 뽑은 카드 ")
            print(f"뽑은카드 {self.deck[-(i+1)]} ")
            players_card.append(self.deck[-(i+1)])

        MaxCard = max(players_card)
        MinCard = min(players_card)
        MaxPlayer = None

        for player in self.players:
            if self.deck[-1] == MaxCard:
                MaxPlayer = player
            player.score = self.deck[-1] - MinCard

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

        self.players.sort(key=lambda x: x.score, reverse=True)
        for rank, player in enumerate(self.players, 1):
            if player == self.my_player:
                print(f"{rank}. *{player}* : {player.score}점")
            else:
                print(f"{rank}. {player} : {player.score}점")

        print()

        # TODO 4-(2) : 승리 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 승리 횟수")
        print("=============================")

        self.players.sort(key=lambda x: x.round_wins, reverse=True)
        for rank, player in enumerate(self.players, 1):
            if player == self.my_player:
                print(f"{rank}. *{player}* : {player.round_wins}승")
            else:
                print(f"{rank}. {player} : {player.round_wins}승")

        print()

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
