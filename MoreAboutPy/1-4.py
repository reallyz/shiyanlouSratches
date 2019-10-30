from abc import ABCMeta,abstractmethod
from random import randint


class Fighter(object,metaclass=ABCMeta):
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._hp=hp
        self._name=name

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp>=0 else 0

    @property
    def alive(self):
        return self._hp>0
    # 只有一个类加了抽象方法，就不能被实例化
    # 也是继承顺序是元类 过后是abc类
    @abstractmethod
    def attack(self,other):
        pass

class Ultraman(Fighter):
    #__slots__=super().__slots__+('_mp',)
    __slots__ = ('_name','_hp','_mp') #对_slots_能追加吗
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp=mp

    def attack(self,other):
        other.hp-=randint(15,25)
    def huge_attack(self,other):
        flag=0
        if self._mp>=50:
            self._mp-=50
            injury=other.hp*3//4
            injury=injury if injury>=50 else 50
            other.hp-=injury
            flag=1
        else:
            self.attack(other)
        return flag

    def magic_attack(self,others):
        flag=0
        if self._mp>=20:
            self._mp-=20
            for _ in others:
                if _.alive:
                    _.hp-=randint(10,15)
            flag=1
        return flag

    def resume(self):
        incr_point=randint(1,10)
        self._mp+=incr_point
        return incr_point
    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    flag=0
    for monster in monsters:
        if monster.alive>0:
            flag=1
            break
    return flag
def select_alive_one(monsters):
    pass


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    print("you can arrange your monsters to have a better chance to win\n")
    ms=[m1,m2,m3]
    s=eval(input("your order\n"))
    msn=[]
    for i in s:
        msn.append(ms[i-1])
    fight_round = 1
    while u.alive and is_any_alive(msn):
        print('========第%02d回合========' % fight_round)
        m=msn.pop(0)
        skill=randint(1,10)
        if skill<=6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
            msn.append(m)
        display_info(u,msn)
        fight_round+=1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__=="__main__":
    main()
