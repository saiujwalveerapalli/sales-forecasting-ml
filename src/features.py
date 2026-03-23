import pandas as pd

def create_lag_features(df, target_col, lags=[1, 7, 14, 30]):
    """Create lag features for time series forecasting."""
    for lag in lags:
        df[f"lag_{lag}"] = df[target_col].shift(lag)
    return df

def create_rolling_features(df, target_col, windows=[7, 30]):
    """Create rolling mean and std features."""
    for window in windows:
        df[f"rolling_mean_{window}"] = df[target_col].rolling(window).mean()
        df[f"rolling_std_{window}"] = df[target_col].rolling(window).std()
    return df

def add_calendar_features(df, date_col):
    """Add month, quarter, week features."""
    df["month"] = pd.to_datetime(df[date_col]).dt.month
    df["quarter"] = pd.to_datetime(df[date_col]).dt.quarter
    df["week"] = pd.to_datetime(df[date_col]).dt.isocalendar().week
    return df
