# CLASSES 



class cat:
    breed = None
    gender = None
    fun_color = None
    age = None
    weight = None
    height = None
    is_pet = None
    is_tamed = None
    
    def eat(self,food = 'catfood'):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is eating {food}')
    
    def play(self):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is playing')

    def sleep(self):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is sleeping')

billu = cat()
tom = cat()
bangad_billa = cat()


billu.breed = 'persian'
billu.weight = 2
billu.age = 2
billu.fur_color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = 'F'


tom.breed = 'street cat'
tom.weight = 3
tom.age = 2
tom.fur_color = 'grey'
tom.height = 1
tom.is_tamed = True
tom.gender = 'M'


bangad_billa.breed = 'wild cat'
bangad_billa.weight = 5
bangad_billa.age = 6
bangad_billa.fur_color = 'black'
bangad_billa.height = 3
bangad_billa.is_tamed = False
bangad_billa.gender = 'M'

print('billu deatils')
print('breed', billu.breed)
print('gender', billu.gender)
print('age', billu.age)
print('weight', billu.weight)
print('height', billu.height)
print('pet', 'yes' if billu.is_tamed else 'no')
billu.eat()
billu.play()
billu.sleep()



print('tom deatils')
print('breed',tom.breed)
print('gender', tom.gender)
print('age', tom.age)
print('weight', tom.weight)
print('height', tom.height)
print('pet', 'yes' if tom.is_tamed else 'no')
tom.sleep()
tom.play()
tom.sleep()



print('bangadbilla deatils')
print('breed', bangad_billa.breed)
print('gender', bangad_billa.gender)
print('age', bangad_billa.age)
print('weight', bangad_billa.weight)
print('height', bangad_billa.height)
print('pet', 'yes' if bangad_billa.is_tamed else 'no')
bangad_billa.eat('mouse')
bangad_billa.eat('bird')
bangad_billa.sleep()
bangad_billa.eat('bird')














