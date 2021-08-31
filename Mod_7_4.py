# Moduł_7.4_wzorzec_projektowy_Mixin________________________________________________________
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s',filename="logfile-runningcount.log")
from faker import Faker
fake=Faker()
#___________________________________________________________________________________________

#_____Base_class___________________class__Movie_________________________________Klasa Bazowa
class Movie :
    def __init__(self,title,publication_date,movie_type,):#numb_of_play
        self.title=title                                         #_________________Tytuł__fake.words(nb=3)
        self.publication_date=publication_date                   #_________Rok wydania__<<-->> fake.date()
        self.movie_type=movie_type                               #___________________Gatunek

#        self.numb_of_play=numb_of_play#__________Liczba odtworzeń_______TODO<<<<<<<<<<<<<<<<<<<<
#metoda play---------_TODO

#_____Child_class__________________class__Series_______________________________Klasa Potomna
class Series(Movie):
    def __init__(self,episod_numb,season_numb,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.episod_numb=episod_numb
        self.season_numb=season_numb
        
#        self.numb_of_play=numb_of_play#__________Liczba odtworzeń_______TODO<<<<<<<<<<<<<<<<<<<<
#metoda play---------_TODO

    

if __name__ == "__main__":
    logging.info("uruhomiono :")
    print("Bilioteka filmów")
#___________tytuł____________rok_wydania__gatunek__
film=Movie(fake.words(nb=3),fake.date(),'dramat')
print(film.title)