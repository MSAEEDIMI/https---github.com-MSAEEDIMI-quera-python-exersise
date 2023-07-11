class Shooter:
    """
    chose and set gun and bullets
    a=Shooter()
    >>>a.set_gun_by_name("Submachine Gun")
    >>>a.add_bullet_of_given_size_to_gun(0.5,10)
    >>>a.shoot_to_target(1,1,15,5,4)
    """
    def __init__(self,name:str="",size:float=0,count:int=0,power:int=0,damage:float=0,bord:int=0) -> None:
        self.name=name
        self.size=size
        self.count=count
        self.power=power
        self.damage=damage
        self.bord=bord
    def guns(self):
        print("Submachine Gun,Assault Rifle,Pistol,Shotgun,Sniper Rifle")
        
    def set_gun_by_name(self, name: str) -> None:
        if name == "Submachine Gun":
            self.name = name
            self.bord=100
            self.power=10
        elif name == "Assault Rifle":
            self.name = name
            self.bord=200
            self.power=20
        elif name == "Pistol":
            self.name = name
            self.bord=80
            self.power=8
        elif name == "Shotgun":
            self.name = name
            self.bord=50
            self.power=40
        elif name == "Sniper Rifle":
            self.name = name
            self.bord=1000
            self.power=30
        else:
            raise Exception

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        """
        Sets the number and amunt of bullets
        size and damage of bullets(1,0,5)(1.5,1)(3,3)(2,4) 
        >>>a.set_gun_by_name("Submachine Gun")
        >>>a.add_bullet_of_given_size_to_gun(0.5,10)
        >>>a.printifo()
        a.set_gun_by_name("Submachine Gun")

        """
        
        if self.name == "Submachine Gun":
            if size != 0.5:
                raise Exception
            else:
                self.damage=1
                self.size = size
            if count < 0:
                raise Exception
            else:
                self.count = count
        elif self.name == "Assault Rifle":
            if size != 1:
                raise Exception
            else:
                self.damage=1.5
                self.size = size
            if count < 0:
                raise Exception
            else:
                self.count = count
        elif self.name == "Pistol":
            if size != 0.5:
                raise Exception
            else:
                self.damage=3
                self.size = size
            if count < 0:
                raise Exception
            else:
                self.count = count
        elif self.name == "Shotgun":
            if self.size != 3:
                raise Exception
            else:
                self.damage=3
                self.size = size
            if count < 0:
                raise Exception
            else:
                self.count = count
        elif self.name == "Sniper Rifle":
            if size != 4:
                raise Exception
            else:
                self.damage=2
                self.size = size
            if count < 0:
                raise Exception
            else:
                self.count = count
        else:
            raise Exception
        
    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        """set distanse and Coordinates"""
        if self.name == "Submachine Gun" and 0<self.count :
            if target_distance >self.bord:
                print(0)    
            else: 
                print(self.damage*self.power)
        elif self.name == "Assault Rifle" and 0<self.count:
            if target_distance >self.bord:
                print(0)    
            else: 
                print(self.damage*self.power)       
        elif self.name == "Pistol" and 0<self.count:
            if target_distance >self.bord:
                print(0)    
            else: 
                print(self.damage*self.power)
        elif self.name == "Shotgun" and 0<self.count:
            if target_distance >self.bord:
                print(0)    
            else: 
                print(self.damage*self.power)
        elif self.name == "Sniper Rifle" and 0<self.count:
            if target_distance >self.bord:
                print(0)    
            else: 
                print(self.damage*self.power)
        else:
            raise Exception
        
