"""
    This file contains the Machine Learning Model class, which is responsible
    of anything related to the ML Model. This included building, training, and 
    evaluating the model.
"""
from keras.models import Sequential

from ml_data import Data
import config as cfg


class Model():
    """
        This class represents the overall Machine Learning Model, and
        contains methods for creating, building, training, evaluating
        and retrieving the model.

        All of this should be handled as if it was local, and should
        therefore not use ANY MS-Azure functions.
    """
    model = Sequential()
    def __init__(self, data):
        """
            Construct the class by creating an empty, sequential model (see
            the variable above). The function takes in a Data object from
            the ml_data module, which should be used to extract the data
            and retrieve training and test data.
        """
        pass


    def build(self):
        """
            The model is built by adding different layers using Keras.
            Since the model processes images, important layers may include:

            Convolution, MaxPool, Dropout and Flatten layers.
        """
        pass


    def train(self):
        """
            Compile and initalize training of the model. Important factors
            to consider here is which optimizer to use, how to compute
            loss, and which metrics to use. Also decide on how many epochs to
            run the training for. All of this can be specified in the config.
        """
        pass


    def save(self):
        """
            Save the model object as a local file. Consider which
            format to use, as it may be important to use a format which is
            compatible with Azure.
        """
        pass


    def evaluate(self):
        """
            Compute the accuracy and loss of the model trained. It may also
            be relevant to plot a graph which shows how the accuracy and
            loss developes through the epochs. Note that this requires that
            the history is retrieved during training.
        """
        pass

    
    def get(self):
        """
            Retrieve the model to the caller.
        """
        return self.model
