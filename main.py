class Game:
    def __init__(self, Playerlist, Rules):
        self.Playerlist = Playerlist #List of Players (Player[])
        self.Rules = Rules #Rules of the Game (Dictionary)

    #All Accessors
    def getPlayerlist(self):
        return self.Playerlist
    def getRules(self):
        return self.Rules

    #Methods
    def evolve(self):
        """TO DO LATER""" #Bc im fucking bored
        pass

class Pokemon:
    def __init__(self, name, HP, Elem, Attacks, LevelEvolve):
        self.name = name #Name of the Pokémon (str)
        self.HP = HP #HP of the Pokémon (float)
        self.evolveStage = 0 #The evolving stage of the Pokémon (int)
        self.Elem = Elem #Element of the Pokémon (str)
        self.lvl = 0 #The level of the Pokémon (int)
        self.xp = 0 #The XP of the Pokémon (int)
        self.Attack = Attacks #The Attacks of the Pokémon (Attack[])
        self.LevelEvolve = LevelEvolve #The level until evolution of the Pokémon (int[])
        self.maxHP = HP #The maximum HP of the Pokémon (int)
        #TEMPORARY VALUES
        self.xpUpgrade = [10, 15, 20, 25, 30, 35]

    #All Accessors
    def getHP(self):
        return self.HP
    def getName(self):
        return self.name
    def evolveStage(self):
        return self.evolveStage
    def getElem(self):
        return self.Elem
    def getLvl(self):
        return self.Elem
    def getXP(self):
        return self.xp
    def getAttack(self):
        return self.Attacks
    def getLevelEvolve(self):
        return self.LevelEvolve
    def getMaxHP(self):
        return self.maxHP
    def getXPUpgrade(self):
        return self.xpUpgrade

    #Methods
    def evolve(self):
        """FUNCTION SHOULDNT BE HERE TO BE CHANGED TO GAME""" #TO BE CHANGED TO GAME
        if self.lvl >= (self.evolveStage + 1) * self.LevelEvolve[i]:
            self.evolveStage += self.evolveStage
    def upgrade(self): #Adds a level to the Pokémon
        self.lvl += 1
        self.upgradeHP() #Adds more HP to the Pokémon
        for attack in self.Attacks: #Adds more damage to the Attacks
            attack.upgrade()
        self.xp = 0 #Resets the xp
    def addXP(self, XP): #Adds XP to the Pokémon
        self.xp += XP
        if xpUpgrade[self.lvl] >= self.xp: #If enough xp is needed to level up -> upgrade
            upgrade(self.lvl)
    def addHP(self, HP): #Adds HP to the Pokémon
        self.HP += HP
        if self.HP > self.maxHP: #Makes a new maxHP because the HP increased
            self.HP = self.maxHP
    def AddAttacks(self, Attacks): #Adds an attack to the Pokémon
        if len(Attacks) < 4: #Limits the amount of attacks
            self.Attacks.append(Attacks)
    def RemoveAttacks(self, Attacks): #Removes an attack from the Pokémon
        self.Attacks.remove(Attacks)
    def upgradeHP(self): #Upgrades the HP of the Pokémon at level up
        self.HP *= 1.01

    def __str__(self): #Gives the description of the Pokémon
        return f"HP : {self.HP} on Max HP : {self.maxHP}, Name : {self.name}, Elem : {self.Elem}, Evolution Stage : {self.evolveStage}, Attacks : {self.Attack}, Xp : {self.xp}/{self.xpUpgrade}, lvl {self.lvl} Until Evolve : {self.LevelEvolve[self.evolveStage]};"

class Attack:
    def __init__(self, damage, name, description, element): #Init
        self.damage = damage #The Base Attack's damage (float)
        self.name = name #The Attack's name (str)
        self.element = element #The Attack's element (str)
        self.description = description #The Attack's description (str)

    #All accessors
    def getDamage(self):
        return self.damage
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getElement(self):
        return self.element

    #Methods
    def upgradeAttack(self): #Upgrades the attack for the level up
        self.damage *= 1.01
    def __str__(self): #Gives the description of the attack
        return f"Damage : {self.damage}, Name : {self.name}, Description : {self.description}, Element : {self.element}"

