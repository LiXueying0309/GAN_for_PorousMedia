# GAN_for_PorousMedia
### This code is partially borrowed from the package named PorousMediaGAN, which is developed by Lukas Mosser, Olivier Dubrule, and Martin J. Blunt from the department of Earth Science and Engineering, Imperial College London. (https://github.com/LukasMosser/PorousMediaGan)

1. Preparation before training the generative adversarial neural network model

Install jupyter notebook
```
pip install jupyter notebook
```

Since the neural network is trained by pytorch, you should also install the torch packages ```hdf5``` and ```dpnn```.
```
pip install hdf5
pip install dpnn
```

Plus, ```h5py``` and ```tifffile``` are also needed.
```
pip install h5py
pip install tifffile
```

Then, clone this repository to your PC:
```
git clone https://github.com/LiXueying0309/GAN_for_PorousMedia
cd GAN_for_PorousMedia
```

2. How to train the model

1) Run ```generator.py``` to generate training images from the original data sample
```
python generator.py --seed 42 --imageSize 64 --ngf 32 --ndf 16 --nz 512 --netG [path to generator checkpoint].pth --experiment sand --imsize 9 --cuda --ngpu 1
```

2) Run ```create_training_images.py``` to segment the image size into 64*64*64 voxel
```
python create_training_images.py --image berea.tif --name berea --edgelength 64 --stride 32 --target_dir berea_ti
```

3) Run ```main.py``` to train the GAN model
```
python main.py --dataset 3D --dataroot [path to training images] --imageSize 64 --batchSize 128 --ngf 64 --ndf 16 --nz 512 --niter 1000 --lr 1e-5 --workers 2 --ngpu 2 --cuda 
```
