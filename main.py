from src.sudoquest_game import SudoquestGame


def main():
    shouldQuit = False
    game = SudoquestGame()
    game.init()

    while not shouldQuit:
        shouldQuit = game.run()
    
    game.quit()


if __name__ == '__main__':
    main()
