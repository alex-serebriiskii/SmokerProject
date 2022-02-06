from config import Config

def GenerateConfigs():
    configs=[]
    for ct in range(5,15):
        for rat in range(1,15):
            conf= Config(ct, rat)
            configs.append(conf)
    return configs