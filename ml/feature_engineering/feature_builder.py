import pandas as pd

from feature_engineering.mfcc import extract_mfcc


def build_feature_row(
    audio,
    label
):
    """
    Create one feature row.
    """

    mfcc_features = extract_mfcc(audio)

    row = {
        f"mfcc_{i}": value
        for i, value in enumerate(mfcc_features)
    }

    row["label"] = label

    return row


def create_feature_dataframe(rows):
    """
    Convert rows to DataFrame.
    """

    return pd.DataFrame(rows)