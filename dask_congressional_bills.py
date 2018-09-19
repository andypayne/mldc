
# Call db.read_text with congress/bills*.json
bills_text = db.read_text('congress/bills*.json')
# Map the json.loads function over all elements
bills_dicts = bills_text.map(json.loads)
# Extract the first element with .take(1) and index to the first position
first_bill = bills_dicts.take(1)[0]
print(first_bill.keys())

# Filter the bills
overridden = bills_dicts.filter(veto_override)
# Print the number of bills retained
print(overridden.count().compute())
# Get the value of the 'title' key
titles = overridden.pluck('title')
# Compute and print the titles
print(titles.compute())


# lifespan - dictionary d
def lifespan(d):
    current = pd.to_datetime(d['current_status_date'])
    intro = pd.to_datetime(d['introduced_date'])
    return (current - intro).days

# Filter bills_dicts
days = bills_dicts.filter(lambda s:s['current_status']=='enacted_signed').map(lifespan)
# Print the mean value of the days bag
print(days.mean().compute())


