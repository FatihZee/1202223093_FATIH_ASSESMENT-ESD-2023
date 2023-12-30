def analyze_reviews(ratings):
    if not ratings:
        return None

    min_rating = round(min(ratings), 1)
    max_rating = round(max(ratings), 1)
    avg_rating = round(sum(ratings) / len(ratings), 1)
    
    min_rating = int(min_rating) if min_rating.is_integer() and min_rating % 1 == 0 else min_rating
    max_rating = int(max_rating) if max_rating.is_integer() and max_rating % 1 == 0 else max_rating
    avg_rating = int(avg_rating) if avg_rating.is_integer() and avg_rating % 1 == 0 else avg_rating

    return [min_rating, max_rating, avg_rating]

input_reviews_str = input("Masukkan daftar rating aplikasi: ")

input_reviews_str = input_reviews_str.replace(',', ', ')

input_reviews = [float(rating) for rating in input_reviews_str.split(', ')]

output = analyze_reviews(input_reviews)
print("Output:", output)