import os
import urllib.request


def mkdir_if_not_exists(dir_name):
    if not (os.path.exists(dir_name) and os.path.isdir(dir_name)):
        os.mkdir(dir_name)


if __name__ == '__main__':
   

    
    
    train_link = 'https://zenodo.org/records/2603256/files/train.h5?download=1'
    val_link = 'https://zenodo.org/records/2603256/files/val.h5?download=1'
    test_link = 'https://zenodo.org/records/2603256/files/test.h5?download=1'
    

    print('Creating data directories...')
    mkdir_if_not_exists('original')



    #data Zenodo    
    
    print('Downloading training data to original/train.h5...', flush=True)
    urllib.request.urlretrieve(train_link, 'original/train.h5')
    print('Downloading validation data to original/val.h5...', flush=True)
    urllib.request.urlretrieve(val_link, 'original/val.h5')
    print('Downloading test data original/test.hf...', flush=True)
    urllib.request.urlretrieve(test_link, 'original/test.h5')
    

    print('Done!')

