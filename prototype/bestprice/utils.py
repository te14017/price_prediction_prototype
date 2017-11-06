import pandas as pd
import re
import prototype.settings as settings
import datetime

BASE_DIR = settings.BASE_DIR


def convert_form_to_df(form):
    # get columns of dataframe
    with open(BASE_DIR + '/bestprice/static/models/columns.txt', 'r') as f:
        columns_str = f.readline()
    columns = re.findall(r'[\w\d]+[\w_\d\.\s&+\-,]*', columns_str)
    print(len(columns))

    # get big company names
    with open(BASE_DIR + '/bestprice/static/models/bigCompanies.txt', 'r') as f:
        bigCom_str = f.readline()
    bigProviders = re.findall(r'\w{2,}[\w\s]*', bigCom_str)
    #print(bigProviders[:10])

    # construct empty dataframe for the input app
    df = pd.DataFrame(columns=columns)
    #print(df.dtypes)

    df.loc[0, 'text'] = form.cleaned_data["name"] + form.cleaned_data["author"] + form.cleaned_data["description"]
    df.loc[0, 'starRating'] = form.cleaned_data["starRating"] if form.cleaned_data["starRating"] else 0.0
    df.loc[0, 'bigProvider'] = 1 if form.cleaned_data["author"] in bigProviders else 0
    _transform_reviews(form, df)
    df.loc[0, '1_star_reviews'] = form.cleaned_data["one_star_reviews"] if form.cleaned_data["one_star_reviews"] else 0
    df.loc[0, '2_star_reviews'] = form.cleaned_data["two_star_reviews"] if form.cleaned_data["two_star_reviews"] else 0
    df.loc[0, '3_star_reviews'] = form.cleaned_data["three_star_reviews"] if form.cleaned_data["three_star_reviews"] else 0
    df.loc[0, '4_star_reviews'] = form.cleaned_data["four_star_reviews"] if form.cleaned_data["four_star_reviews"] else 0
    df.loc[0, '5_star_reviews'] = form.cleaned_data["five_star_reviews"] if form.cleaned_data["five_star_reviews"] else 0

    # convert date into datetime
    update_day = datetime.datetime.combine(form.cleaned_data["lastUpdate"].today(), datetime.time.min)
    df.loc[0, 'days_since_lastUpdated'] = (datetime.datetime.now() - update_day).days if form.cleaned_data["lastUpdate"] else 0

    release_day = datetime.datetime.combine(form.cleaned_data["age"].today(), datetime.time.min)
    df.loc[0, 'days_since_release'] = (datetime.datetime.now() - release_day).days

    df.loc[0, 'category_' + form.cleaned_data["category"].strip()] = 1
    _transform_androidVersion(form, df)
    df.loc[0, 'ranking_' + form.cleaned_data["rank"].strip()] = 1
    df.loc[0, 'contentRating_' + form.cleaned_data["contentRating"].strip()] = 1
    _transform_library(form, df)
    _transform_binarySize(form, df)

    df.loc[0, 'installs_' + form.cleaned_data["installs"].strip()] = 1

    if form.cleaned_data["inAppPurchase"] == 'with in-App purchase':
        df.loc[0, 'offersInAppPurchases_1'] = 1
    else:
        df.loc[0, 'offersInAppPurchases_0'] = 1

    df.fillna(0.0, inplace=True)
    #print(df.dtypes)

    return df


def _transform_reviews(form, df):
    if form.cleaned_data["reviews"] < 100:
        df.loc[0, 'totalNrOfReviews_1'] = 1
    elif form.cleaned_data["reviews"] >= 100 and form.cleaned_data["reviews"] < 500:
        df.loc[0, 'totalNrOfReviews_2'] = 1
    else:
        df.loc[0, 'totalNrOfReviews_3'] = 1


def _transform_androidVersion(form, df):
    nums = form.cleaned_data["androidVersion"].split('.')
    df.loc[0, 'requiredAndroidVersion_d1_'+nums[0]] = 1
    df.loc[0, 'requiredAndroidVersion_d2_' + nums[0]] = 1


def _transform_library(form, df):
    if form.cleaned_data["libraries"] > 0:
        df.loc[0, 'libraries_1.0'] = 1
    else:
        df.loc[0, 'libraries_0.0'] = 1


def _transform_binarySize(form, df):
    size = form.cleaned_data["size"] * 1024
    if size < 3000.0:
        df.loc[0, 'binarySize_1'] = 1
    elif size >= 3000.0 and size <= 10000.0:
        df.loc[0, 'binarySize_2'] = 1
    elif size > 10000.0 and size <= 35000.0:
        df.loc[0, 'binarySize_3'] = 1
    else:
        df.loc[0, 'binarySize_4'] = 1
