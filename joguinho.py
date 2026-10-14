import pygame, os, json, random

pygame.init()
pygame.font.init()

tela = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Jogo do quadrado comilão")

relogio = pygame.time.Clock()
rodando = True
vel = 7
x_fruta = random.randint(50, 950)
y_fruta = random.randint(50, 700)
f_save = "save_joguinho.json"
font = pygame.font.SysFont("Arial", 32)

if os.path.exists(f_save):
    with open(f_save, "r") as f:
        data_save = json.load(f)
        x_perso = data_save.get("x", 500)
        y_perso = data_save.get("y", 375)
        pontos = data_save.get("pontos", 0)
    print("Progesso carregado! volte com seu jogo!")
else:
    x_perso = 500
    y_perso = 375
    pontos = 0
    print("Você não tem saves, iniciando do zero!")

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  x_perso -= vel
    if teclas[pygame.K_RIGHT]: x_perso += vel
    if teclas[pygame.K_UP]:    y_perso -= vel
    if teclas[pygame.K_DOWN]:  y_perso += vel

    if x_perso < 0:   x_perso = 0
    if x_perso > 950: x_perso = 950
    if y_perso < 0:   y_perso = 0
    if y_perso > 700:   y_perso = 700
  
    rect_player = pygame.Rect(x_perso, y_perso, 50, 50)
    rect_fruta = pygame.Rect(x_fruta, y_fruta, 25, 25)

    if rect_player.colliderect(rect_fruta):
        pontos += 10
        print(f"Umm, delicioso! Você ganhou 10 pontos por comer! Pontos: {pontos}")

        while True:
            x_fruta = random.randint(50, 950)
            y_fruta = random.randint(50, 700)
            rect_new_fruta = pygame.Rect(x_fruta, y_fruta, 25, 25)

            if not rect_player.colliderect(rect_new_fruta):
                break

    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (0, 100, 255), rect_player)
    pygame.draw.rect(tela, (255, 0, 0), rect_fruta)
    text = font.render(f"Pontos: {pontos}", True, (255, 255, 255))

    tela.blit(text, (15, 15))
    pygame.display.flip()

    relogio.tick(60)

data_to_save = {"x": x_perso, "y": y_perso, "pontos": pontos}

with open(f_save, "w") as f:
    json.dump(data_to_save, f)

print("Guardamos seus dados de jogador num save, até mais!")

pygame.quit()
