#�]�w�Ѥl�����A
class Checker(object):
        def __init__(self):
            self.alive=True # ����
        def dead(self):
            self.alive =False #����            
            
class Jungle(Checker):
        def __init__(self,name):
            Checker.__init__(self) #�~�� checker.__init__
            
            animal={"E":"�H","T":"�Ѫ�","C":"��","M":"��"}
            food={"E":["�H","��","��"],"T":["��","��","��"],"C":["��","��"],"M":["��","�H"]}
            
            if animal.has_key(name):
                self.name=animal[name]
                self.food=food[name]
            else:
                print "�S���o�ذʪ���!"
                self.name=False
                
        def __str__(self):
            if self.alive and self.name:
               return "�ڬO[%s]! " %self.name
            else:
               return "[%s]�Q�Y���F!" %self.name
        
       #�Ѥl���Y����k                                     
        def capture(self,other):
            if self.name ==other.name:
                print self.name,"����ۤv�Y�ۤv!"
            else:
               if self.alive and other.alive:
                  if other.name in self.food:
                     print self.name,"�Y",other.name
                     other.dead()
                  else:
                     print self.name,"����Y",other.name
               elif not self.alive:
                     print self.name,"�w�g�����F!"
               elif not other.alive:
                     print other.name,"�w�g�����F!"
               else:
                     print self.name,"�M",other.name,"���w�g���F!"
                     
#����C�������                
def main():
        #��l����]�w
        #�ѻP�C�����ʪ��Ѥl
        players ={"e":Jungle("E"),"t":Jungle("T"),"c":Jungle("C"),"m":Jungle("M")}
        #�`�s���ƪ��]�w
        lives=len(players)
        
#�D�n�C���j��
        while lives > 1:
                #�L�X�C���ʪ����s���T��
                for player in sorted(players.values()):
                        print player

                #�ާ@����
                print
                print "�ާ@ �H ��e,�ާ@ �ꥴ t,�ާ@ �ߥ� c,�ާ@ ���� m"
                first=raw_input("���@���ʪ��j�F?")
                second =raw_input("�n�Y���@��")

                if first in players.keys() and second in players.keys():
                        players[first].capture(players[second])
                        if not players[second].alive:
                                lives=lives - 1
                #�L�X�Ϯ�u
                print "*"*50
                print

        #�L�X�C���ӧQ��
        for Winner in players.values():
                if Winner.alive ==True:
                        print
                        print Winner.name,"�O�̫᪺�s����"

__main__ = main()                        
                        

                
