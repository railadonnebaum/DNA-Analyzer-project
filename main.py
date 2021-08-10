try:
    from util.CLI import CLI
    from util.controller import Controller
except ImportError:
    print("Need to fix the installation")
    raise

def main():
    controller = Controller()
    cli = CLI(controller)
    cli.run()


if __name__ == '__main__':
    main()


