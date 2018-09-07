# encoding: utf-8
#

class DefaultConfig(object):
    env = 'dev'
    model_path = './model/hello'
    debug = False
    port = 5000


def parse(self, kwargs):
    for k, v in kwargs.items():
        setattr(self, k, v)

    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse

opt = DefaultConfig()


def hello(**kwargs):
    opt.parse(kwargs)


if __name__ == '__main__':
    import fire
    import cv2
    cv2.VideoCapture
    fire.Fire()
