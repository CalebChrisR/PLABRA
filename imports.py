def usage(argc, argv):
    if argc == 1:
        # too little words
        return 1
    elif argc > 2:
        # too many words
        return 2
    elif argc == 2:
        if len(argv[1]) != 5:
            # word not 5 letters
            return 3
    else:
        return 0
