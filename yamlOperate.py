import yaml

class yamlOperate():
    def __init__(self,yamlFile):
        self.yamlFile=yamlFile

    def readYaml(self):
        with open(self.yamlFile,encoding="utf-8") as f:
            data = yaml.load(f,Loader=yaml.Loader)
        return data



if __name__=="__main__":
    yamlOperate("test_case.yaml").readYaml()