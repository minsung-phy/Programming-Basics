# ValueError, IndexError, KeyError 예외를 발생시키는 사례를 각각 실행창에서 만들어 확인하자.

# ValueError
num = int("python")

# IndexError
a = ['a', 'b', 'c', 'd', 'e']
a[50]

# KeyError
me = {"name": "이민성", "bir": "2003", "email": "chocomin0211@hanyang.ac.kr"}
phonenum = me["phonenum"]