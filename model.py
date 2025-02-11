import pandas as pd

def normalize(value, data_series, invert=False):
    """Dynamically normalizes a value between 0 and 100 based on min and max of dataset."""
    min_value, max_value = data_series.min(), data_series.max()
    score = (value - min_value) / (max_value - min_value) * 100
    return 100 - score if invert else score

def calculate_investment_score(data):
    """Computes the final investment score based on weighted parameters."""
    weights = {
        'price_growth': 0.3,
        'rental_yield': 0.25,
        'crime_rate': 0.2,
        'proximity_transit': 0.15,
        'population_growth': 0.1
    }
    
    data['price_growth_norm'] = data['price_growth'].apply(lambda x: normalize(x, data['price_growth']))
    data['rental_yield_norm'] = data['rental_yield'].apply(lambda x: normalize(x, data['rental_yield']))
    data['crime_rate_norm'] = data['crime_rate'].apply(lambda x: normalize(x, data['crime_rate'], invert=True))
    data['proximity_transit_norm'] = data['proximity_transit'].apply(lambda x: normalize(x, data['proximity_transit'], invert=True))
    data['population_growth_norm'] = data['population_growth'].apply(lambda x: normalize(x, data['population_growth']))
    
    data['final_score'] = (
        data['price_growth_norm'] * weights['price_growth'] +
        data['rental_yield_norm'] * weights['rental_yield'] +
        data['crime_rate_norm'] * weights['crime_rate'] +
        data['proximity_transit_norm'] * weights['proximity_transit'] +
        data['population_growth_norm'] * weights['population_growth']
    )
    
    return data

def assign_rating(score):
    """Assigns an investment rating based on the final score."""
    if score >= 85:
        return 'A+'
    elif score >= 70:
        return 'A'
    elif score >= 50:
        return 'B'
    elif score >= 30:
        return 'C'
    else:
        return 'D'

# Example Data
example_data = pd.DataFrame({
    'price_growth': [6, 8, 3],
    'rental_yield': [7, 5, 4],
    'crime_rate': [5, 10, 12],
    'proximity_transit': [800, 400, 1500],
    'population_growth': [1.5, 2.5, 0.7]
})

# Calculate investment score
scored_data = calculate_investment_score(example_data)
scored_data['investment_rating'] = scored_data['final_score'].apply(assign_rating)

# Display results
print(scored_data)
