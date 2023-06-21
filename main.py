#Isabella e Kemily - Sistema de Biblioteca LP2
import bd
import menu

MENU_INICIAL = 0

def main():
  menu.exibir_menuPRINCIPAL()

if __name__ == "__main__":
  bd.criar_bdd()
  main()
