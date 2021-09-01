# Moduł_7.4_wzorzec_projektowy_Mixin________________________________________________________
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s',filename="logfile-runningcount.log")
from faker import Faker
fake=Faker()
#********************************************************************************************

#_____Base_class___________________class__Movie_________________________________Klasa Bazowa
class Movie :
    def __init__(self,title,publication_date):#numb_of_play
        self.title=title                           #____Tytuł________<<-->>_fake.words(nb=3)
        self.publication_date=publication_date     #____Rok wydania__<<-->>______fake.date()
        self.movie_type=None                       #____Gatunek______<<-->>_fake.word(ext_word_list=(['Action','Musical','Historic'])/fake.random_int(min=0, max=15)
#__________________________________________________#____Liczba odtworzeń_TODO
#__________________________________Methods____________________________________________________
    def __str__(self):
        return (f'Tytuł: {self.title}, gatunek: {self.movie_type}, premiera: {self.publication_date}') #--------lambda do title np lambda:self.movie_type:**args=elf.movie_type.split()
    @property
    def movie_type (self):
        return self._movie_type
    @  movie_type.setter
    def movie_type (self,value):#_value, nie potrzebne i nie wykorzystane setter
        type=['Action','Musical','Historic','Komedy']
        self._movie_type =type[fake.random_int(min=0, max=3)]

# metoda self.numb_of_play=numb_of_play#__________Liczba odtworzeń___
# metoda play---------_TODO_________________________ziekszanie odtworzen o 1 



#_____Child_class__________________class__Series_______________________________Klasa Potomna
class Series(Movie):
    def __init__(self,episod_numb,season_numb,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.episod_numb=episod_numb
        self.season_numb=season_numb
        
# self.numb_of_play=numb_of_play#__________Liczba odtworzeń_______TODO<<<<<<<<<<<<<<<<<<<<
# metoda play---------_TODO
def __str__(self):#nr odcinka i nr sezonu 
    return (f'Tytuł: {self.title}, gatunek: {self.movie_type}, premiera: {self.publication_date}')

#**********************************************************************************************
#**********************************************************************************************
if __name__ == "__main__":
    logging.info("uruhomiono :")
    print("Bilioteka filmów")
#______________tytuł________rok_wydania___gatunek__nr gatunku z lity w lini 22
film=Movie(fake.words(nb=3),fake.year())#,fake.random_int(min=0, max=2))#_______fake.int_to arg dla nr gatunku w property.setter le jest int zamiast str
print(film.title)
print(film.movie_type)
print(film)
print('\n')