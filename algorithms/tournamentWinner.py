class TournamentWinner:
    """
    Time Complexity: O(n)
    Space Complexity: O(k) -> k refers to number of teams in tournament
    """

    def __init__(self, competitions, results):
        self.competitions = competitions
        self.results = results
        self.scores = {"": 0}

    def findBestTeam(self):
        bestTeam = ""

        for index, result in enumerate(self.results):
            matchWinner = self.competitions[index][not result]
            self.__updateScores(matchWinner, 3)

            if self.scores[matchWinner] > self.scores[""]:
                self.scores[""] = self.scores[matchWinner]
                bestTeam = matchWinner

        return bestTeam

    def __updateScores(self, matchWinner, point):
        if matchWinner not in self.scores:
            self.scores[matchWinner] = 0

        self.scores[matchWinner] += point


bestTeam = TournamentWinner(
    [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
print(bestTeam.findBestTeam())
