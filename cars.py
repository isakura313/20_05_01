
from Car import Car
# import Car

jugul = Car("jigul", 120)
del jugul.speed
bmw = Car("bmw", 100)
print(bmw.car_ride())
print(getattr(bmw, 'speed'))
if(hasattr(jugul, 'speed')):
    print('она едет!')
else:
    print("она сломалась")

bmw.speed = 1400
print(bmw.speed)

print(bmw.odometr_reading)

bmw.update_odometr(100)
bmw.odometr_reading()




# print(Car.__dict__)
#
# for attr in dir(bmw):
#     if attr[0] == '_':
#         print(attr)
# for item in bmw.__dict__:
#     print(item, bmw.__dict__[item])
