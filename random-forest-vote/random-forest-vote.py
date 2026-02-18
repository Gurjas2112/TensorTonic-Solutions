import numpy as np
from sklearn.utils.extmath import weighted_mode

def random_forest_vote(predictions):
    predictions = np.array(predictions)
    return weighted_mode(
        predictions,
        np.ones(predictions.shape),
        axis=0
    )[0].ravel().tolist()