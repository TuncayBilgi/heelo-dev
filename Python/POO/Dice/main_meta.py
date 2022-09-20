from meta import *

instance = Maclassacorriger()
print(f'compteur = {instance._compteur}')
instance.second = 4
print(f'compteur = {instance._compteur}')
print(f'second = {instance._second}')
print(type(instance))
print(type(Maclassacorriger))
print(Maclassacorriger.__bases__)
print(instance.get_compteur())
print(instance.GET_COmpteur())
print(instance.__dict__)