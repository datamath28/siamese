PROJECT_HOME = "/Users/Brian/workplace/projects/siamese/"

# Settings for a local run.  More computational muscle than dev but less than if we
# were actually running on a gpu

# Settings for vanilla nn
NB_EPOCH = 25

# Settings for cnn
L1_FILTERS = 32
L2_FILTERS = 48
L3_FILTERS = 32

DROPOUT = True
CONVO_DROPOUT_FRACTION = 0.4
DROPOUT_FRACTION = 0.6

CONVO_L2_REGULARIZER = 0.00001
DENSE_L2_REGULARIZER = 0.00001

# Dimension of the embedding space. Here it is artificially small so we can visualize it
EMBEDDING_DIM = 16

FULLY_CONNECTED_SIZE = 128

# Learning Rate. Here we make it smaller because we seem to diverge with the normal learning
# rate and such a small embedding space
LEARNING_RATE = 0.00001
OPTIMIZER = 'rms'

# Margin for the contrastive loss function.  How far apart two observations from different
# classes need to be before the error is zero
MARGIN = 3
