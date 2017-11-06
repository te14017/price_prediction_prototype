from django.http import HttpResponse
from django.shortcuts import render

from bestprice import models
from bestprice import utils
from bestprice.apps import TRANSFORMER
from bestprice.apps import CLF
from bestprice.apps import APP_DATA

from sklearn.neighbors import NearestNeighbors


def inputpage(request):
    form = models.AppInfoForm()

    return render(request, "input_price.html", {'form': form})


def get_prediction(request):
    if request.method == 'POST':
        form = models.AppInfoForm(request.POST)

        if form.is_valid():
            # convert received form into dataframe
            df = utils.convert_form_to_df(form)
            df_ = df.copy()
            #print("===== df shape:" + str(df_.shape))

            category = form.cleaned_data["category"]
            if category not in CLF.keys():
                predict_seg = 'overall'
            else:
                predict_seg = category

            # transform and predict input dataframe
            transformed_df = TRANSFORMER.transform(df)
            predicted_price_range = CLF[predict_seg].predict(transformed_df)[0]
            print("========= predicted range: " + str(predicted_price_range))
            predicted_price_range = 2

            range = models.consts.PRICE_RANGE_BOUNDARY[predict_seg]
            confidence = models.consts.PREDICT_CONFIDENCE[predict_seg][predicted_price_range-1]
            confidence_result = max(confidence)
            predict_result = _get_predict_result(range, predicted_price_range)

            # compute nearest neighbors
            df_for_nn = _transform_app_data(df_)
            neighbors = _get_nearest_apps(df_for_nn, form)

            return render(request, "predict_result.html", {'range': range,
                                                           'confidence': confidence,
                                                           'result': predict_result,
                                                           'confidence_result': confidence_result,
                                                           'similar_apps': neighbors})
    else:
        return HttpResponse("Bad Request.")


def _get_nearest_apps(df, form, withInSameCategory=True):
    # if withInSameCategory, we compute nearest apps from apps with the same category
    if withInSameCategory:
        app_data = APP_DATA.loc[APP_DATA['category_' + form.cleaned_data["category"].strip()] == 1, :].copy()

    # get app information for return view use
    app_data.reset_index(inplace=True)
    app_info = app_data[['name', 'appUrl']]
    #app_info.reset_index(inplace=True)
    app_data.drop(['index', 'name', 'appUrl'], inplace=True, axis=1)
    #transformed_app_data = TRANSFORMER.named_steps['selector'].transform(app_data)
    print("=====app data shape: "+str(app_data.shape))
    #print(str(df.columns.tolist()))
    #print(str(app_data.columns.tolist()))

    nearest_neighbors = NearestNeighbors(n_neighbors=7, algorithm='ball_tree').fit(app_data)

    distances, indices = nearest_neighbors.kneighbors(df)
    print(indices)

    neighbors = {app_info.loc[x, 'name']: app_info.loc[x, 'appUrl'] for x in indices[0]}

    print(distances)

    return neighbors


def _transform_app_data(df):
    # transform text feature
    df_text_as_result = TRANSFORMER.named_steps['textTransformer'].transform(df)

    # scaling
    transformed_df = TRANSFORMER.named_steps['scaling'].transform(df_text_as_result)

    return transformed_df


def _get_predict_result(range, number):
    if number == 1:
        result = "free" + " - " + str(range[1])
    elif number == 2:
        result = str(range[0]) + " - " + str(range[1])
    elif number == 3:
        result = str(range[1]) + " - " + str(range[2])
    else:
        result = "above " + str(range[2])
    return result