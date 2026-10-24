class Player:
    def __init__(self, playerName, playerPosition):
        self._playerName = playerName
        self._playerPosition = playerPosition

class Team:
    def __init__(self, teamName):
        self._teamName = teamName
        self._playerList = []

    def addPlayer(self, player):
        self._playerList.append(player)

    def displayPlayerList(self):
        print("Team Name:", self._teamName)
        print("Players:")

        for player in self._playerList:
            print(player._playerName, "-", player._playerPosition)

#Create Players Objects
player1 = Player("Joe Monatana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

#Adding players on a list
playList = [player1, player2, player3, player4]

team = Team("Smashmouth Football")

for player in playList:
    team.addPlayer(player)

team.displayPlayerList()