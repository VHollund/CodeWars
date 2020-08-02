class Test():
    def assert_equals(x: typing.Any, y: typing.Any, z: str='') -> bool:
        print(x == y)
        if x != y:
            print(x)
            print(y)
            print(z)
            return False
        return True
