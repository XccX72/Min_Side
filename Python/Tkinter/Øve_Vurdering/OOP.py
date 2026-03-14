
class Game:
    def __init__(self, name:str, genre:str, published:int, pegi:int):
        self.name = name
        self.genre = genre
        self.published = published
        self.pegi = pegi

    def get_info(self):
        return (f"Name: {self.name} | Genre: {self.genre} | Published: {self.published} | Pegi: {self.pegi}")

    def get_genre(self):
        return (f"Genre: {self.genre}")
    
    def get_published(self):
        return (f"Genre: {self.published}")
    
    def get_pegi(self):
        return (f"Pegi: {self.pegi}")

class Player:
    def __init__(self, name:str, player_id:int, level:int, year_born:int):
        self.name = name
        self.player_id = player_id
        self.level = level
        self.year_born = year_born

    def get_info(self):
        return (f"Name: {self.name} | Player_id: {self.player_id} | Lvl: {self.level} | Year_born: {self.year_born}")
    
    def get_player_id(self):
        return(f"Player_id: {self.player_id}")
    
    def get_level(self):
        return(f"Lvl: {self.level}")
    
    def increase_level(self):
        self.level += 1
        return self.level
    
    def get_age(self):
        a = 2026 - self.year_born
        return a

class Session:
    def __init__(self, session_id:int, game:Game, players:list = []):
        self.session_id = session_id
        self.game = game
        self.players = players
        self.active = True

    def add_player(self, new_player):
        if new_player not in self.players:
            self.players.append(new_player)
        else:
            return(f"Spiller allerede i listen")

    def check_age(self):
        for player in self.players:
            b = player.get_age()
            return b
        
    def end_session(self):
        self.active =False
    
game1 = Game("Sjakk", "brettspill", 0, 5)

p1 = Player("Danni", 1234, 0, 2008)
p2 = Player("Emil", 4321, 67, 1988)
p3 = Player("Aline", 2134, 2, 2001)

s1 = Session(1, game1, [p1, p2])

game1.get_info()
p1.get_info()
s1.check_age()
s1.end_session()



