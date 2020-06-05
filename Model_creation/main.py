from model_data.DATA import create_binary
from model_data.DATA import create_multi
from model_data import create_binary_multi_model



def main():
    exec(create_binary)
    exec(create_multi)
    exec(create_binary_multi_model)





if __name__ == '__main__':
    main()
