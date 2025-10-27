from keras.layers import Dense, Dropout
from keras.models import Sequential
from sklearn.metrics import log_loss
from sklearn.preprocessing import StandardScaler

# データのスケーリング
scaler = StandardScaler()
tr_x = scaler.fit_transform(tr_x)
va_x = scaler.transform(va_x)
test_x = scaler.transform(test_x)

# ニューラルネットモデルの構築
model = Sequential()
model.add(Dense(256, activation='relu', input_shape=(train_x.shape[1],)))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
             optimizer='adam', metrics=['accuracy'])

# 学習の実行
# バリデーションデータもモデルに渡し、学習の進行とともにスコアがどう変わるかモニタリングする
batch_size = 128
epochs = 10
history = model.fit(tr_x, tr_y,
                   batch_size=batch_size, epochs=epochs,
                   verbose=1, validation_data=(va_x, va_y))

# バリデーションデータでのスコアの確認
va_pred = model.predict(va_x)
score = log_loss(va_y, va_pred, eps=1e-7)
print(f'logloss: {score:.4f}')

# 予測
pred = model.predict(test_x)

