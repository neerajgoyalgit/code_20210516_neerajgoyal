import json
import pytest

overweight_count = 0

f = open('data.json')
data = json.load(f)


def bmi_cal(HeightCm, WeightKg):
    bmi = (WeightKg*10000/((HeightCm)*(HeightCm)))
    if bmi < 18.5:
        category = 'Underweight'
        risk = 'Malnutrition risk'
    elif bmi < 25:
        category = 'Normal weight'
        risk = 'Low risk'
    elif bmi < 30:
        category = 'Overweight'
        risk = 'Enhanced risk'
    elif bmi < 35:
        category = 'Moderately obese'
        risk = 'Medium risk'
    elif bmi < 40:
        category = 'Severely obese'
        risk = 'High risk'
    else:
        category = 'Very severely obese'
        risk = 'Very high risk'
    return round(bmi,2), category, risk
        

for i in data:
    bmi, cat, risk = bmi_cal(i['HeightCm'], i['WeightKg'])
    print(i['HeightCm'], i['WeightKg'], bmi, cat, risk)
    if cat == 'Overweight':
        overweight_count += 1

print("overweight count is: ", overweight_count)
        
@pytest.mark.parametrize("test_input1, test_input2, expected_bmi, expected_category, expected_risk", [(171,96, 32.83, 'Moderately obese','Medium risk'),(167,82,29.4, 'Overweight','Enhanced risk')])
def test_eval(test_input1, test_input2, expected):
    assert bmi_cal(test_input1, test_input2) == expected
