# -*- coding: utf-8 -*-
class InvalidCharInResult(Exception):
    pass


class LongGameResult(Exception):
    pass


class ShortGameResult(Exception):
    pass


class CagleCountResult(Exception):
    pass


class PositionChecker:
    VALID_DIGITS = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    VALID_IN_FIRST_POS = ('X', '-', *VALID_DIGITS)
    VALID_IN_SECOND_POS = ('/', '-', *VALID_DIGITS)

    def __init__(self, score_counter):
        self.ScoreCounter = score_counter

    def prepare_char(self):
        char = self.ScoreCounter.game_result[self.ScoreCounter.pos_in_game_result]
        self.ScoreCounter.pos_in_game_result += 1
        return char


class FirstPositionChecker(PositionChecker):
    def __init__(self, score_counter):
        super().__init__(score_counter)

    def check(self):
        char = self.prepare_char()

        if char not in PositionChecker.VALID_IN_FIRST_POS:
            raise InvalidCharInResult("ERROR: InvalidCharIn FirstPosition")
        elif char == 'X':
            return 10
        else:
            self.ScoreCounter.state = self.ScoreCounter.second_pos_checker_state
            if char == '-':
                return 0
            else:
                return int(char)


class SecondPositionChecker(PositionChecker):
    def __init__(self, score_counter):
        super().__init__(score_counter)

    def check(self):
        char = self.prepare_char()

        if char not in PositionChecker.VALID_IN_SECOND_POS:
            raise InvalidCharInResult("ERROR: InvalidCharIn SecondPosition")
        else:
            self.ScoreCounter.state = self.ScoreCounter.first_pos_checker_state
            if char == '/':
                return 15
            elif char == '-':
                return 0
            else:
                return int(char)


class BowlingScoreCounter:

    def __init__(self, game_result):
        self.game_result = game_result
        self.pos_in_game_result = 0
        self.game_scores = 0
        self.game_frames = 0
        self.first_pos_checker_state = FirstPositionChecker(self)
        self.second_pos_checker_state = SecondPositionChecker(self)
        self.state = self.first_pos_checker_state

    def check_frame(self):
        self.game_frames += 1
        result_1 = self.state.check()
        if result_1 == 10:
            return 20  # strike
        else:
            result_2 = self.state.check()
            if result_2 == 15:
                return 15  # spare
            else:
                res = result_1 + result_2
                if 0 <= res <= 10:
                    return res
                else:
                    raise CagleCountResult("ERROR: Invalid CagleCount")

    def run(self):
        self.pos_in_game_result = 0
        self.game_scores = 0
        self.game_frames = 0
        while self.pos_in_game_result < len(self.game_result):
            self.game_scores += self.check_frame()

        if self.game_frames > 10:
            raise LongGameResult("ERROR: LongGameResult")
        elif self.game_frames < 10:
            raise ShortGameResult("ERROR: ShortGameResult")

        return self.game_scores


def get_score(game_result):
    bc = BowlingScoreCounter(game_result)
    result = -1
    try:
        result = bc.run()
    except (InvalidCharInResult, LongGameResult, ShortGameResult, CagleCountResult) as exc:
        # print(exc)
        pass
    finally:
        return result
