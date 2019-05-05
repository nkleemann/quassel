# quassel

Generate a set of random names, words or sentences which are similar to other words, names or sentences.

## Example

#### `sample.txt`:
```
hulu
facebook
spotify
google
instagram
[...1000 other e-brand names]
```
#### Output
```bash
$ python3 generate.py 5 4
fiibly
mootoo
jellyy
boouke
araaon
```

## Note
This is nothing fancy, just a random pick from anarrowed down set of pre-, in- and suffixes chosen and filtered by number of occurence in the sample data. 