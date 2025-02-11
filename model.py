import pandas as pd

def normalize(value, min_value, max_value, invert=False):
    """Normalizes a value between 0 and 100."""
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
    
    data['price_growth_norm'] = normalize(data['price_growth'], 2, 10)
    data['rental_yield_norm'] = normalize(data['rental_yield'], 3, 10)
    data['crime_rate_norm'] = normalize(data['crime_rate'], 2, 15, invert=True)
    data['proximity_transit_norm'] = normalize(data['proximity_transit'], 100, 2000, invert=True)
    data['population_growth_norm'] = normalize(data['population_growth'], 0.5, 3)
    
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
