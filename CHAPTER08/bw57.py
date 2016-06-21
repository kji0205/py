"""pdb를 이용한 대화식 디버깅을 고려하자"""

def complex_func(a, b, c):
	
	import pdb; pdb.set_trace();


complex_func(1, 2, 3)	