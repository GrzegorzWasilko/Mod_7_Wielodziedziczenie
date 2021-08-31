# Moduł_7.4_wzorzec_projektowy_Mixin________________________________________________________
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s',filename="logfile-runningcount.log")
from faker import Faker
fake=Faker()
#********************************************************************************************

#_____Base_class___________________class__Movie_________________________________Klasa Bazowa
class Movie :
    def __init__(self,title,publication_date,movie_type,):#numb_of_play
        self.title=title                            #____Tytuł________<<-->>_fake.words(nb=3)
        self.publication_date=publication_date      #____Rok wydania__<<-->>______fake.date()
        self.movie_type=movie_type                  #____Gatunek______<<-->>_fake.word(ext_word_list=(['Action','Musical','Historic'])/fake.random_int(min=0, max=15)
#__________________________________Methods____________________________________________________
    def __str__(self):
        return (f'Tytuł: {self.title}, gatunek: {self.movie_type}, premiera: {self.publication_date}')
    @property
    def movie_type (self):
        return self.movie_type
    @movie_type.setter
    def movie_type (self,value):
        type=['Action','Musical','Historic']
        _type=int(value)
        self.movie_type =type[_type]

# metoda self.numb_of_play=numb_of_play#__________Liczba odtworzeń___
# metoda play---------_TODO_________________________ziekszanie odtworzen o 1 



#_____Child_class__________________class__Series_______________________________Klasa Potomna
class Series(Movie):
    def __init__(self,episod_numb,season_numb,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.episod_numb=episod_numb
        self.season_numb=season_numb
        
#        self.numb_of_play=numb_of_play#__________Liczba odtworzeń_______TODO<<<<<<<<<<<<<<<<<<<<
#metoda play---------_TODO
#def __str__(self)

    
#**********************************************************************************************
if __name__ == "__main__":
    logging.info("uruhomiono :")
    print("Bilioteka filmów")
#______________tytuł________rok_wydania___gatunek__nr gatunku z lity w lini 22
film=Movie(fake.words(nb=3),fake.date(),fake.random_int(min=0, max=2))#_______fake.int_to arg dla nr gatunku w property.setter le jest int zamiast str
print(film.title)
print(film)