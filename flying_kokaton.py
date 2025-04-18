import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)#練習8
    kk_img = pg.image.load("fig/3.png") #練習2こうかとん読み込み
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kk_rct.move_ip(-1,0)
        key_lst = pg.key.get_pressed()#練習10こうかとんの移動
        X=0
        Y=0
        if key_lst[pg.K_UP]:
            Y-=1
        if key_lst[pg.K_DOWN]:
            Y+=1
        if key_lst[pg.K_LEFT]:
            X-=1
        if key_lst[pg.K_RIGHT]:
            X+=2
        kk_rct.move_ip(X,Y)

        x=tmr%3200
        screen.blit(bg_img, [-x, 0])#練習6背景を右に動かす
        screen.blit(bg_img2, [-x+1600, 0])#練習7背景を増やす
        screen.blit(bg_img, [-x+3200, 0])#練習9ループ化
        #練習4こうかとん表示
        screen.blit(kk_img,kk_rct)#
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()