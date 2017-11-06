from django.apps import AppConfig

TRANSFORMER = None
CLF = {}
APP_DATA = None


class BestPriceConfig(AppConfig):
    name = 'bestprice'
    verbose_name = "Best Price"

    def ready(self):
        from sklearn.externals import joblib
        import prototype.settings as settings
        import pandas as pd

        # load transformer and ML models when initializing application
        global TRANSFORMER
        global CLF
        global APP_DATA
        TRANSFORMER = joblib.load(settings.BASE_DIR + '/bestprice/static/models/pipeline_withText.sav')
        CLF['overall'] = joblib.load(settings.BASE_DIR + '/bestprice/static/models/model_GradientBoostingClassifier_with_text.sav')
        CLF['Music & Audio'] = joblib.load(settings.BASE_DIR + '/bestprice/static/models/model_Music_GradientBoostingClassifier_with_text.sav')
        APP_DATA = pd.read_csv(settings.BASE_DIR + '/bestprice/static/models/data_for_nearest_neighbor.csv')
