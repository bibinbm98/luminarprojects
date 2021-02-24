class pycharm:
    def create_file(self):
        print("create a file pycharm")
    def execute_file(self):
        print("execute of pycharm")

class vscode:
    def create_file(self):
        print("create a file vscode")
    def execute_file(self):
        print("execute of vscode")

class programmer:
    def coding(self,ide):
        ide.create_file()
        ide.execute_file()

cd=pycharm()
pg=programmer()
pg.coding(cd)
