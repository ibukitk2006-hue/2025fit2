import pyxel 

pyxel .init(200, 200)
pyxel.cls(7)
for a  in range(0, 360, 1 ):
      c=int(a*7/360)
      pyxel .line(100, 100, 100+100*pyxel.sin(2*a), 100+100*pyxel. cos (3*a), c)
pyxel. show()