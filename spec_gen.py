if __name__ == '__main__':
    path = __file__.split("\\")
    assert path[-2] == 'hinata_maker'
    path[0] = path[0].upper()
    path = "\\\\".join(path[:-2])

    with open("./hinata_maker.spec.prototype", "r") as f_read:
        with open("./hinata_maker.spec", "w") as f_write:
            f_write.write(f_read.read().format(path = path))