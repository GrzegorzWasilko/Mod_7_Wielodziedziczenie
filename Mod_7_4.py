# Moduł_7.4_wzorzec_projektowy_Mixin________________________________________________________
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s',filename="logfile-runningcount.log")
from faker import Faker
fake=Faker()
#********************************************************************************************
#_____Base_class___________________class__Movie_________________________________Klasa Bazowa
class Movie :
    def __init__(self):                                 
        self.title = fake.texts(nb_texts=1,max_nb_chars=19) #__Tytuł____<<-->>_fake.words(nb=3)
        self.publication_date = fake.year()           #____Rok wydania__<<-->>______fake.date()
        self.movie_type = None                        #____Gatunek______<<-->>______fake.word()
        self.numb_of_play = 0
#________________________________________________________________________________________________
    def __str__(self):
        return (f'Tytuł: {self.title} ( {self.publication_date} )')
    @property
    def movie_type (self):
        return self._movie_type
    @  movie_type.setter
    def movie_type (self,value):
        type=['Action','Musical','Historic','Komedy','Anime']
        self._movie_type =type[fake.random_int(min=0, max=(len(type)-1))]

    def generate_vives(self):
        self.numb_of_play+=1        
#_______________________________________E_N_D__________________________________________________

#__________________________________class__Series_______________________________Klasa Potomna
class Series(Movie):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.season_numb=f"S-{fake.random_int(min=1, max=5)}"#notacja 2cyfrowa<<<<<<<<<<<<<<<<<<<<<<<<<<<<__TO__DO
        self.episod_numb=f"E-{fake.random_int(min=1, max=12)}"    

    def __str__(self):
        return (f'Title:{self.title},{self.season_numb} {self.episod_numb}')
#__________________________________class__E_N_D______________________________________________
def get_movies(movie_liblary):#_____________________________________________sortowanie  movie
    for movie in movie_liblary:
        if type(movie) ==  Movie :
            print(movie)

def get_series(movie_liblary):#_____________________________________________sortowanie series
    for series in movie_liblary:
        if type(series) ==  Series:
            print(series)

def search(movie_liblary):#___________________________________wyszukuje film z listy po nazwie
    wanted=input("wpisz szukany tytuł : ")
    for x in movie_liblary:
        if x.title[0]  ==  wanted:
            print(f"Pozycja znajduje się w bazie : {x} ")
    pass
def generate_vievs(movie_liblary):#_____losowo od 1 do 100 zwiększa wyswietlenia
    pass
def generate_vievs(movie_liblary):#_____10 wyswietlen dodaje
    pass
def top_titles(movie_liblary):  #_____zwraca wybrana ilość najpopularniejszych tytułow z bilioteki
    pass                    #content type - zmienna po której decyduje czy wybieram top filmy czy seriale


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
if __name__ == "__main__":
    logging.info(f"uruhomiono :")
    print("***********************************\n*******  Bilioteka  filmów  *******\n***********************************")
    movie_liblary=[]
    for x in range(25):#_______________________________________________________________________add_Movies_in_liblary
        x=Movie()
        movie_liblary.append(x)
    for series in range(12):#__________________________________________________________________add_Series_in_liblary
        series=Series()
        movie_liblary.append(series)
    
    get_movies(movie_liblary)#__________________________________________________________________add_Movies_in_liblary
    get_series(movie_liblary)#__________________________________________________________________add_Series_in_liblary
    #search(movie_liblary)#__________________________________________________________________wyszukiwanie _ in_liblary
    for x in movie_liblary:
        pass#print(x)    


