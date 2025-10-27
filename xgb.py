import xgboost as xgb
from sklearn.metrics import log_loss

# 特徴量と目的変数をxgboostのデータ構造に変換する
dtrain = xgb.DMatrix(tr_x, label=tr_y)
dvalid = xgb.DMatrix(va_x, label=va_y)
dtest = xgb.DMatrix(test_x)

# ハイパーパラメータの設定
params = {'objective': 'binary:logistic', 'silent': 1, 'random_state': 71}
num_round = 50

# 学習の実行
# バリデーションデータもモデルに渡し、学習の進行とともにスコアがどう変わるかモニタリングする
# watchlistには学習データおよびバリデーションデータをセットする
watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
model = xgb.train(params, dtrain, num_round, evals=watchlist)

# バリデーションデータでのスコアの確認
va_pred = model.predict(dvalid)
score = log_loss(va_y, va_pred)
print(f'logloss: {score:.4f}')

# 予測（二値の予測値ではなく、1である確率を出力するようにしている）
pred = model.predict(dtest)


# モニタリングをloglossで行い、アーリーストッピングの観察するroundを20とする
params = {'objective': 'binary:logistic', 'silent': 1, 'random_state': 71,
        'eval_metric': 'logloss'}
num_round = 500
watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
model = xgb.train(params, dtrain, num_round, evals=watchlist,
                 early_stopping_rounds=20)

# 最適な決定木の本数で予測を行う
pred = model.predict(dtest, ntree_limit=model.best_ntree_limit)

