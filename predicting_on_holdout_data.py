
holdout = pd.read_csv('HoldoutData.csv', index_col=0)
holdout = holdout[NUMERIC_COLUMNS].fillna(-1000)
predictions = clf.predict_proba(holdout)  # Predict with probabilities, since log loss penalizes being confident and wrong

prediction_df = pd.DataFrame(columns=pd.get_dummies(df[LABELS], prefix_sep='__').columns, index=holdout.index, data=predictions)
prediction_df.to_csv('predictions.csv')
score = score_submission(pred_path='predictions.csv')


