import tkinter
from pygame import mixer

def click_btn():
    mixer.init()
    mixer.music.load( "ui_erai.mp3" )
    mixer.music.play(1)
   
root = tkinter.Tk()
root.title("ママに「偉い」と言われたい…")
root.geometry("300x280")
root.resizable( False, False )

background = tkinter.Canvas(root, width="300", height="280", bg="skyblue")
background.pack()

ui = tkinter.PhotoImage(file="ui_love.png")
background.create_image( 150, 120, image = ui )

btn = tkinter.Button( root, text = "俺は，偉い！", command = click_btn )
btn.place( x = 100, y = 230 )


root.mainloop()



#廣瀬豪，株式会社ソーテック，Pythonでつくるゲーム開発入門講座
#【Python】PygameでBGMの再生:https://shizenkarasuzon.hatenablog.com/entry/2019/02/24/090652
#Pythonで効果音を再生する方法を現役エンジニアが解説【初心者向け】:https://techacademy.jp/magazine/28692
