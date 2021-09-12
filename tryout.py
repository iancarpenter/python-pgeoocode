import pgeocode

dist = pgeocode.GeoDistance('GB')
print(dist.query_postal_code('WC2N', 'EH53'))
