import pytest
from cod.main import Calculator
from contextlib import nullcontext as does_not_raise


class TestCaculator:
    @pytest.mark.parametrize(
        "x , y , res",
        [
            (1, 2, 3),
            (5, 1, 6)
        ]
    )
    def test_add(self,x,y,res):
        assert Calculator().add(x, y) == res

    @pytest.mark.parametrize(
        "x , y , res, expectation",
        [
            (1, 2, 2 , does_not_raise()),
            (5, 1, 5, does_not_raise()),
            ('6', 1, "6" , pytest.raises(TypeError))
        ]
    )
    def test_multiplay(self,x,y,res, expectation):
        with expectation:
            assert Calculator().multiply(x,y) == res

    @pytest.mark.parametrize(
        "x , y , res, expectation",
        [
            (18, 3, 6, does_not_raise()),
            (200, 2, 100, does_not_raise()),
            ('6', 1, "6" , pytest.raises(ValueError))
        ]
        )
    def test_divide(self,x,y,res , expectation):
        with expectation:
            assert Calculator().divide(x,y) == res