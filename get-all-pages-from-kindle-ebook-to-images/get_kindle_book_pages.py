import pyautogui as pag
import time

format = '.png'

############################################
#----------      PARÂMETROS      -----------

# TOTAL PAGE NUMBER / NÚMERO DE PÁGINAS AQUI:
total_pages = 22

# SCREENSHOTS PATH / PATH A SALVAR OS SCREENSHOTS:
path = "C:\\Livros\\01\\"

# MOUSE POSITION TITLE BAR KINDLE APP / POSIÇÃO MOUSE x,y BARRA TITULO APP KINDLE:
kindle_head_x = 843
kindle_head_y = 18

# KINDLE APP NEXT PAGE BUTTON x,y POSITION / POSIÇÃO MOUSE x,y BOTÃO KINDLE PRÓXIMA PÁGINA:
kindle_nextpage_x = 1333
kindle_nextpage_y = 402

# SIZE OF PAGE / ENQUADRAMENTO PÁGINA x,y APP KINDLE:
pag_start_x = 452
pag_start_y = 105
pag_end_x = 846
pag_end_y = 590

############################################


# go to kindle app / vai para o app kindle:
pag.click(kindle_head_x, kindle_head_y)

for i in range(1,total_pages+1):
    print(i)
    time.sleep(0.25)

    # page screenshot / printscren pagina:
    pg = str(i).zfill(3)
    im = pag.screenshot(region=(pag_start_x,pag_start_y, pag_end_x, pag_end_y))
    im.save(f"{path}{pg}{format}")

    # go to next page / vai para proxima pagina:
    pag.click(kindle_nextpage_x, kindle_nextpage_y)


