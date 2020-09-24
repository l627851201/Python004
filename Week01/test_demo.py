class TestGlobal:
    g_a = "a"

    def modGA(self):
        # print("modGA: {}".format(g_a))

        global g_a
        g_a = "b"
        print("modGA: {}".format(g_a))

if __name__ == '__main__':
    tg = TestGlobal()
    tg.modGA()
