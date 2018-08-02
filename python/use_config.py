from config import opt
import fire

def main(**kwargs):
    '''
    训练入口
    '''

    opt.parse(kwargs,print_=False)
    if opt.debug:import ipdb;ipdb.set_trace()

    model = getattr(models,opt.model)(opt).cuda()
    if opt.model_path:
        model.load(opt.model_path)
    print(model)

if __name__=="__main__":
    fire.Fire()  
