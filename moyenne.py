from datetime import datetime
def generate_log(params):

        with open('logs.txt', 'a') as f:

                    f.write('on a appelé la fonction moyenne {} avec les parametres {}\n'.format(
                                datetime.now(), params)
                                        )

def moyenne (data):
    generate_log (data)
    return sum(data)/len(data)
