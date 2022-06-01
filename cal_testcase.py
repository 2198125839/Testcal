import pytest
from yamlOperate import yamlOperate
from cal import Calculate
import allure


class Testcal():


    # 获取要执行的所有用例
    case_datas = yamlOperate("./test_case.yaml").readYaml()

    # 获取P0和p1级别的用例
    case_datas_p0 = []
    case_datas_p1 = []
    for case_data in case_datas:
        if case_data["group"] == "p0":
            case_datas_p0.append(case_data)
        else:
            case_datas_p1.append(case_data)


    def setup_class(self):
        print("测试用例开始执行")

    def teardown_class(self):
        print("测试用例结束")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")


    # p0级别的用例集
    @allure.feature('testcal_p0')
    @pytest.mark.p0
    @pytest.mark.parametrize('data', case_datas_p0)
    def testcal_p0(self, data):
        # print("-----------------------------",self.case_datas_p0)
        a, b, c = eval(data["data"])
        cal_return = Calculate().cal(a, b, c)
        print("执行用例：{}".format(data["casename"]))
        assert cal_return == data["assert"]


    # p1级别的用例集
    @allure.feature('testcal_p1')
    @pytest.mark.p1
    @pytest.mark.parametrize('data', case_datas_p1)
    def testcal_p1(self, data):
        a, b, c = eval(data["data"])
        cal_return = Calculate().cal(a, b, c)
        print("执行用例：{}".format(data["casename"]))
        assert cal_return == data["assert"]


if __name__ == "__main__":
    Testcal().testcal()

