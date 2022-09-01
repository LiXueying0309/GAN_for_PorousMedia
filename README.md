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
