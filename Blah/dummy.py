for records in self.Database:
    for k, v in records.items():
        print(k, ":", v, end=" ")
    print()