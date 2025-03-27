from aif360.algorithms.preprocessing import Reweighing
from aif360.datasets import BinaryLabelDataset

def detect_bias(resumes):
    dataset = BinaryLabelDataset(df=resumes, label_names=['job_match_score'], protected_attribute_names=['gender'])
    rw = Reweighing()
    debiased_dataset = rw.fit_transform(dataset)
    return debiased_dataset.convert_to_dataframe()[0]
