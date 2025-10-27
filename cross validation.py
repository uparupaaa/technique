from sklearn.metrics import log_loss, accuracy_score
from sklearn.model_selection import KFold

# 各foldのスコアを保存するリスト
scores_accuracy = []
scores_logloss = []

# クロスバリデーションを行う
# 学習データを4つに分割し、うち1つをバリデーションデータとすることを、バリデーションデータを変えて繰り返す
kf = KFold(n_splits=4, shuffle=True, random_state=71)
for tr_idx, va_idx in kf.split(train_x):
   # 学習データを学習データとバリデーションデータに分ける
   tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
   tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]

   # モデルの学習を行う
   model = XGBClassifier(n_estimators=20, random_state=71)
   model.fit(tr_x, tr_y)

   # バリデーションデータの予測値を確率で出力する
   va_pred = model.predict_proba(va_x)[:, 1]

   # バリデーションデータでのスコアを計算する
   logloss = log_loss(va_y, va_pred)
   accuracy = accuracy_score(va_y, va_pred > 0.5)

   # そのfoldのスコアを保存する
   scores_logloss.append(logloss)
   scores_accuracy.append(accuracy)

# 各foldのスコアの平均を出力する
logloss = np.mean(scores_logloss)
accuracy = np.mean(scores_accuracy)
print(f'logloss: {logloss:.4f}, accuracy: {accuracy:.4f}')
