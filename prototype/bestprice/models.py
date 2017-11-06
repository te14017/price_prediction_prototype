from django.db import models

from django import forms
import bestprice.consts as consts


class AppInfoForm(forms.Form):
    name = forms.CharField(
        required=True,
        label="",
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'required': True,
                'placeholder': "App Name",
            }
        ),
    )
    author = forms.CharField(
        min_length=2,
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Author",
            }
        ),
    )
    category = forms.ChoiceField(
        required=True,
        choices=consts.CATEGORY_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "Select the category",
            }
        ),
    )
    size = forms.FloatField(
        max_value=9999,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Binary size in MB",
            }
        ),
    )
    inAppPurchase = forms.ChoiceField(
        required=True,
        choices=consts.IN_APP_PURCHASE_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "Select if or not with in-App purchase",
            }
        ),
    )
    libraries = forms.IntegerField(
        min_value=0,
        max_value=999,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Number of libraries you used",
            }
        ),
    )
    androidVersion = forms.CharField(
        min_length=1,
        max_length=6,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Required android version (such as: 1.2.0)",
            }
        ),
    )
    contentRating = forms.ChoiceField(
        required=True,
        choices=consts.CONTENT_RATING_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "Select content rating",
            }
        ),
    )
    age = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'placeholder': "Date of your app release (format:'Y-m-d')",
            }
        ),
    )
    lastUpdate = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'placeholder': "Last updated date (format:'Y-m-d')",
            }
        ),
    )
    rank = forms.ChoiceField(
        required=True,
        choices=consts.RANKING_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "Select ranking status",
            }
        ),
    )
    reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of reviews (if you have)",
            }
        ),
    )
    installs = forms.ChoiceField(
        required=False,
        choices=consts.INSTALLS_CHOICES,
        widget=forms.Select(
            attrs={
                'name': "Select installs range (if you have)",
            }
        ),
    )
    starRating = forms.DecimalField(
        min_value=0.0,
        max_value=5.0,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Star Rating (if you have, 0 - 5.0)",
            }
        ),
    )
    one_star_reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of 1 star reviews",
            }
        ),
    )
    two_star_reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of 2 star reviews",
            }
        ),
    )
    three_star_reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of 3 star reviews",
            }
        ),
    )
    four_star_reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of 4 star reviews",
            }
        ),
    )
    five_star_reviews = forms.IntegerField(
        min_value=0,
        max_value=999999999,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'placeholder': "Nr of 5 star reviews",
            }
        ),
    )
    description = forms.CharField(
        required=False,
        label="",
        max_length=999999999,
        widget=forms.Textarea(
            attrs={
                'required': False,
                'placeholder': "All text Description (such as: resource permissions,"
                               "new features, user comments.)",
            }
        ),
    )

