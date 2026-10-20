import json, sys
t = json.load(open('tuning.json'))
ranges = {('phone', 'exposure'): (-2, 3), ('phone', 'fill'): (0.2, 6), ('desktop', 'exposure'): (-2, 3), ('desktop', 'fill'): (0.2, 6)}
for k in ('account', 'creator', 'lobby', 'table'):
    ranges[('scale', k)] = (0.5, 2)
bad = []
for (group, key), (lo, hi) in ranges.items():
    v = t.get(group, {}).get(key)
    if not isinstance(v, (int, float)) or not lo <= v <= hi:
        bad.append(f'{group}.{key} = {v!r} (must be {lo} to {hi})')
if bad:
    sys.exit('tuning.json:\n  ' + '\n  '.join(bad))
print('tuning.json is good')
