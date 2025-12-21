import math

ang=float(input('digite o angulo que você deseja:'))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('O angulo de {} tem seno de {:.2f}'.format(ang,sen))
print('O angulo de {} tem coseno de {:.2f}'.format(ang,cos))
print('O angulo de {} tem tangente de {:.2f}'.format(ang,tan))