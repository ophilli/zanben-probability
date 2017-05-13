import demo
from scipy.special import comb

class TestDemos:
    def test_drawCards_lte_0(self):
        assert demo.probFunc(52,4,0) == 0
        assert demo.probFunc(52,13,0) == 0
        assert demo.probFunc(52,4,-1) == 0
        assert demo.probFunc(52,13,-1) == 0
    def test_prob_three_draws_for_club_from_52_cards(self):
        assert abs(demo.probFunc(52,13,3) - 0.58647058823529408) < 1e-6

    def test_prob_3_clubs_52_equals_1_minus_0_clubs_in_52(self):
        assert abs(demo.probFunc(52,13,3) - (1 - comb(39,3) / comb(52, 3))) < 1e-6

    def test_prob_1_ace_in_52_1_draw(self):
        assert abs(demo.probFunc(52,4,1) - 4/52) < 1e-6

    def test_prob_1_ace_52_equals_1_minus_0_ace_in_52(self):
        assert abs(demo.probFunc(52,4,1) - (1 - comb(48,1) / comb(52,1))) < 1e-6

    def test_probFunc_equals_probFromZero(self):
        assert abs(demo.probFunc(52,4,1) - demo.probFromZero(52,4,1)) < 1e-6
        assert abs(demo.probFunc(52,13,3) - demo.probFromZero(52,13,3)) < 1e-6
        assert abs(demo.probFunc(52,4,52) - demo.probFromZero(52,3,52)) < 1e-6
        assert abs(demo.probFunc(52,13,52) - demo.probFromZero(52,3,52)) < 1e-6

    def test_drawcards_equal_totalCards(self):
        assert demo.probFunc(52,4,52) == 1
        assert demo.probFunc(52,13,52) == 1

class TestScipy:
    def test_comb(self):
        """
        Tests the combination of three cards from a deck of 52 in 52C3 ways
        """
        assert comb(52,3) == 22100
        assert comb(48,1) == 48
        assert comb(52,1) == 52
