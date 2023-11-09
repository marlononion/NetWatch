from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from tpot import TPOTClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import autokeras as ak
import pandas as pd
from sklearn.model_selection import train_test_split

class TrainingData(object):
    def __init__(self, data, target_column, epochs, trials, model_path, save=True):
        self.data = "../../data/raw_data/"+data
        self.target_column = target_column
        self.epochs = epochs
        self.trials = trials
        self.model_path = '../../models/'+model_path
        self.save = save

    def load_data(self):
        self.data = pd.read_csv(self.data)

    def preprocess_data(self):
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]

        # Tratamento de valores ausentes
        imputer = SimpleImputer(strategy='mean')
        X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

        # Padronização dos dados
        scaler = StandardScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)

        self.X_scaled = X_scaled
        self.y = y

        return X_scaled, y

    def training_data(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X_scaled, self.y, test_size=0.2, random_state=42)

        # Inicializar e treinar o classificador Auto-Keras
        clf = ak.StructuredDataClassifier(max_trials=self.trials)  # Escolha o número de tentativas
        clf.fit(X_train, y_train, epochs=self.epochs)

        # Avaliar o modelo
        print(clf.evaluate(X_test, y_test))
        if self.save:
            clf.export_model().save(self.model_path)

    def train(self):
        self.load_data()
        self.preprocess_data()
        self.training_data()

TrainingData("network_traffic.csv", "flags", 2, 1, "default").train()