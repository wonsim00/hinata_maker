if __name__ == '__main__':
    path = __file__.split("\\")
    if path[-2] != 'hinata_maker':
        raise RuntimeError("Please place this code to \"hinata_maker\" folder!")
    path[0] = path[0].upper()       # for windows
    path = "\\\\".join(path[:-2])   # for windows

    with open("./hinata_maker.spec.prototype", "r") as f_read:
        with open("./hinata_maker.spec", "w") as f_write:
            f_write.write(f_read.read().format(path = path))