#設定棋子的型態
class Checker(object):
        def __init__(self):
            self.alive=True # 活著
        def dead(self):
            self.alive =False #死掉            
            
class Jungle(Checker):
        def __init__(self,name):
            Checker.__init__(self) #繼承 checker.__init__
            
            animal={"E":"象","T":"老虎","C":"貓","M":"鼠"}
            food={"E":["象","虎","貓"],"T":["虎","貓","鼠"],"C":["貓","鼠"],"M":["鼠","象"]}
            
            if animal.has_key(name):
                self.name=animal[name]
                self.food=food[name]
            else:
                print "沒有這種動物喔!"
                self.name=False
                
        def __str__(self):
            if self.alive and self.name:
               return "我是[%s]! " %self.name
            else:
               return "[%s]被吃掉了!" %self.name
        
       #棋子互吃的方法                                     
        def capture(self,other):
            if self.name ==other.name:
                print self.name,"不能自己吃自己!"
            else:
               if self.alive and other.alive:
                  if other.name in self.food:
                     print self.name,"吃",other.name
                     other.dead()
                  else:
                     print self.name,"不能吃",other.name
               elif not self.alive:
                     print self.name,"已經死掉了!"
               elif not other.alive:
                     print other.name,"已經死掉了!"
               else:
                     print self.name,"和",other.name,"都已經死了!"
                     
#執行遊戲的函數                
def main():
        #初始條件設定
        #參與遊戲的動物棋子
        players ={"e":Jungle("E"),"t":Jungle("T"),"c":Jungle("C"),"m":Jungle("M")}
        #總存活數的設定
        lives=len(players)
        
#主要遊戲迴圈
        while lives > 1:
                #印出每隻動物的存活訊息
                for player in sorted(players.values()):
                        print player

                #操作提示
                print
                print "操作 象 打e,操作 虎打 t,操作 貓打 c,操作 鼠打 m"
                first=raw_input("哪一隻動物餓了?")
                second =raw_input("要吃哪一隻")

                if first in players.keys() and second in players.keys():
                        players[first].capture(players[second])
                        if not players[second].alive:
                                lives=lives - 1
                #印出區格線
                print "*"*50
                print

        #印出遊戲勝利者
        for Winner in players.values():
                if Winner.alive ==True:
                        print
                        print Winner.name,"是最後的存活者"

__main__ = main()                        
                        

                
