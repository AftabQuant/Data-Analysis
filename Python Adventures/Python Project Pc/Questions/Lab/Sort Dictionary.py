dist = {
    "apple" : 5, "banana" : 2, "cherry" : 4, "date" : 1
}
print(dist)

def sort_asc(dist) :
    asc = dict(sorted(dist.items(), key = lambda item : item[1]))
    print(asc)

def sort_desc(dist) :
    desc = dict(sorted(dist.items(), key = lambda i : i[1], reverse=True))
    print(desc)

sort_asc(dist)
sort_desc(dist)