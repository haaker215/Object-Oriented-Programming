class pair_elements:
    def twosum(self,nums,target):
        a = {}
        for i, num in  enumerate(nums):
            if target - num in a:
                return(a[target - num],i)
            a[num] = i
value = int(input("Enter the numbrt you want to make this search: "))
print("index1=%d, index2=%d" % pair_elements().twosum((10,20,30,40,50,60,70),value))