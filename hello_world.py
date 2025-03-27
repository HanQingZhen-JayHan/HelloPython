class HelloWorld:
    def __init__(self) -> None:
        self.msg = 'Hello World!'

    def print_msg(self) -> None:
        print(self.msg)

    def set_msg(self, new_msg) -> None:
        self.msg = new_msg

    def get_msg(self):
        return self.msg
        
    def data_structure(self):
        list = []
        list.append(1)
        for dig in list:
            print(dig)
        for index in range(0, len(list)):
            print(list[index])
            
        dictionary = {"key":"value"}
        dictionary["hello"]="world"
        for (k,v) in dictionary.items():
            print("key:{}, value:{}".format(k,v)
        
        _set=set()
        _set.add(1)
        for digit in _set:
            print(digit)

def _is_exist(self,str, policys):
    for policy in policys:
        result = re.search(policy, str)
        if result:
            return True
        return False
def check(self):
    policys=["hello",
             "world"]
    return _is_exist("hell",policys)

def extract(self):
    str = "Hello (World)"
    pattern = r"Hello \((\w+)\).*"
    m = match(pattern,str)
    if m and m.group(1) == "World":
        return "Find {}".format(m.group(1))
    return ''
def read_file(self, file_path):
    with open(file_path, 'rb') as f
         return f.readlines()
    return []
    
def parse_file(self, file_path):
    lines = self.read_files(file_path)
    for line in lines:
        line = line.decode('ISO-8859-1')
        print(line)
if __name__ == '__main__':
    h = HelloWorld()
    h.print_msg()
