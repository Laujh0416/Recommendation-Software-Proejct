from RestaurantData import restaurant_arry
class Restaurant:
    def __init__(self, array):
        self.array = array
        self.bucket = [[] for i in range(len(array))]
        self.insert(array)
        #print(self.bucket)
    
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
    
    def compressor(self, hash_code):
        return hash_code % len(self.array)
    
    def insert(self, array):
        for i in array:
            key = i[0]
            idx = self.compressor(self.hash(key))
            self.bucket[idx].append(i[1])
        self.sorting(self.bucket)
        return
    
    def retrive(self, key):
        idx = self.compressor(self.hash(key))
        values = self.bucket[idx]
        print(values)
        return values

    def sorting(self, bucket):
        for element in bucket:
            for i in element:
                for idx in range(len(element)-1):
                    if element[idx][1] > element[idx+1][1]:
                        element[idx], element[idx+1] = element[idx+1], element[idx]
        
    ######More Specific Function######
    def get_key(self):
        key = []
        for element in self.array:
            if element[0] not in key:
                key.append(element[0])
            continue
        #print(key)
        return key
    
    def arranged_menu(self, key):
        idx = self.compressor(self.hash(key))
        values = self.bucket[idx]
        for restaurant in values:
            print(f"########## Rank {restaurant[1]}##########")
            print(f"|Restaurant: {restaurant[0]}|")
            print(" ")




###Testing Area###
array = [["A", ["A1", 1]], ["B", ["B1", 3]],["B", ["B2", 2]], ["B", ["B3", 8]], ["B", ["B4", 7]], ["B", ["B5", 4]],["B", ["B6", 10]]]

test1 = Restaurant(array)
#test1.insert(array)
#test1.sorting(array)
#print(f"This is {test1.get_key()}")
test1.retrive("A")
print(test1.bucket)
test1.arranged_menu("B")
