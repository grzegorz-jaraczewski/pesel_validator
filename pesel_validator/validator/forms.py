from django import forms


class PeselForm(forms.Form):
    """
    Django form for validating PESEL input.

    Fields:
        pesel (CharField): A required text input for the PESEL number.
            - Must be exactly 11 digits long.
            - Includes a placeholder guiding the user to enter their PESEL.

    This form does not perform PESEL validation itself, it only ensures the
    input length and type. Validation logic is handled separately.
    """

    pesel = forms.CharField(
        max_length=11,
        min_length=11,
        label="PESEL",
        widget=forms.TextInput(attrs={"placeholder": "Enter PESEL number"})
    )
