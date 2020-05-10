import allure
import pytest


class TestAllure:
    @allure.step(title='woshiallure')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_allure(self):
        allure.attach("输入1","输入1的描述")
        print(1)
        assert 0


    @allure.step(title='allure1')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure2(self):
        allure.attach("输入2","输入2的描述")
        print(2)