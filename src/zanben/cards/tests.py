from django.test import TestCase
from zanben.models import Cards
from scipy.special import comb

class CardsTestCase(TestCase):
    def setUp(self):

    def test_drawCards_lt_numAtleast(self):
        """
        If the number of cards drawn is less than the number of of successes at
        least necessary then we expect 0 probability
        """
        self.assertEqual(compute.compute(deckSize=52,numCardsInCategory=4,numAtLeast=1,numDraws=0), 0)
        self.assertEqual(compute.compute(52,13,1,0), 0)
        self.assertEqual(compute.compute(52,4,1,-1), 0)
        self.assertEqual(compute.compute(52,13,1,-1), 0)
        self.assertEqual(compute.compute(52,4,2,1), 0)
        self.assertEqual(compute.compute(52,13,2,1), 0)
        self.assertEqual(compute.compute(52,4,2,-1), 0)
        self.assertEqual(compute.compute(52,13,2,-1), 0)

    def test_at_least_more_than_1(self):
        """ Compare our values against startrek.com/online-calculator-hypergeometric.aspx """
        self.assertAlmostEqual(compute.compute(52,13,1,10), 0.959813879728687))
        self.assertAlmostEqual(compute.compute(52,13,2,10), 0.785674025219665))
        self.assertAlmostEqual(compute.compute(52,13,3,10), 0.482333633494272))
        self.assertAlmostEqual(compute.compute(52,13,4,10), 0.204271607745995))
        self.assertAlmostEqual(compute.compute(52,13,5,10), 0.0568144728794855))
        self.assertAlmostEqual(compute.compute(52,13,6,10), 0.00997514768659347))
        self.assertAlmostEqual(compute.compute(52,13,7,10), 0.0010533714593759))
        # P(X >= 8) is ~= 6.2e-05 which is too small to bother checking

    def test_prob_three_draws_for_club_from_52_cards(self):
        self.assertAlmostEqual(compute.compute(52,13,1,3), 0.586470588235294))

    def test_prob_3_clubs_52_equals_1_minus_0_clubs_in_52(self):
        self.assertAlmostEqual(compute.compute(52,13,1,3), (1, comb(39,3) / comb(52, 3))))

    def test_prob_1_ace_in_52_1_draw(self):
        self.assertAlmostEqual(compute.compute(52,4,1,1), 4/52))

    def test_prob_1_ace_52_equals_1_minus_0_ace_in_52(self):
        self.assertAlmostEqual(compute.compute(52,4,1,1), (1, comb(48,1) / comb(52,1))))

    def test_probFunc_equals_probFromZero(self):
        self.assertAlmostEqual(compute.compute(52,4,1,1), compute.probFromZero(52,4,1)))
        self.assertAlmostEqual(compute.compute(52,13,1,3), compute.probFromZero(52,13,3)))
        self.assertAlmostEqual(compute.compute(52,4,1,52), compute.probFromZero(52,3,52)))
        self.assertAlmostEqual(compute.compute(52,13,1,52), compute.probFromZero(52,3,52)))

    def test_drawcards_equal_totalCards(self):
        self.assertEqual(compute.compute(52,4,1,52), 1)
        self.assertEqual(compute.compute(52,13,1,52), 1)

class TestScipy:
    def test_comb(self):
        """
        Tests the combination of three cards from a deck of 52 in 52C3 ways
         """
        self.assertEqual(comb(52,3), 22100)
        self.assertEqual(comb(48,1), 48)
        self.assertEqual(comb(52,1), 52)
