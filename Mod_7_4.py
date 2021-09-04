# Moduł_7.4_wzorzec_projektowy_Mixin_nir był potrzebny
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s',filename="logfile-runningcount.log")
from faker import Faker
fake=Faker()
import random
from datetime import date
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
    def __lt__(self, other):
         return self.numb_of_play < other.numb_of_play     
#_______________________________________E_N_D__________________________________________________

#__________________________________class__Series_______________________________Klasa Potomna
class Series(Movie):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.season_numb=f"S{fake.random_int(min=1, max=5):02}"#notacja 2cyfrowa<<<<<<<<<<<<<<<<<<<<<<<<<<<<__TO__DO
        self.episod_numb=f"E{fake.random_int(min=1, max=12):02}"    

    def __str__(self):
        return (f'Title:{self.title},{self.season_numb} {self.episod_numb}')
#__________________________________class__E_N_D______________________________________________
def get_movies(movie_liblary):#_____________________________________________sortowanie  movie
    x=[]
    for movie in movie_liblary:
        if type(movie) ==  Movie :
            x.append(movie)
    x_sort=sorted(x,key=lambda title: title.title)#do nowej listy sortuje piewotna       
    for m in x_sort:   
        print(m)

def get_series(movie_liblary):#_____________________________________________sortowanie series
    x=[]
    for series in movie_liblary:
        if type(series) ==  Series:
            x.append(series)
    x_sort=sorted(x,key=lambda series: series.title)
    for m in x_sort:   
        print(m)

def search(movie_liblary):#___________________________________wyszukuje film z listy po nazwie
    wanted=input("wpisz szukany tytuł : ")
    for x in movie_liblary:
        if x.title[0]  ==  wanted:
            print(f"Pozycja znajduje się w bazie : {x} ")

def generate_vievs(movie_liblary):#___________________losowo od 1 do 100 zwiększa wyswietlenia  
    random.shuffle(movie_liblary)#_________________________________mieszam kolejność elementów 
    for i in range( random.randint(1,100)):#_______________losuje ile razy wywołać "oglądanie"
        movie_liblary[0].generate_vives()#__________________w 1 poz listy zwiększe oglądalność

def generate_vievs_times_10(movie_liblary):#____________________________________10 wyswietlen dodaje
    for i in range(10):
        generate_vievs(movie_liblary)

def top_titles(movie_liblary):  #_____zwraca wybrana ilość najpopularniejszych tytułow z bilioteki
    content_type = input("DLa filmów wybioerz :1, dla Seriali wybierz: 2\n")
    numb = input("wpisz liczbę najlepszych filmów do wyświetlenia\n")
    if content_type == '1':
        lsorted=sorted(movie_liblary, key=lambda movie: movie.numb_of_play,reverse=True)
        for m in range (int(numb)):
            print(f'nr wyświetleń:{lsorted[m].numb_of_play:003},tytuł:{lsorted[m].title}')

    elif content_type == '2':
        lsorted=sorted(movie_liblary, key=lambda series: series.numb_of_play,reverse=True)
        for s in range(int(numb)):
            print(f'nr wyświetleń:{lsorted[s].numb_of_play:003},tytuł:{lsorted[s].title}')

def top_three(movie_liblary) :#___________________________________________________Top_3_______
    top_3=sorted(movie_liblary, key=lambda index: index.numb_of_play,reverse=True)
    for nr in range (3):
        print(f'Top nr{nr+1}:{top_3[nr].numb_of_play:003},tytuł:{top_3[nr].title}')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
if __name__ == "__main__":
    logging.info(f"uruhomiono :")
    print("****************************************\n*******    Bilioteka  filmów     *******\n****************************************")
    movie_liblary=[]
    for x in range(25):#_______________________________________________________________________add_Movies_in_liblary
        x=Movie()
        movie_liblary.append(x)
    for series in range(12):#__________________________________________________________________add_Series_in_liblary
        series=Series()
        movie_liblary.append(series)
    
    #get_movies(movie_liblary)#__________________________________________________________________Find_Movies_in_liblary 
    #get_series(movie_liblary)#__________________________________________________________________Find_Series_in_liblary 
    #search(movie_liblary)#__________________________________________________________________wyszukiwanie _ in_liblary 
    for x in movie_liblary:
        pass#print(x)    
    generate_vievs(movie_liblary)
    generate_vievs_times_10(movie_liblary)
    top_titles(movie_liblary)
    print(f"\n najpopularniejsze produkcje dnia {date.today()}")
    top_three(movie_liblary)
