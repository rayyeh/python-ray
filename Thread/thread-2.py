import threading
import time
import Tkinter
import Queue
import sys
 
class Window(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.t = Msg()
	def run(self):
		self.root = Tkinter.Tk()
		exitb = Tkinter.Button(self.root, text="Done", command=self.endCommand)
		w = Tkinter.Label(self.root, 
			background="yellow")
		w.pack()
		self.t.setw(w, exitb)
		self.t.start()
		self.root.mainloop()
	def putmsg(self, obj):
		self.t.putmsg(obj)
	def endCommand(self):
		self.t.endApp()
		self.root.quit()
 
class Msg(threading.Thread):
	def __init__(self):
		self.q = Queue.Queue(1000)
		threading.Thread.__init__(self)
		self.running = 1
	def putmsg(self, obj):
		self.q.put(obj)
	def setw(self, w, exitb):
		self.w = w
		self.exitb = exitb
	def endApp(self):
		self.running = 0
	def run(self):
		while self.running:
			while self.q.qsize():
				try:
					msg = self.q.get(0)
					self.w['text'] = msg[0]
					if not msg[1] :
                                            self.exitb.pack()
				except Queue.Empty:
					pass
			time.sleep(1)
	
def main():
	t = Window()
	t.start() # If the threading isn't stop. The programming isn't stop.
	msg = [["Test", 1],  ["Test.Com", 0]]
	for m in msg:
		t.putmsg(m)
		time.sleep(2)

if __name__ == "__main__" :
	main()
	sys.exit()
