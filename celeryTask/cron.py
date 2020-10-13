from apps import celery


@celery.task(name='helloWorld')
def helloWorld():
    # time.sleep(1)
    print('hello,world')
    return 'hello,world'
