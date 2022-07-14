# define GAN model
model = dict(
    type='SNGAN',
    data_preprocessor=dict(type='GANDataPreprocessor'),
    generator=dict(type='SNGANGenerator', output_scale=128, base_channels=64),
    discriminator=dict(
        type='ProjDiscriminator', input_scale=128, base_channels=64),
    discriminator_steps=2)
