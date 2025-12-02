def add(x, bucket=[]): bucket.append(x); return bucket
bucket = add(1)        # [1]
print(bucket)
bucket = add(2)        # [1, 2]   ← same list reused
print(bucket)
bucket = add(3)        # [1, 2, 3]   ← same list reused
print(bucket)
# Why: defaults are evaluated once, at function definition time, and if you put a mutable as default it will have this effect.
