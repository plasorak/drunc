


def main() -> None:
    import nest_asyncio
    nest_asyncio.apply()
    from drunc.interface.rc_shell import rc_shell, RCContext
    from drunc.controller.controller import Controller
    ctrlr = Controller('top')
    ctrlr.add_controlled_children('child1', 'localhost:123')
    ctrlr.add_controlled_children('child2', 'localhost:124')
    context = RCContext(ctrlr)
    rc_shell(obj = context)
    

if __name__ == '__main__':
    main()
