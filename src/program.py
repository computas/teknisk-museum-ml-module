"""
    This file contains everything needed to run the overall program. This is
    done with the use of the Program class, which is responsible for this.
"""
import config as cfg


class Program():
    """
        This class is responsible for managing the overall program flow.
        Because of this, it is also responsible for connecting to Azure
        and such, but the class should use the Model and Data classes to
        manage the machine learning model, and the data.
    """
    def __init__(self):
        """
            Construct the class. We simply do this by calling on the
            class' main-function.
        """
        self.main()


    def main(self):
        """
            We let this function serve as the programs overall main-function.
            The entry point for the overall source code therefore starts here.
        """
        pass