class Pokedex:
    def __init__(self, Pokelist): #Init
        self.Pokelist = Pokelist

    #All Accessors
    def getPokedex(self):
        return self.Pokelist

    #Methods
    def addPokemon(self, pokemon): #Adds a Pokémon to the Pokédex
        self.Pokelist.append(pokemon)

class Item:
    def __init__(self, name, price, description): #Init
        self.name = name #Item's name (str)
        self.price = price #Item's Price (int)
        self.description = description #The Item's description (str)

    #All Accessors
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getDescription(self):
        return self.description

    #Methods
    def __str__(self): #Gives the description of the item
        return f"Name : {self.name}, Price : {self.price}, Description : {self.description}"

class Player:
    def __init__(self, name, pokedex, inventory, Id, lvl, xp, money, poketeam, pokelist): #Init
        self.pokelist = pokelist #List of Pokémon Base Empty (Pokemon[])
        self.name = name #Discord Name (str)
        self.pokedex = pokedex #List of Pokémon Base Empty (Pokédex)
        self.poketeam = poketeam #List of Pokémon Base Empty (Pokemon[]) (max 6)
        self.inventory = inventory #List of Items Base Empty (Item[])
        self.id = Id #Discord ID (int or str)
        self.lvl = lvl #Base Lvl 0 (int)
        self.xp = xp #Base XP 0 (int)
        self.money = money #Base Money 100 bucks (int)
        #TEMPORARY VALUES
        self.xpUpgrade = [10, 15, 20, 25, 30, 35, 40, 50, 60] #The xp that is needed to level up the player for each level the player has (int[])

    #All Accessors
    def getInventory(self):
        return self.inventory
    def getName(self):
        return self.name
    def getPokedex(self):
        return self.pokedex
    def getPoketeam(self):
        return self.poketeam
    def getId(self):
        return self.id
    def getLvl(self):
        return self.lvl
    def getXP(self):
        return self.xp
    def getMoney(self):
        return self.money
    def getXPUpgrade(self):
        return self.xpUpgrade
    def getPokelist(self):
        return self.pokelist

    #Methods
    def upgrade(self): #Upgrades the player's level
        self.lvl += 1 #Levels up the player
        self.xp = 0 #Sets the xp to 0
    def addXP(self, XP):
        self.xp += XP #Gives the xp to the player
        if xpUpgrade[self.lvl] >= self.xp: #If enough xp is needed to level up -> upgrade
            self.upgrade()
    def addMoney(self, Money): #Adds Money to the player
        if self.money + Money < 0: #If the player's money added is negative and makes the money negative then just don't do it'
            return 0
        self.money += Money #Adds the money to the player
        return 1
    def addItem(self, item): #Adds an item to the player's inventory'
        self.inventory.append(item)

    def __str__(self): #Gives the description of the player
        return f"Name : {self.name}, ID : {self.id}, Lvl : {self.lvl}, XP : {self.xp}, Money : {self.money}, Inventory : {[self.inventory[i[0]].name for i in enumerate(self.inventory)]}, Pokelist : {[self.pokelist[i[0]].name for i in enumerate(self.pokelist)]}, Pokedex : {[self.pokedex.Pokelist[i[0]].name for i in enumerate(self.pokedex.Pokelist)]}, Poketeam : {[self.poketeam[i[0]].name for i in enumerate(self.poketeam)]}"

class Shop:
    def __init__(self, Itemlist): #Init
        self.Itemlist = Itemlist #All the items that are in the shop (Item[])

    #All Accessors
    def getItemlist(self):
        return self.Itemlist

    #Methods
    def buyItem(self, item, player): #Buy an item from the shop
        if item in self.Itemlist and player.money - item.price: #If the item is in the shop and the player has enough money
            player.money -= item.price #Removes the money from the player
            player.addItem(item) #Gives the item to the player
