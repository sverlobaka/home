from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):

    #def setUp(self) -> None:
    #    self.solver = Solver(a=2, b=3)

    #def tearDown(self) -> None:
    #    print("dispose solver", id(self.solver))


    def test_add(self):
        s = Solver(a=2, b=3)
        res = s.add()
        #res = self.solver.add()
        self.assertEqual(res, second=5)

    def test_add_zeros(self):
        s = Solver(a=0, b=0)
        res = s.add()

        self.assertEqual(res, second=0)

    def test_mul(self):
        s = Solver(a=2, b=3)
        res = s.mul()

        self.assertEqual(res, second=6)

    def test_many_add(self):
        for a, b, expected in [
            (2, 3, 5),
            (0, 0, 0),
            (0, 1, 1),
            (3, 2, 5)
        ]:
            with self.subTest(msg="все хорошо"):
                s = Solver(a, b)
                res = s.add()
                self.assertEqual(expected, res)

#Pythest
@pytest.fixture()
def solver_fixture():
    s = Solver(2, 3)
    return s

@pytest.fixture(
    params=[
        pytest.param((2, 3), id="first"),
        pytest.param((0, 0), id="zeros"),
        pytest.param((5, 3)),
        (5, 6),
    ]
)
def solver_multi(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver

@pytest.fixture()
def solver_mix(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver

class TestSolver:
    def test_add(self, solver_fixture):
        res = solver_fixture.add()

        assert res == 5

    def test_mul(self, solver_fixture):
        res = solver_fixture.mul()

        assert res == 6

    def test_mul_many(self, solver_multi):
        res = solver_multi.mul()

        assert res == solver_multi.a * solver_multi.b

#передаем параметры a, b, expected (параметаризация)
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        pytest.param(0, 0, 0, id="zeros"),
        pytest.param(0, 1, 1),
        (3, 2, 5)
    ])
    def test_many_add(self, a, b, expected):
            s = Solver(a, b)
            res = s.add()
            assert res == expected

    @pytest.mark.parametrize("solver_mix, expected", [
        pytest.param(("a", "b"), "ab"),
        pytest.param(("", ""), "", id="empty"),
        pytest.param((2, 3), 5),
    ], indirect=["solver_mix"])
    def test_add_strings(self, solver_mix, expected):
            res = solver_mix.add()
            assert res == expected

def test_data_equal():...

