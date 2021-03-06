from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from pdb import set_trace


class ABCD:

    @classmethod
    def get_pd_pf(cls, actual, predicted):
        """
        Obtain Recall (Pd) and False Alarm (Pf) scores

        Parameters
        ----------
        actual: numpy.ndarray, shape=[n_samples]
            Ground truth (correct) target values.
        predicted: numpy.ndarray, shape=[n_samples]
            Estimated targets as returned by a classifier.
        
        Returns
        -------
        pd: float
            Recall (pd) value 
        pf: float
            False alarm (pf) values 
        """
        tn, fp, fn, tp = confusion_matrix(actual, predicted).ravel()
        pd = int(100 * tp/(tp+fn+1e-5))
        pf = int(100 * fp/(fp+tn+1e-5))

        return pd, pf

    @classmethod
    def get_f_score(cls, actual, predicted, beta=1):
        """
        Obtain F scores

        Parameters
        ----------
        actual: numpy.ndarray, shape=[n_samples]
            Ground truth (correct) target values.
        predicted: numpy.ndarray, shape=[n_samples]
            Estimated targets as returned by a classifier.
        beta: float, default=1
            Amount by which recall is weighted higher than precision
        
        Returns
        -------
        prec: float
            Precision
        recall: float
            Recall
        f: float
            F score 
        """

        tn, fp, fn, tp = confusion_matrix(actual, predicted).ravel()
        prec = tp / (tp + fp + 1e-5)
        recall = tp / (tp + fn + 1e-5)
        f = int(100 * (1 + beta**2) * (prec * recall) /
                (beta**2 * prec + recall + 1e-5))
        prec = int(100 * prec)
        recall = int(100 * recall)
        return prec, recall, f
